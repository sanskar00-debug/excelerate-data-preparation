# Experiential Learning Opportunity Dataset - Data Preparation Package

Welcome to the **Data Understanding & Preparation Package** repository for Week 1. This project focuses on auditing, cleaning, and structuring raw programmatic data (Competitions, Virtual Internships, Corporate Simulations, and Masterclasses) extracted from a NoSQL database source.

![Python](https://img.shields.io/badge/Python-white?style=for-the-badge&logo=Python)
![NumPy](https://img.shields.io/badge/NumPy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Analytics](https://img.shields.io/badge/Data_Analytics-pink?style=for-the-badge)
![Visuals](https://img.shields.io/badge/Data_Visualization-beige?style=for-the-badge)


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
