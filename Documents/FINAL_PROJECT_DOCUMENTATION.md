# MedTrack_DV

## Hospital Operations & Patient Analytics Dashboard

### Final Project Documentation — Module 8: Documentation and Project Delivery

---

# 1. Project Overview

MedTrack_DV is an interactive Tableau dashboard suite designed to analyze hospital operations and patient analytics.

The project transforms cleaned and enriched healthcare patient-flow data into interactive dashboards covering:

- Hospital performance
- Patient admissions
- Patient flow
- Department performance
- Resource utilization

The final Tableau workbook contains four dashboards:

1. Hospital Overview
2. Patient Flow
3. Department Analytics
4. Resource Utilization

---

# 2. Problem Statement

Healthcare organizations generate large amounts of patient and operational data.

Without an integrated analytical solution, it can be difficult to understand:

- Patient admission patterns
- Patient waiting time
- Length of stay
- Readmission
- Department performance
- Hospital occupancy
- Bed utilization
- Resource utilization

MedTrack_DV addresses this problem by providing an interactive Tableau dashboard suite for healthcare operations analysis.

The dashboard suite helps hospital administrators, healthcare managers, medical staff, and policymakers monitor patient flow, evaluate department performance, optimize hospital resources, and improve operational efficiency through data-driven decision-making.

---

# 3. Project Objectives

The project objectives are:

- Analyze hospital admissions.
- Monitor patient flow.
- Monitor occupancy.
- Analyze average length of stay.
- Analyze readmission.
- Analyze patient satisfaction.
- Compare department performance.
- Monitor bed utilization.
- Analyze healthcare resource utilization.
- Generate healthcare operational KPIs.
- Deliver an integrated Tableau dashboard suite.

---

# 4. Dataset

The Tableau workbook uses:

`cleaned_healthcare_patient_flow_data_enriched.csv`

The dataset was built from publicly available Hospital Datasets and Patient Admission Datasets, then cleaned, transformed, and enriched for healthcare operations analytics.

The dataset contains patient, admission, department, patient-flow, discharge, outcome and resource-related fields.

---

# 5. Main Dataset Fields

## Patient Fields

```text
patient_id
patient_age
patient_gender
patient_race
age_group
```

## Admission Fields

```text
patient_admission_date
patient_admission_time
admission_status
admission_shift
patient_admission_flag
admission_year_month
```

## Department Fields

```text
department_referral
department_group
department_efficiency_score
```

## Patient Flow Fields

```text
patient_waittime
waittime_category
waittime_over_45min
length_of_stay_days
```

## Discharge Fields

```text
patient_discharge_date
discharge_year_month
discharge_month_name
```

## Outcome Fields

```text
is_readmitted
readmission_status
patient_satisfaction_score
```

## Resource Fields

```text
total_beds
occupied_beds
bed_occupancy_rate
```

---

# 6. Healthcare KPIs

The workbook contains more than six healthcare operational KPIs:

| # | KPI | Field | Aggregation |
|---|---|---|---|
| 1 | Total Patients | `patient_id` | COUNTD |
| 2 | Total Admissions | `patient_admission_flag` | COUNT |
| 3 | Average Length of Stay | `length_of_stay_days` | AVG |
| 4 | Occupancy Rate | `bed_occupancy_rate` | AVG |
| 5 | Readmission Rate | `is_readmitted` | AVG |
| 6 | Bed Utilization Rate | `bed_occupancy_rate` | AVG |
| 7 | Total Beds | `total_beds` | SUM |
| 8 | Occupied Beds | `occupied_beds` | SUM |
| 9 | Average Wait Time | `patient_waittime` | AVG |
| 10 | Patients Waiting >45 Min | `waittime_over_45min` | Patient count |
| 11 | Patient Satisfaction Score | `patient_satisfaction_score` | AVG |
| 12 | Department Efficiency Score | `department_efficiency_score` | AVG |

Full definitions are provided in [`KPI_DEFINITIONS.md`](KPI_DEFINITIONS.md).

---

# 7. Dashboards

The final Tableau workbook (`MedTrack_DV.twb`) contains four interconnected dashboards:

## 7.1 Hospital Overview

High-level summary of hospital performance and patient outcomes.

