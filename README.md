# Excelerate Data Preparation - Team 11

Welcome to the **Data Understanding & Preparation Package** repository for Week 1. This project focuses on auditing, cleaning, and structuring raw programmatic data (Competitions, Virtual Internships, Corporate Simulations, and Masterclasses) extracted from a NoSQL database source.An executive-grade visual intelligence platform analyzing 5,674 platform offerings across 10 verticals. Developed during the Excelerate Data Visualization Trainee Internship, this repository consolidates Week 2 exploratory data analysis (EDA) and Week 3 interactive SaaS dashboard architecture.


![Python](https://img.shields.io/badge/Python-white?style=for-the-badge&logo=Python)
![NumPy](https://img.shields.io/badge/NumPy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Visuals](https://img.shields.io/badge/Data_Visualization-skyblue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)
![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=Tableau&logoColor=white)
![Status](https://img.shields.io/badge/Deliverable-Week%203%20Complete-emerald?style=for-the-badge)
![Status](https://img.shields.io/badge/Deliverable-Week%202%20Complete-azure?style=for-the-badge)



---
## 👥 Team Members

* **Olasope Omolola (Team Leader)** 
* **Sanskar Muneshwar (Dashboard Developer)**
* **Sadhna MM (Documentation Reports Lead)**
* **Gordan Moenga**
* **Muhammad Waqar Tahir**
* **Keerti Betagiri(Data Insights & Interpretation Lead)**
* **Silah Tarbai (Insights & Analytics Lead)**
* **Nash Were**
---
---

## 📌 Executive Summary & Key Metrics

* **Total Active Listings:** 5,674 opportunities analyzed across 43 standardized attributes.
* **Micro-Scholarship Coverage:** 86.2% of opportunities include financial support, with a standardized median award of **$120**.
* **Delivery Infrastructure:** 74.6% of programs operate via remote infrastructure (**41.1% Work From Home**, **33.5% Virtual**).
* **Tuition Access Model:** 78.9% (4,477 listings) are fully free access ($0 tuition fee).
* **Operational Intake Bottleneck:** 85.9% of application pipelines require manual staff review, exhibiting high latency during cyclical batch spikes (July, October/November, February/March).

---

## 🖥️ Week 3 Interactive UI Dashboard

Built with modern SaaS UI card architecture (`#F4F6F9` canvas, floating white cards, 1px `#E2E8F0` structural boundaries, and dark brand navigation sidebar).

![Executive Dashboard Preview](Week_3_Dashboard/assets/dashboard_preview.png)

### Key Dashboard Components:
1. **Left Filter Navigation Dock:** Global multi-select dropdowns for `Category`, `Location Format`, `Currency Type`, and `Approval Protocol`.
2. **Top KPI Status Banner:** Real-time totals, median scholarship allocation, remote penetration rate, and zero-fee access ratios.
3. **Monthly Trajectory:** Dual-axis time series capturing cohort intake spikes across 3.8 longitudinal years.
4. **Application Format Distribution:** Horizontal volume benchmarks for Remote delivery.
5. **Workflow Automation Highlight Matrix:** Percent-of-total operational grid identifying high-automation tracks (e.g., Competitions at ~29%) vs. gatekept tracks (Careers at ~3.7%).
6. **Program Density Bubble Grid:** Packed cluster volume scaling by track size.
7. **Financial Structural Scatter Grid:** Non-aggregated parametric distribution benchmarking duration days vs. tuition fees.
8. **Track Mix Profile:** Dual-axis center-KPI donut detailing categorical portfolio share.

---

## 📊 Week 2 Python Visual Explorations

Standalone high-resolution (300 DPI) analysis scripts exploring supplemental dimensions not covered in BI dashboards:

| Visual Output | Focus Area | Analytical Takeaway |
| :--- | :--- | :--- |
| **Duration Units Lollipop** | Program Scheduling | 75.4% of catalog durations are structured in weekly increments. |
| **Monetization Donut** | Revenue Architecture | 78.9% free access baseline; paid programs (21.1%) cluster heavily in Events and Internships. |
| **Scholarship Tiers Donut** | Financial Subsidy | 68.0% of all platform micro-scholarships sit in the standard $101–$250 tier. |
| **Feature Adoption Funnel** | Engagement Completeness | Badges, Eligibility, and Cohort IDs exceed 87% adoption; Testimonials remain underutilized at 3.6%. |
| **Metric Correlation Heatmap** | Inter-variable Dependency | Negative correlation between Duration and Rewards ($r = -0.48$) highlights micro-incentive deployment for shorter tracks. |

---

## 🛠️ Reproduction & Setup

###  Clone Repository
```bash
git clone [https://github.com/sanskar00-debug/excelerate-data-preparation.git](https://github.com/sanskar00-debug/excelerate-data-preparation.git)
cd excelerate-data-preparation

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
python notebooks/generate_opportunities_visuals.py
``` 

## 🚀 How to Run the Pipeline

### Prerequisites
Ensure you have Python 3.x installed alongside the `pandas` and `numpy` data engineering modules:
```bash
pip install pandas numpy
```

## 🗒️ Milestone Outcomes
* ** Tabular Schema Clarity:** Clean separation between transactional metadata markers and natural content variables.
* ** Statistical Readiness:** Complete unification of shifting chronological lengths to single numerical indices ready for rapid analytics.
* ** Core Skew:** The catalog operates as a highly standardized, long-duration (210 Days), USD-dominated ecosystem requiring dedicated human gatekeeping layers.
* ** Agile Windows:** Automation expansion should target *Engagement* and *Event* tracks to mimic the success of *Competition* workflows and alleviate manual                         review bottlenecks.
