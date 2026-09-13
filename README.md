# Hospital-Operations-and-Patient-Analytics-Dashboard-Group-2

## Project Overview

The **Hospital Operations and Patient Analysis Dashboard** is a data analytics and visualization project developed to analyze hospital operations, patient flow, department performance, and resource utilization.

The project transforms hospital data into interactive dashboards that help hospital management understand operational trends, identify areas requiring attention, and support data-driven decision-making.

This project was developed as part of the **Infosys Springboard Virtual Internship 7.0** in the **Data Analysis & Visualization** domain.

---

## Project Objectives

The main objectives of this project are:

- Analyze hospital admission and patient trends.
- Understand patient flow and transfers.
- Compare department-wise performance.
- Analyze hospital revenue and readmission patterns.
- Monitor bed and staff utilization.
- Analyze equipment usage and status.
- Develop interactive dashboards for hospital management.
- Present meaningful insights from healthcare operational data.

---

# Dashboard Suite

The project consists of four interactive dashboards developed using **Tableau and Power BI**.

---

## 1. Hospital Overview

The **Hospital Overview Dashboard** provides a high-level view of overall hospital operations.

### Key Analysis

- Total Admissions
- Total Revenue
- Average Length of Stay
- Readmission Rate
- Efficiency Score
- Monthly Admissions Trend
- Monthly Revenue Trend
- Department-wise Admissions
- Insurance Provider Distribution
- Readmission Trend

### Tableau Dashboard

![Hospital Overview](module%205/Tableau/Hospital%20Overview.png)

---

## 2. Patient Flow

The **Patient Flow Dashboard** focuses on patient movement and workflow throughout the hospital.

### Key Analysis

- Total Admissions
- Average Length of Stay
- Patients Transferred
- Transfer Rate
- Average Patient Age
- Patient Discharges
- Age Group Distribution
- Patient Transfers by Department
- Admission Type Distribution
- Length of Stay Distribution

### Tableau Dashboard

![Patient Flow](module%205/Tableau/Patient%20Flow.png)

---

## 3. Department Analysis

The **Department Analysis Dashboard** compares the performance of different hospital departments.

### Key Analysis

- Patient Volume by Department
- Revenue by Department
- Average Length of Stay
- Test Results by Department
- Staff Utilization
- Readmission Rate
- Department-wise performance comparison

### Tableau Dashboard

![Department Analysis](module%206/Tableau/Department%20Analysis.png)

---

## 4. Resource Utilization

The **Resource Utilization Dashboard** analyzes the utilization of hospital resources.

### Key Analysis

- Resource Utilization Score
- Bed Utilization Rate
- Staff Utilization Rate
- Available Beds
- Equipment Utilization Rate
- Equipment Usage
- Equipment Status
- ICU Capacity
- Department-wise Resource Utilization

### Tableau Dashboard

![Resource Utilization](module%206/Tableau/Resource%20Utilization.png)

---

# Dashboard Preview

The four dashboards provide a complete operational story:

| Dashboard | Main Focus |
|---|---|
| Hospital Overview | Overall hospital performance |
| Patient Flow | Patient movement and workflow |
| Department Analysis | Department performance |
| Resource Utilization | Hospital resource utilization |

---

# Dataset

The project uses hospital operational and patient-level data containing information related to:

- Hospital details
- Patient information
- Gender and age
- Admission and discharge dates
- Departments
- Diagnosis
- Treatment
- Medication
- Admission type
- Test results
- Billing amount
- Insurance provider
- Readmission
- Beds and ICU capacity
- Doctors and nurses
- Staff utilization
- Equipment
- Patient transfers
- Length of Stay

The dataset was cleaned and validated before being used for analysis and dashboard development.

---

# Key Performance Indicators

The project includes several important healthcare operational KPIs.

### Patient KPIs

- Total Admissions
- Unique Patients
- Average Patient Age
- Average Length of Stay
- Patient Transfer Rate
- Readmission Rate

### Financial KPIs

- Total Revenue
- Revenue by Department
- Monthly Revenue

### Resource KPIs

- Bed Utilization Rate
- Staff Utilization Rate
- Equipment Utilization Rate
- Available Beds
- Resource Utilization Score
- ICU Capacity
- Equipment Inventory

---

# Project Workflow

