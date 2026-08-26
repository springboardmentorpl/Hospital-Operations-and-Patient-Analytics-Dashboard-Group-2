# MedTrack_DV — Hospital Operations & Patient Analytics Dashboard

## Project Statement

This project aims to develop a comprehensive hospital operations and patient analytics dashboard suite for analyzing hospital performance, patient admissions, department efficiency, and healthcare resource utilization.

Using an independently sourced hospital patient dataset (`hospital_patient_analytics_expanded.csv`), this project transforms raw healthcare operational data into actionable insights through interactive Tableau dashboards.

The final deliverable is a unified Tableau workbook consisting of four interconnected dashboards:
- Hospital Overview
- Patient Flow
- Department Analytics
- Resource Utilization

---

## Tech Stack

| Area | Tools / Libraries |
|---|---|
| Data Collection | Python, self-sourced hospital patient dataset |
| Data Processing | Pandas, NumPy |
| Data Cleaning | Python |
| Visualization | Tableau Desktop / Tableau Public |
| Dashboard Integration | Tableau Filters, Parameters, Actions |
| Documentation | Markdown, GitHub |

---

## Module 1: Hospital Data Collection

**Status:** ✅ Complete

**Tasks**
- Collected raw hospital patient dataset
- Reviewed structure and quality of dataset

**Deliverables**
- [hospital_patient_analytics_expanded.csv](./data/hospital_patient_analytics_expanded.csv) — raw dataset

**Evaluation**
- Dataset successfully collected and loaded
- 15,000 records, 12 columns

---

## Module 2: Data Cleaning & Transformation

**Status:** ✅ Complete

**Tasks**
- Standardized inconsistent Gender values
- Removed invalid records (negative bill amounts)
- Removed duplicate patient records
- Parsed mixed date formats
- Handled missing values (Age, City, Insurance_Provider, Patient_Satisfaction_Score, Discharge_Date)
- Engineered new features (Length_of_Stay, Admission_Year/Month/Quarter/Day, Age_Group, Bill_Category, Stay_Category)

**Deliverables**
- [Hospital_Analytics_notebook.ipynb](./notebook/Hospital_Analytics_notebook.ipynb) — cleaning & transformation notebook
- [hospital_operations_patient_analytics_cleaned.csv](./data/hospital_operations_patient_analytics_cleaned.csv) — cleaned dataset

**Evaluation**
- Final dataset: 14,734 records, 20 columns
- 0 missing values remaining

---

## Module 3: Hospital KPI Engineering

**Status:** ⏳ In Progress

**Tasks**
- Calculate Total Admissions
- Calculate Occupancy Rate
- Calculate Average Length of Stay
- Calculate Readmission Rate
- Calculate Bed Utilization Rate
- Calculate Department Efficiency Score

**Deliverables**
- KPI definitions note *(to be added)*

**Evaluation**
- All KPIs correctly calculated
- Dataset optimized for Tableau

---

## Module 4: Dashboard Planning & Prototyping

**Status:** ⏳ In Progress

**Tasks**
- Design layouts for Hospital Overview, Patient Flow, Department Analytics, Resource Utilization
- Define filters, navigation, dashboard actions, department comparisons

**Deliverables**
- [dashboard_storyboard.pdf](./dashboard/dashboard_storyboard.pdf) — dashboard structure/storyboard file

**Evaluation**
- Dashboard designs approved
- Prototype functionality verified

---

## Module 5: Build Hospital Overview & Patient Flow Dashboards

**Status:** ✅ Complete

**Tasks**
- Hospital Overview: admissions overview, occupancy monitoring, readmission analysis, hospital performance KPIs, monthly operational trends
- Patient Flow: admission trends, discharge tracking, patient movement analysis, average stay analysis, peak patient load monitoring

**Deliverables**
- [medtrack_dashboard_v1.twbx](./dashboard/medtrack_dashboard_v1.twbx)

**Evaluation**
- Interactive visualizations operational
- Hospital KPIs validated

---

## Module 6: Build Department Analytics & Resource Utilization Dashboards

**Status:** ⏳ Not Started

**Tasks**
- Department Analytics: department performance, patient volume, readmission by department, efficiency comparison, treatment capacity
- Resource Utilization: bed utilization, staff allocation, equipment utilization, capacity planning, resource availability
- Dashboard integration: global filters, navigation controls, parameter actions, dashboard linking

**Deliverables**
- [MedTrack_DV.twbx](./dashboard/MedTrack_DV.twbx)

**Evaluation**
- All dashboards integrated
- Navigation and filters functioning correctly

---

## Module 7: Testing and Validation

**Status:** ⏳ Not Started

**Tasks**
- Validate KPI calculations
- Verify healthcare metrics
- Test dashboard interactions
- Validate patient flow analytics

**Deliverables**
- QA Checklist
- Dashboard Testing Report

**Evaluation**
- No major dashboard issues
- KPI accuracy above 95%

---

## Module 8: Documentation and Project Delivery

**Status:** ⏳ Not Started

**Tasks**
- Prepare dataset sources, KPI definitions, dashboard guide, methodology documentation
- Organize project structure
- Deploy to GitHub / Tableau Public

**Deliverables**
- GitHub Repository
- Final Documentation
- Tableau Workbook

**Evaluation**
- Fully documented project
- Portfolio-ready dashboard suite

---

## Project Structure

```
Hospital_Analytics/
│
├── data/
│   ├── hospital_patient_analytics_expanded.csv
│   └── hospital_operations_patient_analytics_cleaned.csv
│
├── notebook/
│   └── Hospital_Analytics_notebook.ipynb
│
├── dashboard/
│   ├── dashboard_storyboard.pdf
│   ├── medtrack_dashboard_v1.twbx
│   └── MedTrack_DV.twbx
│
└── README.md
```

---

## Conclusion

The hospital patient dataset was successfully cleaned and transformed using Python and Pandas. Missing values, duplicate records, inconsistent categorical values, and invalid billing records were addressed, and new analytical features were engineered. Two of the four planned Tableau dashboards (Hospital Overview and Patient Flow) are complete; Department Analytics, Resource Utilization, KPI documentation, testing, and final delivery are in progress.

*This project was independently built as a practice/portfolio project, inspired by the MedTrack_DV hospital analytics framework, using a self-sourced dataset.*
