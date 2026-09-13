# Hospital Operations & Patient Analytics Dashboard

## 1. Project Overview

The Hospital Operations & Patient Analytics Dashboard is a Tableau-based data visualization project designed to analyze hospital operations, patient flow, department performance, and healthcare resource utilization.

The project provides four interconnected dashboards:

1. Hospital Overview
2. Patient Flow
3. Department Analysis
4. Resource Utilization

## 2. Project Objectives

- Analyze hospital operational performance.
- Understand patient admissions and patient flow.
- Analyze department and specialty performance.
- Analyze healthcare resource utilization.
- Provide interactive dashboards for data-driven insights.

## 3. Dataset

The project uses a hospital operations dataset containing 500 records and 21 columns.

Important fields include:

- Month
- Case_No
- DOB
- Nationality
- Gender
- DoctorLicense
- DoctorName
- Doctor Type
- Doctor Status
- CMI Value
- Specialty
- Insurance/Payer
- InsurancePlanName
- Payer Mix
- Case type
- LOS
- Severity
- Surgical Mix
- Discharge Time
- Discharge Before 12PM
- Revenue

## 4. Data Cleaning & Transformation

The dataset was cleaned and transformed using Python and Pandas.

The cleaning process included:

- Checking duplicate records.
- Checking missing values.
- Standardizing data types.
- Converting Month into a date format.
- Preparing the cleaned dataset for Tableau analysis.
- Creating a Tableau-ready cleaned dataset.

The final cleaned dataset contains 500 records and 21 columns.

## 5. KPI Development

The project includes the following key metrics:

- Total Cases: 500
- Total IP Admissions: 141
- IP Admission Rate: 28.20%
- Average LOS: 1.28
- Average IP LOS: 4.19
- Total Revenue: ₹8,523,364
- Average Revenue: ₹17,046.73

## 6. Dashboard Development

### 6.1 Hospital Overview

This dashboard provides an overall view of hospital operations.

It includes:

- Total Cases
- IP Admissions
- IP Admission Rate
- Average LOS
- Total Revenue
- Monthly Cases Trend
- Case Type Distribution
- Monthly Revenue Trend
- Discharge Before 12PM analysis

### 6.2 Patient Flow

This dashboard focuses on patient and admission patterns.

It includes:

- Total Cases
- Admissions
- Average IP LOS
- Average LOS
- Monthly Admissions
- Patient Type Distribution
- Average LOS by Month
- IP Admissions by Severity
- Patient Cases by Gender
- Average LOS by Case Type

### 6.3 Department Analysis

This dashboard analyzes hospital specialties and departmental performance.

It includes:

- Top Specialty by Cases
- Top Specialty by Revenue
- Average LOS by Specialty
- Revenue vs Cases by Specialty
- Case Type by Specialty
- Average CMI by Specialty

### 6.4 Resource Utilization

This dashboard focuses on doctors and healthcare resource utilization.

It includes:

- Active Doctors
- Inactive Doctors
- Total Cases
- Doctor Status
- Cases by Doctor Type
- Revenue by Doctor Type
- Doctors by Specialty
- Doctor Status by Doctor Type
- Average CMI by Doctor Type

## 7. Tools & Technologies

- Python
- Pandas
- Jupyter Notebook
- Microsoft Excel
- Tableau
- Git
- GitHub

## 8. Project Workflow

The project was completed through the following modules:

1. Data Collection
2. Data Cleaning & Transformation
3. KPI Engineering
4. Dashboard Planning & Prototyping
5. Dashboard Development
6. Dashboard Integration
7. Testing & Validation
8. Documentation & Delivery

## 9. Final Deliverables

### Data

- hospital_raw_data.csv
- hospital_cleaned.csv
- hospital_final_dataset.xlsx

### Scripts

- data_collection.py
- hospital_cleaning.ipynb
- generate_hospital_kpis.py

### Tableau Dashboards

- medtrack_prototype.twbx
- medtrack_dashboard_v1.twbx
- MedTrack_DV.twbx

### Documentation

- dashboard_storyboard.pdf
- QA_Checklist.pdf
- Dashboard_Testing_Report.pdf
- Project_Documentation.md

## 10. Conclusion

The Hospital Operations & Patient Analytics Dashboard provides a unified Tableau-based solution for analyzing hospital operations, patient flow, department performance, and resource utilization.

The final project combines data preparation, KPI development, visualization, dashboard integration, testing, and documentation into a complete data analytics workflow.