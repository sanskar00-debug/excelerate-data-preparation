import pandas as pd
import json
import numpy as np

def clean_opportunity_data(file_path, output_path="cleaned_opportunities.csv"):
    print(f"Reading file from: {file_path}...")
    
    # FIXED LINE: Removed the unexpected argument causing your error
    df = pd.read_csv(file_path)
    
    # 1. Standardize mixed string representations of empty fields to proper NaNs
    print("Standardizing missing values...")
    null_variants = ["NULL", "null", "Null", "{}", "[]", " ", ""]
    df = df.replace(null_variants, np.nan)
    
    # 2. Parse Unix Epoch Timestamps (Milliseconds) into clean Date-Times
    print("Converting database timestamps...")
    timestamp_cols = ['created_at', 'modified_at', 'last_date_to_apply']
    for col in timestamp_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(pd.to_numeric(df[col], errors='coerce'), unit='ms', errors='coerce')
            
    # 3. Regularize string Boolean switches into true Python Booleans 
    print("Standardizing logical flags...")
    bool_cols = ['is_archived', 'is_auto_approve']
    for col in bool_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.upper().map({'TRUE': True, 'FALSE': False})
            df[col] = df[col].fillna(False)
            
    # 4. Standardize paired tracking units into a uniform analytical field: Standard Days
    print("Normalizing program durations to metric standard days...")
    def normalize_to_days(row):
        try:
            val = float(row['duration'])
            unit = str(row['duration_type']).lower().strip()
        except (ValueError, TypeError):
            return np.nan
            
        if pd.isna(val) or pd.isna(unit):
            return np.nan
        if 'minute' in unit:
            return round(val / 1440, 4)
        elif 'hour' in unit:
            return round(val / 24, 4)
        elif 'day' in unit:
            return round(val, 4)
        elif 'week' in unit:
            return round(val * 7, 4)
        elif 'month' in unit:
            return round(val * 30.4375, 4)
        elif 'year' in unit:
            return round(val * 365.25, 4)
        return np.nan

    if 'duration' in df.columns and 'duration_type' in df.columns:
        df['duration_standard_days'] = df.apply(normalize_to_days, axis=1)
        
    # 5. Extract structural identifier keys safely out of text JSON structures
    print("Flattening stringified JSON structures...")
    def parse_structural_sk(val):
        if pd.isna(val) or not isinstance(val, str):
            return np.nan
        try:
            parsed = json.loads(val)
            if isinstance(parsed, dict):
                return parsed.get('sk', np.nan)
            elif isinstance(parsed, list) and len(parsed) > 0:
                return parsed[0].get('sk', np.nan) if isinstance(parsed[0], dict) else np.nan
        except json.JSONDecodeError:
            pass
        return np.nan

    structural_json_cols = ['Badge', 'Eligibility', 'Reward', 'Cohort', 'CareerAddOn']
    for col in structural_json_cols:
        if col in df.columns:
            df[f'{col}_clean_id'] = df[col].apply(parse_structural_sk)
            
    # 6. Extract raw clear text out of structural HTML elements
    print("Stripping HTML elements out of text columns...")
    if 'role_responsibility' in df.columns:
        df['role_responsibility_clean'] = df['role_responsibility'].astype(str).str.replace(r'<[^>]*>', '', regex=True).str.strip()
        df['role_responsibility_clean'] = df['role_responsibility_clean'].replace(['nan', 'NAN'], np.nan)

    # Export target file
    print(f"Saving fully processed Cleaned Dataset file to: {output_path}")
    df.to_csv(output_path, index=False)
    print("Data cleaning successfully completed!")
    return df

if __name__ == "__main__":
    # This matches the raw file name seen in your console error path
    raw_file = "opportunity_dataset.csv" 
    clean_opportunity_data(file_path=raw_file, output_path="cleaned_opportunities.csv")
