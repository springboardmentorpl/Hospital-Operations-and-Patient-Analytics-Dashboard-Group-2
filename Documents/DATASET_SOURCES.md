# MedTrack_DV — Dataset Sources

## 1. Overview

MedTrack_DV is a healthcare operations and patient analytics dashboard suite developed using Tableau.

The Tableau workbook uses the following cleaned and enriched healthcare patient-flow dataset:

`cleaned_healthcare_patient_flow_data_enriched.csv`

This dataset is used across the four dashboards:

1. Hospital Overview
2. Patient Flow
3. Department Analytics
4. Resource Utilization

---

## 2. Dataset Purpose

The dataset supports analysis of:

- Patient admissions
- Patient flow
- Patient waiting time
- Length of stay
- Readmission
- Patient satisfaction
- Department performance
- Bed capacity
- Bed occupancy
- Resource utilization
- Department efficiency

---

## 3. Patient Information

| Field | Description |
|---|---|
| `patient_id` | Unique patient identifier |
| `patient_age` | Patient age |
| `patient_gender` | Patient gender |
| `patient_race` | Patient race/category |
| `age_group` | Grouped patient age category |

---

## 4. Admission Information

| Field | Description |
|---|---|
| `patient_admission_date` | Patient admission date |
| `patient_admission_time` | Patient admission time |
| `admission_status` | Patient admission status |
| `admission_shift` | Admission shift |
| `patient_admission_flag` | Admission indicator |
| `admission_year_month` | Monthly admission grouping |

---

## 5. Department Information

| Field | Description |
|---|---|
| `department_referral` | Department associated with the patient |
| `department_group` | Department grouping |

Departments represented in the Tableau workbook include:

- Cardiology
- Orthopedics
- Neurology
- Renal
- General Practice
- Physiotherapy
- Gastroenterology

---

## 6. Patient Flow Information

| Field | Description |
|---|---|
| `patient_waittime` | Patient waiting time |
| `waittime_category` | Waiting-time category |
| `waittime_over_45min` | Indicator for waiting over 45 minutes |
| `length_of_stay_days` | Patient length of stay |

---

## 7. Discharge Information

| Field | Description |
|---|---|
| `patient_discharge_date` | Patient discharge date |
| `discharge_year_month` | Discharge year-month |
| `discharge_month_name` | Discharge month name |

---

## 8. Patient Outcome Information

| Field | Description |
|---|---|
| `is_readmitted` | Readmission indicator |
| `readmission_status` | Readmission status |
| `patient_satisfaction_score` | Patient satisfaction score |

---

## 9. Resource Information

| Field | Description |
|---|---|
| `total_beds` | Total bed capacity |
| `occupied_beds` | Occupied beds |
| `bed_occupancy_rate` | Bed occupancy/utilization rate |

---

## 10. Department Analytics

The Tableau workbook uses:

`department_efficiency_score`

This field is used to compare operational efficiency between departments.

---

## 11. Data Preparation

The project data preparation process includes:

1. Collecting hospital operational data.
2. Collecting patient admission data.
3. Integrating healthcare datasets.
4. Removing duplicate records.
5. Handling missing patient data.
6. Standardizing department names.
7. Normalizing healthcare indicators.
8. Creating a Tableau-ready analytical dataset.

---

## 12. Tableau Data Flow

```text
Healthcare Dataset
        ↓
Data Cleaning
        ↓
Data Transformation
        ↓
Cleaned & Enriched Dataset
        ↓
Tableau Data Source
        ↓
KPI Engineering
        ↓
Four Tableau Dashboards