```text
Data Collection
      ↓
Data Cleaning
      ↓
Data Validation
      ↓
KPI Calculation
      ↓
Dashboard Development
      ↓
Dashboard Testing
      ↓
Documentation
      ↓
Final Project Delivery

Technologies Used
Data Processing
Python
Pandas
NumPy
Data Visualization
Tableau
Power BI
Development and Documentation
Jupyter Notebook
VS Code
Microsoft Excel
Git
GitHub
##Project Structure##
Hospital-Operations-and-Patient-Analytics-Dashboard-Group-2/
│
├── module 1/
│   └── Hospital_RawDataset_Updated.csv
│
├── module 2/
│   ├── data cleaning.ipynb
│   └── hospital_cleaned.csv
│
├── module 3/
│   ├── generate_hospital_kpis.py
│   └── hospital_final_dataset.xlsx
│
├── module 4/
│   └── Dashboard_Storyboard.pdf
│
├── module 5/
│   ├── Power BI/
│   └── Tableau/
│
├── module 6/
│   ├── Power BI/
│   └── Tableau/
│
├── module 7/
│   ├── Dashboard_Testing_Report_Updated.docx
│   ├── Hospital Operations and Patient Analysis.pbix
│   ├── Hospital Operations and Patient Analysis.twb
│   └── QA_Checklist_Updated.xlsx
│
└── module 8/
    ├── dashboard/
    │   └── Hospital Operations and Patient Analysis.twb
    │
    ├── data/
    │   ├── Hospital_RawDataset_Updated.csv
    │   └── hospital_cleaned.csv
    │
    ├── docs/
    │   ├── Dashboard Testing Report.docx
    │   ├── Dashboard_Guide.md
    │   ├── Healthcare_Methodology.md
    │   ├── KPI_Definitions.md
    │   └── Project_Documentation.md
    │
    └── scripts/
        ├── data Validation.ipynb
        └── data cleaning.ipynb
Modules
Module 1 – Data Collection

Collection and preparation of the hospital dataset.

Module 2 – Data Cleaning

Cleaning, preprocessing, handling data quality issues, and preparing the dataset for analysis.

Module 3 – KPI Generation

Calculation and preparation of important hospital operational KPIs.

Module 4 – Dashboard Storyboard

Planning the dashboard structure, KPIs, visualizations, and analytical story.

Module 5 – First Dashboard Set

Development of:

Hospital Overview
Patient Flow

using Tableau and Power BI.

Module 6 – Second Dashboard Set

Development of:

Department Analysis
Resource Utilization

using Tableau and Power BI.

Module 7 – Testing and Validation

Dashboard testing, quality assurance, KPI validation, and final dashboard preparation.

Module 8 – Documentation and Project Delivery

Final documentation, project organization, dashboard delivery, methodology, KPI definitions, dashboard guide, and GitHub deployment.

Testing and Validation

The project includes testing and validation activities to ensure:

KPI calculations are accurate.
Dashboard filters work correctly.
Visualizations display the expected data.
Dashboard interactions function correctly.
Data quality is maintained.
Dashboard outputs are consistent with the underlying dataset.

Detailed testing information is available in the Dashboard Testing Report and QA Checklist included in the repository.

Documentation

The project documentation includes:

Project Documentation – Overall project description and workflow.
KPI Definitions – Definitions and calculation logic for important KPIs.
Dashboard Guide – Instructions for understanding and using the dashboards.
Healthcare Operations Methodology – Analytical methodology used for hospital operations analysis.
Dashboard Testing Report – Testing and validation results.
Key Insights

The dashboards enable management to:

Monitor overall admission and revenue trends.
Identify departments with higher patient volumes.
Understand patient movement and transfer patterns.
Compare department performance.
Monitor readmission patterns.
Evaluate bed and staff utilization.
Analyze equipment usage and status.
Identify areas that may require operational attention.
Business Value

The dashboard suite provides a consolidated view of hospital operations and helps management move from raw data to meaningful operational insights.

It supports analysis of:

Patients → Departments → Resources → Overall Hospital Performance

This allows decision-makers to identify trends, compare operational performance, and better understand resource utilization.

Important Note

This project is designed for hospital operational and analytical purposes.

It is intended to support operational monitoring and data analysis and is not intended for clinical diagnosis, treatment recommendations, or medical decision-making.

Project Deliverables

The repository contains:

Raw dataset
Cleaned dataset
Data cleaning notebooks
Data validation notebooks
KPI generation script
Final dataset
Dashboard storyboard
Power BI dashboards
Tableau workbooks
Dashboard screenshots
Dashboard testing report
QA checklist
KPI definitions
Dashboard guide
Healthcare operations methodology
Project documentation
Internship

Infosys Springboard Virtual Internship 7.0

Domain: Data Analysis & Visualization

Conclusion

The Hospital Operations and Patient Analysis Dashboard provides an integrated analytical view of hospital operations.

The project follows a complete data analytics workflow from data collection and cleaning to KPI generation, visualization, testing, documentation, and final project delivery.

The four dashboards work together to tell a complete story:

Hospital Overview → Patient Flow → Department Analysis → Resource Utilization

This dashboard suite demonstrates the use of data analytics and visualization techniques to transform healthcare operational data into meaningful and actionable insights.