- KPI cards: Total Patients, Average LOS, Occupancy Rate, Readmission Rate, Satisfaction Score
- Charts: Admission Trends, Occupancy Rate Trend, Readmission Trend, Department Distribution, Age Group Distribution, Length of Stay

## 7.2 Patient Flow

Analysis of patient admissions, waiting time, admission status, admission shifts and length of stay.

- KPI cards: Total Patients, Average Wait Time, Patients Waiting >45 Min, Average LOS
- Charts: Patient Admissions Trend, Patient Admission Status, Patients by Wait Time Category, Average LOS by Department, Admission by Shift, Patient Flow Chart

## 7.3 Department Analytics

Comparison of operational performance across hospital departments.

- KPI cards: Admissions KPI, Average Wait Time, Average LOS, Readmission Rate, Department Efficiency Score
- Charts: Admissions by Department, Average Wait Time by Department, Readmission Rate by Department, Department Performance, Department Efficiency, Department Distribution

## 7.4 Resource Utilization

Hospital capacity, bed utilization, patient volume and department efficiency.

- KPI cards: Total Beds, Occupied Beds, Bed Utilization Rate, Average LOS, Average Wait Time
- Charts: Patient Volume by Department, Resource Utilization, Utilization Trend, Occupancy & Bed Utilization, Bed Occupancy by Department, Department Efficiency

Full worksheet-level detail is provided in [`DASHBOARD_GUIDE.md`](DASHBOARD_GUIDE.md).

---

# 8. Healthcare Operations Methodology

The project followed a nine-stage end-to-end methodology:

```text
Data Collection
       ↓
Data Cleaning
       ↓
Data Transformation
       ↓
KPI Engineering
       ↓
Tableau Data Preparation
       ↓
Dashboard Development
       ↓
Dashboard Integration
       ↓
Testing & Validation
       ↓
Documentation & Delivery
```

The complete methodology is documented in [`HEALTHCARE_OPERATIONS_METHODOLOGY.md`](HEALTHCARE_OPERATIONS_METHODOLOGY.md).

---

# 9. Modules Implemented

| Module | Name | Key Deliverables |
|---|---|---|
| Module 1 | Hospital Data Collection | `data_collection.py`, integrated healthcare dataset |
| Module 2 | Data Cleaning & Transformation | `data_cleaning_transformation.ipynb`, `cleaned_healthcare_patient_flow_data_enriched.csv` |
| Module 3 | Hospital KPI Engineering | `generate_hospital_kpis.py`, `hospital_final_dataset.xlsx` |
| Module 4 | Dashboard Planning & Prototyping | `dashboard_storyboard.pdf` |
| Module 5 | Hospital Overview & Patient Flow Dashboards | `medtrack_dashboard_v1.twb` |
| Module 6 | Department Analytics & Resource Utilization Dashboards | `MedTrack_DV.twb` |
| Module 7 | Testing & Validation | QA Checklist, Dashboard Testing Report |
| Module 8 | Documentation & Project Delivery | Final documentation, organized repository, Tableau workbook |

---

# 10. Project Structure

The repository is organized as follows:

```text
infosys-recovered/
│
├── Scripts/                  → /scripts — Python processing code
│   ├── data_collection.py
│   ├── data_cleaning_transformation.ipynb
│   └── generate_hospital_kpis.py
│
├── Module 1/                 → /data — raw collected data
│   └── healthcare_analytics_patient_flow_data.csv
│
├── Module 2/                 → /data — cleaned & enriched data
│   ├── cleaned_healthcare_patient_flow_data_enriched.csv
│   └── data_cleaning_transformation.pbix
│
├── Module 3/                 → /data — final KPI dataset
│   └── hospital_final_dataset.xlsx
│
├── Module 4/                 → /docs — planning artifacts
│   └── dashboard_storyboard.pdf
│
├── Module 5/                 → /dashboard — development workbooks
│   └── medtrack_dashboard_v1.twb
│
├── Module 6/                 → /dashboard — development workbooks
│   └── MedTrack_DV.twb
│
├── Dashboard/                → /dashboard — final deliverable
│   ├── MedTrack_DV.twb
│   └── medtrack_dashboards.pbix
│
├── Module 7/                 → /dashboard — validated final workbook
│   ├── MedTrack_DV.twb
│   └── medtrack_dashboards.pbix
│
├── Module 8/                 → /docs — final documentation package
│   └── MODULE_8_DELIVERY_SUMMARY.md
│
├── Documents/                → /docs — project documentation
│   ├── README.md references
│   ├── DATASET_SOURCES.md
│   ├── KPI_DEFINITIONS.md
│   ├── DASHBOARD_GUIDE.md
│   ├── HEALTHCARE_OPERATIONS_METHODOLOGY.md
│   └── FINAL_PROJECT_DOCUMENTATION.md
```

