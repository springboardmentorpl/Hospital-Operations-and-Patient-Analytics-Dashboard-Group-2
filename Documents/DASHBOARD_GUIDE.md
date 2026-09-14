# MedTrack_DV — Dashboard Guide

## 1. Overview

The MedTrack_DV Tableau workbook contains four integrated dashboards:

1. Hospital Overview
2. Patient Flow
3. Department Analytics
4. Resource Utilization

The dashboards provide different levels of healthcare operational analysis.

---

# 2. Hospital Overview

## Purpose

The Hospital Overview dashboard provides a high-level summary of hospital performance and patient outcomes.

## KPI Cards

- Total Patients
- Average LOS
- Occupancy Rate
- Readmission Rate
- Satisfaction Score

## Tableau Worksheets

- KPI - Total Patients
- KPI - Average LOS
- KPI – Occupancy Rate
- KPI - Readmission Rate
- KPI - Satisfaction Score
- Admission Trends Chart
- Occupancy Rate Trend
- Readmission Trend
- Department Distribution
- Age Group Distribution
- Length of Stay

## Analysis

### Admission Trends Chart

Shows admission activity over time.

### Occupancy Rate Trend

Shows changes in hospital occupancy over time.

### Readmission Trend

Shows changes in readmission over time.

### Department Distribution

Shows patient or admission distribution across departments.

### Age Group Distribution

Shows patient distribution across age groups.

### Length of Stay

Provides patient length-of-stay analysis.

---

# 3. Patient Flow

## Purpose

The Patient Flow dashboard analyzes patient admissions, waiting time, admission status, admission shifts and length of stay.

## KPI Cards

- Total Patients
- Average Wait Time
- Patients Waiting >45 Min
- Average LOS

## Tableau Worksheets

- KPI - Total Patients
- KPI 3 — Average Wait Time
- KPI 4 — Patients Waiting >45 Min
- KPI - Average LOS
- Patient Admissions Trend
- Patient Admission Status
- Patients by Wait Time Category
- Average LOS by Department
- Admission by shift
- Patient Flow chart

## Analysis

### Patient Admissions Trend

Shows patient admission volume over time.

### Patient Admission Status

Analyzes patients according to admission status.

### Patients by Wait Time Category

Groups patients according to waiting-time categories.

### Average LOS by Department

Compares average length of stay between departments.

### Admission by Shift

Analyzes admission volume by admission shift.

### Patient Flow Chart

Provides an overall view of patient movement and flow.

---

# 4. Department Analytics

## Purpose

The Department Analytics dashboard compares operational performance across hospital departments.

## KPI Cards

- KPI #2
- Average Wait Time
- Average LOS
- Readmission Rate
- Department Efficiency Score

## Tableau Worksheets

- KPI #2
- KPI 3 — Average Wait Time
- KPI - Average LOS
- KPI - Readmission Rate
- Department Efficiency Score
- Admissions by Department
- Average Wait Time by Department
- Readmission Rate by Department
- Department Performance
- Department Efficiency
- Department Distribution

## Departments

The workbook contains departments including:

- Cardiology
- Orthopedics
- Neurology
- Renal
- General Practice
- Physiotherapy
- Gastroenterology

## Analysis

### Admissions by Department

Compares patient or admission volume between departments.

### Average Wait Time by Department

Compares waiting time across departments.

### Readmission Rate by Department

Compares readmission levels between departments.

### Department Performance

Provides department-level performance comparison.

### Department Efficiency

Compares department efficiency scores.

### Department Distribution

Shows patient distribution across departments.

---

# 5. Resource Utilization

## Purpose

The Resource Utilization dashboard focuses on hospital capacity, bed utilization, patient volume and department efficiency.

## KPI Cards

- Total Beds
- Occupied Beds
- Bed Utilization Rate
- Average LOS
- Average Wait Time

## Tableau Worksheets

- KPI 1 — Total Beds
- KPI 2 — Occupied Beds
- KPI 5 — Bed Utilization Rate
- KPI - Average LOS
- KPI 3 — Average Wait Time
- Patient volume by department
- Resource Utilization chart
- Utilization trend
- Occupancy & bed utilization
- Bed occupancy by department
- Department Efficiency

## Analysis

### Patient Volume by Department

Shows patient volume across departments.

### Resource Utilization Chart

Provides an overview of hospital resource utilization.

### Utilization Trend

Shows utilization changes over time.

### Occupancy & Bed Utilization

Analyzes occupancy and bed utilization.

### Bed Occupancy by Department

Compares bed occupancy across departments.

### Department Efficiency

Compares department efficiency.

---

# 6. Dashboard Navigation

The workbook contains navigation elements connecting the four dashboard views.

Recommended analytical flow:

```text
Hospital Overview
       ↓
Patient Flow
       ↓
Department Analytics
       ↓
Resource Utilization