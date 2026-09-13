import pandas as pd
import json
import numpy as np
import re

def advanced_clean_pipeline(file_path, output_path="data/processed/cleaned_opportunities.csv"):
    print("🚀 Initializing Advanced Data Cleaning Pipeline...")
    
    # 1. Safe ingestion of raw csv file
    df = pd.read_csv(file_path)
    initial_row_count = len(df)
    
    # -------------------------------------------------------------------------
    # ACTION 1: Locate and Resolve Corrupted Rows (%22 or stray \"\")
    # -------------------------------------------------------------------------
    print("🧹 Action 1: Scanning for string corruptions (%22 or stray escaping)...")
    # Generate an analytical mask checking all columns for corruption patterns
    corruption_mask = df.astype(str).apply(
        lambda col: col.str.contains(r'%22|\\\"\"|""', na=False, regex=True)
    ).any(axis=1)
    
    corrupted_count = corruption_mask.sum()
    print(f"   -> Found {corrupted_count} corrupted data entries.")
    
    # Decision: Drop corrupted records to protect downstream data types (defensible out of 5,733)
    df = df[~corruption_mask].reset_index(drop=True)
    print(f"   -> Successfully excluded corrupted records. Rows remaining: {len(df)}")

    # -------------------------------------------------------------------------
    # ACTION 2: Standardize Location into a Controlled Structural List
    # -------------------------------------------------------------------------
    print("📍 Action 2: Standardizing geographic and location strings...")
    if 'location' in df.columns:
        # Initial cleanup of whitespaces and string variations
        df['location'] = df['location'].astype(str).str.strip()
        
        # Mapping dictionaries for strict standardization
        location_map = {
            r'(?i)^virt.*$': 'Virtual',
            r'(?i)^wfm$|^work\s*from\s*home$': 'Work From Home',
            r'(?i)^kolkata$': 'Kolkata',
            r'(?i)^location$': np.nan  # Stripping stray table header rows
        }
        
        for pattern, replacement in location_map.items():
            df['location'] = df['location'].replace(pattern, replacement, regex=True)
            
        # Eliminate junk testing entries or placeholder content
        junk_patterns = [r'(?i)elit\s+cum', r'(?i)qwerty', r'(?i)page\s+testing']
        for junk in junk_patterns:
            df['location'] = df['location'].replace(junk, np.nan, regex=True)
            
        # Re-map standard pandas string null values back to true NaNs
        df['location'] = df['location'].replace(['nan', 'NAN', 'None', ''], np.nan)

    # -------------------------------------------------------------------------
    # ACTION 3: Merge Currency Types & ACTION 4: Numeric Conversions
    # -------------------------------------------------------------------------
    print("💵 Action 3 & 4: Normalizing financial metrics and tracking codes...")
    if 'currency_type' in df.columns:
        df['currency_type'] = df['currency_type'].astype(str).str.strip().str.upper()
        df['currency_type'] = df['currency_type'].replace({'EURO': 'EUR'})
        df['currency_type'] = df['currency_type'].replace(['NAN', 'NONE', ''], np.nan)

    # Convert numeric fields after removing corrupted strings that break typing rules
    numeric_targets = ['fee', 'microscholarship']
    for col in numeric_targets:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0.0)

    # -------------------------------------------------------------------------
    # ACTION 5: Standardize current_editor Formats
    # -------------------------------------------------------------------------
    print("📧 Action 5: Extracting and unifying editor identification accounts...")
    if 'current_editor' in df.columns:
        def parse_editor(val):
            if pd.isna(val) or not isinstance(val, str):
                return np.nan
            val_clean = val.strip()
            # If wrapped in a NoSQL stringified JSON map object
            if val_clean.startswith('{') and val_clean.endswith('}'):
                try:
                    parsed = json.loads(val_clean)
                    # Pull values out if stored as key list parameters
                    if isinstance(parsed, dict):
                        emails = parsed.get('emails', parsed.get('email', np.nan))
                        if isinstance(emails, list):
                            return ", ".join([str(e).strip() for e in emails])
                        return str(emails).strip() if emails else np.nan
                except json.JSONDecodeError:
                    pass
            return val_clean

        df['current_editor'] = df['current_editor'].apply(parse_editor)
        df['current_editor'] = df['current_editor'].replace(['nan', 'NAN', '{}', '[]'], np.nan)

    # -------------------------------------------------------------------------
    # ACTION 6: Investigate & Resolve Duplicate Code System Metrics
    # -------------------------------------------------------------------------
    print("🆔 Action 6: Auditing duplicate code value parameters...")
    if 'code' in df.columns:
        # Deduplication Strategy: Identify records sharing codes, sort by modification date
        if 'modified_at' in df.columns:
            df = df.sort_values(by='modified_at', ascending=False)
        
        # Keep the most recent modified record entry and drop older conflicting code rows
        df = df.drop_duplicates(subset=['code'], keep='first').reset_index(drop=True)
        print(f"   -> Code tracking resolved. Rows remaining: {len(df)}")

    # -------------------------------------------------------------------------
    # ACTION 7: Comprehensive Structural JSON Flattening Pipeline
    # -------------------------------------------------------------------------
    print("🏗️ Action 7: Unpacking remaining raw NoSQL JSON structures uniformly...")
    def extract_clean_id(val):
        if pd.isna(val) or not isinstance(val, str):
            return np.nan
        val_clean = val.strip()
        try:
            # Handle empty dictionary string anomalies
            if val_clean in ["{}", "[]", ""]:
                return np.nan
            parsed = json.loads(val_clean)
            if isinstance(parsed, dict):
                return parsed.get('sk', parsed.get('id', np.nan))
            elif isinstance(parsed, list) and len(parsed) > 0:
                # If wrapped inside an array array list configuration block
                first_item = parsed[0]
                if isinstance(first_item, dict):
                    return first_item.get('sk', first_item.get('id', np.nan))
        except json.JSONDecodeError:
            pass
        return np.nan

    # Process ALL remaining nested fields to ensure full consistency across your schema
    all_json_fields = [
        'Badge', 'Eligibility', 'Reward', 'Cohort', 'CareerAddOn',
        'Panellist', 'Testimonial', 'DropoutTransaction', 
        'NotStartedTransaction', 'tracking_questions'
    ]
    
    for field in all_json_fields:
        if field in df.columns:
            df[f'{field}_clean_id'] = df[field].apply(extract_clean_id)
            print(f"   -> Standardized key IDs extracted for column: {field}_clean_id")

    # Final Export Summary Check
    print(f"💾 Saving clean production target file to: {output_path}")
    df.to_csv(output_path, index=False)
    print("🏆 High-fidelity clean dataset generated successfully!")
    return df

if __name__ == "__main__":
    import os
    
    # 1. Automatically create the directory structure if it is missing
    os.makedirs("data/processed", exist_ok=True)
    
    # 2. Run the advanced cleaning pipeline exactly as before
    raw_file = "opportunity_dataset.csv"
    advanced_clean_pipeline(file_path=raw_file, output_path="data/processed/cleaned_opportunities.csv")