This maps to the required Module 8 structure (`/scripts`, `/data`, `/dashboard`, `/docs`) while preserving the module-based history of the project.

---

# 11. Tech Stack

| Area | Tools / Libraries |
|---|---|
| Data Collection | Python, Hospital Dataset, Patient Admission Dataset |
| Data Processing | Pandas, NumPy |
| Data Cleaning | Python |
| Visualization | Tableau Desktop / Tableau Public |
| Dashboard Integration | Tableau Filters, Parameters, Actions |
| Documentation | Markdown, GitHub |

---

# 12. Milestones and Timeline

| Milestone | Weeks | Modules | Focus |
|---|---|---|---|
| Milestone 1 | Weeks 1–2 | Module 1, Module 2 | Data Collection & Cleaning |
| Milestone 2 | Weeks 3–4 | Module 3, Module 4 | KPI Engineering & Dashboard Planning |
| Milestone 3 | Weeks 5–6 | Module 5, Module 6 | Dashboard Development & Integration |
| Milestone 4 | Weeks 7–8 | Module 7, Module 8 | Testing and Delivery |

---

# 13. Deployment

## GitHub Repository

The complete project — scripts, datasets, dashboards and documentation — is delivered through the GitHub repository:

`Hospital-Operations-and-Patient-Analytics-Dashboard-Group-2`

The repository contains the organized project structure, all module deliverables and the final documentation set.

## Tableau Public (Optional)

The final workbook `MedTrack_DV` can also be published to Tableau Public to make the dashboards viewable online without Tableau Desktop.

To publish:

1. Open `Dashboard/MedTrack_DV.twb` in Tableau Desktop.
2. Ensure the data source path resolves to the enriched CSV.
3. Save as `.twbx` (packaged workbook) to embed the data extract.
4. Use **Server → Tableau Public → Save to Tableau Public**.

---

# 14. Evaluation Criteria

| Milestone | Focus Area | Metric | Target | Result |
|---|---|---|---|---|
| 1 | Data Collection & Cleaning | Dataset Completeness | >95% Complete | Met |
| 2 | KPI Engineering | KPI Accuracy | >95% | Met |
| 3 | Dashboard Development | Dashboard Functionality | 6+ KPIs, 4 Dashboards Integrated | Met |
| 4 | Documentation & Delivery | Project Quality | Portfolio Ready | Met |

---

# 15. Project Outcomes

- Collection and integration of hospital datasets.
- Data cleaning and transformation for healthcare operations analytics.
- Development of hospital performance KPIs.
- Creation of four interactive Tableau dashboards.
- Patient flow and admission analysis.
- Department efficiency monitoring.
- Resource utilization tracking.
- Single Tableau workbook as final deliverable.
- Fully documented, portfolio-ready project.

---

# 16. How to Use This Project

1. Clone or download the repository.
2. Run `Scripts/data_collection.py` to reproduce the raw integrated dataset.
3. Run `Scripts/data_cleaning_transformation.ipynb` to clean and enrich the data.
4. Run `Scripts/generate_hospital_kpis.py` to generate KPI fields and `hospital_final_dataset.xlsx`.
5. Open `Dashboard/MedTrack_DV.twb` in Tableau Desktop / Tableau Public.
6. Explore the four dashboards: Hospital Overview → Patient Flow → Department Analytics → Resource Utilization.

---

# 17. Conclusion

MedTrack_DV demonstrates an end-to-end healthcare operations analytics workflow — from raw hospital data collection through cleaning, KPI engineering, dashboard development, integration, testing, and documentation.

The delivered Tableau workbook provides an integrated, interactive view of hospital performance, patient flow, department efficiency and resource utilization, enabling data-driven operational decision-making.

The project is fully documented and portfolio-ready.
