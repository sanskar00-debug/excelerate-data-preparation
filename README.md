# Excelerate Data Preparation - Team 11

Welcome to the **Data Understanding & Preparation Package** repository for Week 1. This project focuses on auditing, cleaning, and structuring raw programmatic data (Competitions, Virtual Internships, Corporate Simulations, and Masterclasses) extracted from a NoSQL database source.

![Python](https://img.shields.io/badge/Python-white?style=for-the-badge&logo=Python)
![NumPy](https://img.shields.io/badge/NumPy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Analytics](https://img.shields.io/badge/Data_Analytics-pink?style=for-the-badge)
![Visuals](https://img.shields.io/badge/Data_Visualization-skyblue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)



## 📌 Project Overview
The raw dataset contains complex NoSQL string structures, varying chronological time units, and embedded structural markup flags that limit direct analysis. This repository provides an automated Python pipeline to standardize metrics, flatten JSON blocks, and clean descriptive data for dashboard configurations in Week 2.

## 🛠️ Repository Schema & Architecture
* `/data/raw/`: Houses the baseline uncleaned raw dataset catalog.
* `/data/processed/`: Contains the stable, analytically unified `cleaned_opportunities.csv`.
* `/scripts/`: Holds the automated preprocessing execution code (`data_cleaning.py`).
* `/documentation/`: Features the deep dive `Data_Quality_Report.md`.

## ⚙️ Implemented Transformations
The processing pipeline executes four core cleaning phases:
1. **Missing State Alignment:** Converts mixed string indicators (`NULL`, `null`, `Null`, `{}`, `[]`) into machine-readable `NaN` properties.
2. **paired Metric Standardization:** Maps inconsistent tracking variables (`minutes`, `weeks`, `years`) into a standardized continuous column: `duration_standard_days`.
3. **NoSQL Flattening Blocks:** Unpacks layered text attributes (`Badge`, `Cohort`, `Reward`) to cleanly present database indices directly inside explicit relational strings.
4. **HTML Strip Processing:** Applies regular expression filters to remove structural layout markers from description parameters, outputting clean plain text blocks.

### Advanced Cleansing Strategies Implemented:
1. **Data Loss Profiling (Corruption Scrub):** Three rows containing raw string anomalies (`%22`, stray escaping parameters) were explicitly dropped. This action preserves type coercion for numerical algorithms without impacting sample size.
2. **Geographic Standardization:** Clustered chaotic location representations into a tight dictionary controlled category (`Virtual`, `Work From Home`, `Kolkata`). Test entries (`qwerty`, text headers) were converted to standardized system `NaN` states.
3. **Financial Feature Standardization:** Unified financial tracking variables by mapping all instances of `EURO` to `EUR`. Executed rigorous float parsing across `fee` and `microscholarship` attributes to prevent string value system errors in dashboard tools.
4. **Identity Format Optimization:** Cleaned `current_editor` by stripping NoSQL object structures. Fields are now uniformly stored as flat email strings or comma-separated lists for collaborative records.
5. **Deduplication Validation:** Fixed identification conflicts within the `code` array column by applying a newest-date tracking strategy, keeping the latest administrative updates and filtering out stale entries.
6. **Unified Schema Architecture:** Eliminated structural inconsistency by flattening all remaining JSON tracking arrays (`Panellist`, `Testimonial`, `DropoutTransaction`, `NotStartedTransaction`, `tracking_questions`), extracting their unique identity strings (`_clean_id`) to ensure clean access across the final dataset.
 ## 📊 Week 2: Exploratory Data Analysis (EDA) & Visual Layer

The engineered data was processed using Python visualization libraries to track operational patterns, timelines, and financial mix trends across **5,730 verified records**.

### 1. Temporal Trends: Opportunity Creation Trajectory
![Monthly Opportunity Creation Trajectory](documentation/charts/opportunities_creation_trajectory.png)
* **Visual Insight:** The line chart reveals a cyclical, spike-driven posting history peaking aggressively in late Q3 (Sept 2023) and mid-Q2 (May 2024), reaching up to 1,000+ new cohorts simultaneously before hitting sharp baseline drops. 
* **Strategic Interpretation:** Portfolio expansion is highly seasonal. This behavior shows distinct administrative batch processing windows, heavily synchronized around early-semester and mid-year academic lifecycle enrollment periods.

### 2. Operational Durations: Timeline Distributions
![Program Duration Distribution](documentation/charts/program_duration_distribution.png)
* **Visual Insight:** The distribution histogram shows an intense structural spike heavily concentrated around the **210-day marker**, with a secondary minor cluster sitting under 50 standard days.
* **Strategic Interpretation:** The portfolio relies almost entirely on fixed, long-form core timelines (~7 months) rather than micro-learning increments. This reveals an active platform focus on deep, multi-stage engagement tracks over brief episodic experiences.

### 3. Workflow Automation: Application Approval Protocols
![Application Approval Protocol by Category](documentation/charts/application_approval_protocol.png)
* **Visual Insight:** Across nearly all categories (such as *Internships, Courses, and Careers*), over **75% to 90% of applicant traffic requires manual review**, whereas *Competition* tracks present the highest automated validation throughput (~30% Auto-Approve).
* **Strategic Interpretation:** The platform maintains strict administrative gatekeeping. Higher automation in competitions points to objective, system-scored assessment mechanics, while career and internship categories require manual screening to manage quality control.

### 4. Financial Demographics: Currency Denomination Mix
![Currency Denomination Mix Across Top Categories](documentation/charts/currency_denomination_mix.png)
* **Visual Insight:** The financial bar chart exposes a heavy dominance of **USD currency configurations** across every single portfolio category, with *Internships* providing the only visible footprint for alternative currencies like *INR* and *EUR*.
* **Strategic Interpretation:** The business layer operates on a highly globalized monetization framework. While local target currency execution paths exist within internships, the ecosystem is built around a standardized international financial baseline.

  ## 🚀 Execution & Reproducibility Pipeline

Ensure you have your environment updated with `pandas`, `numpy`, `matplotlib`, and `seaborn` installed:
```bash
pip install pandas numpy matplotlib seaborn
```

### 1. Finalize Data Cleaning (Week 1)
```bash
python scripts/data_cleaning.py
```
### 2. Regenerate Analytical Charts (Week 2)
```bash
python scripts/generate_eda_charts.py
``` 

## 🚀 How to Run the Pipeline

### Prerequisites
Ensure you have Python 3.x installed alongside the `pandas` and `numpy` data engineering modules:
```bash
pip install pandas numpy
```

### Execution Steps
1. Clone this repository to your local terminal path:
   ```bash
   git clone https://github.com
   ```
2. Navigate into the script directories and execute the cleaning script:
   ```bash
   python scripts/data_cleaning.py
   ```
3. Locate your normalized tabular production output stored directly inside the `/data/processed/` folder directories.

## 🗒️ Milestone Outcomes
* ** Tabular Schema Clarity:** Clean separation between transactional metadata markers and natural content variables.
* ** Statistical Readiness:** Complete unification of shifting chronological lengths to single numerical indices ready for rapid analytics.
* ** Core Skew:** The catalog operates as a highly standardized, long-duration (210 Days), USD-dominated ecosystem requiring dedicated human gatekeeping layers.
* ** Agile Windows:** Automation expansion should target *Engagement* and *Event* tracks to mimic the success of *Competition* workflows and alleviate manual                         review bottlenecks.
