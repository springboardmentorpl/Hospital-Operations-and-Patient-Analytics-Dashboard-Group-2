# Hospital Operations and Patient Analytics Dashboard(Group2)
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
# Dataset

The project uses an integrated hospital healthcare dataset containing hospital operational, patient, admission, department, ward, bed, billing, disease, and staff-related information.

The dataset includes the following major tables and attributes:

- **Patients:** Patient ID, gender, date of birth, blood group, city, and contact information
- **Admissions:** Admission ID, admission date, discharge date, admission type, admission status, patient ID, department ID, ward ID, bed ID, and disease ID
- **Departments:** Department ID, department name, department type, floor number, and status
- **Wards:** Ward ID, ward name, ward type, total beds, and department ID
- **Beds:** Bed ID, bed number, bed status, and ward ID
- **Billing:** Bill ID, bill date, total amount, insurance-covered amount, patient-payable amount, payment status, payment mode, and admission ID
- **Staff Assignment:** Assignment ID, employee ID, ward ID, and shift
- **Employees:** Employee ID, employee name, and staff-related details
- **Diseases:** Disease ID, disease name, and disease category

The final integrated dataset contains approximately 45,000 records and 34 columns. The data was cleaned, transformed, integrated, and validated before being used for KPI calculation and dashboard development.

---

# Key Performance Indicators

The project includes healthcare operational KPIs to evaluate patient admissions, patient flow, department performance, financial performance, and resource utilization.

### Patient and Admission KPIs

- Total Admissions
- Total Patients
- Total Discharges
- Average Length of Stay
- Readmission Rate
- Emergency Admission Percentage
- Admissions by Admission Type
- Admissions by Department
- Admissions by Disease Category

### Financial KPIs

- Total Revenue
- Patient Payable Amount
- Insurance Covered Amount
- Revenue by Department
- Department-wise Charges
- Monthly Revenue

### Department Performance KPIs

- Department Efficiency Score
- Admissions by Department
- Discharges by Department
- Readmission Rate by Department
- Average Length of Stay by Department
- Department-wise Patient Charges

### Resource Utilization KPIs

- Total Beds
- Total Staff
- Total Wards
- Average Beds per Ward
- Bed Utilization Rate
- Staff Allocation by Department
- Beds by Department
- Beds by Ward Type
- Monthly Bed Utilization
- Discharges by Disease Category

--- 
## Project Workflow

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
```

---

# Technologies Used

### Data Processing
- Python
- Pandas
- NumPy

### Data Visualization
- Tableau
- Power BI

### Development and Documentation
- Jupyter Notebook
- MS Word and PDF
- Microsoft Excel
- GitHub

---,
# Modules

### Module 1 – Data Collection
Collection and preparation of the hospital dataset.

### Module 2 – Data Cleaning
Cleaning, preprocessing, handling data quality issues, and preparing the dataset for analysis.

### Module 3 – KPI Generation
Calculation and preparation of important hospital operational KPIs.

### Module 4 – Dashboard Storyboard
Planning the dashboard structure, KPIs, visualizations, and analytical story.

### Module 5 – First Dashboard Set
Development of:
- Hospital Overview
- Patient Flow

using Tableau and Power BI.

### Module 6 – Second Dashboard Set
Development of:
- Department Analysis
- Resource Utilization

using Tableau and Power BI.

### Module 7 – Testing and Validation
Dashboard testing, quality assurance, KPI validation, and final dashboard preparation.

### Module 8 – Documentation and Project Delivery
Final documentation, project organization, dashboard delivery, methodology, KPI definitions, dashboard guide, and GitHub deployment.

---

# Dashboard Guide

The project contains four interconnected dashboards developed using Tableau. Each dashboard focuses on a specific area of hospital operations and provides interactive filters, KPI cards, and visualizations for better decision-making.

## 1. Hospital Overview Dashboard

The Hospital Overview dashboard provides a high-level summary of hospital performance and admission activity.

### Purpose

This dashboard helps hospital administrators understand overall admission trends, hospital occupancy, readmission performance, bed utilization, and department efficiency.

### Filters

- Admission Month
- Admission Type
- Department Name
- Ward Type

### Key Performance Indicators

- Total Admissions
- Occupancy Rate
- Readmission Rate
- Bed Utilization Rate
- Department Efficiency

### Visualizations

- **Monthly Admission Trend:** Shows how admissions change over time.
- **Admissions by Admission Type:** Compares emergency, urgent, and other admission types.
- **Admissions by Ward Type:** Displays the distribution of admissions across different ward types.
- **Average Length of Stay by Department:** Compares the average duration of patient stays across departments.

---

## 2. Patient Flow Dashboard

The Patient Flow dashboard focuses on patient movement, admissions, discharges, and length of stay.

### Purpose

This dashboard helps users monitor patient volume, discharge activity, admission patterns, and patient flow across departments and disease categories.

### Filters

- Admission Date
- Admission Type
- Department Name
- Age Group
- Blood Group

### Key Performance Indicators

- Readmission Rate
- Total Discharges
- Total Patients
- Average Length of Stay
- Pre-Admission Rate

### Visualizations

- **Monthly Discharge Trend:** Shows the number of discharges over time.
- **Patients by Admission Type:** Compares patient counts based on admission type.
- **Patients by Department:** Displays the distribution of patients across departments.
- **Patients by Disease Category:** Shows patient distribution across major disease categories.
- **Admissions by Disease Name:** Presents disease-wise admission distribution using a donut chart.
- **Emergency Admission Percentage:** Highlights the proportion of emergency admissions.

---

## 3. Department Analytics Dashboard

The Department Analytics dashboard evaluates the performance, workload, and financial activity of individual hospital departments.

### Purpose

This dashboard helps hospital management compare departments, identify high-performing departments, analyze patient charges, and monitor readmission patterns.

### Filters

- Department Name
- Admission Type
- Admission Date
- Age Group
- Disease Category

### Key Performance Indicators

- Total Admissions
- Total Discharges
- Department Efficiency Score
- Readmission Rate
- Patient Payable Amount

### Visualizations

- **Admissions by Department:** Compares the number of admissions across departments.
- **Discharges by Department:** Shows the discharge workload handled by each department.
- **Department Efficiency Treemap:** Displays department efficiency scores using different-sized boxes.
- **Readmission Rate by Department:** Compares readmission rates across departments using a donut chart.
- **Department-wise Charges by Age Group:** Shows patient charges across departments, categorized by age group.

---

## 4. Resource Utilization Dashboard

The Resource Utilization dashboard focuses on hospital resources such as beds, wards, and staff allocation.

### Purpose

This dashboard helps hospital administrators understand resource availability, bed utilization, staff allocation, and resource distribution across departments and ward types.

### Filters

- Department Name
- Ward Type
- Admission Date
- Disease Category

### Key Performance Indicators

- Total Beds
- Total Staff
- Total Wards
- Average Beds per Ward
- Bed Utilization Rate

### Visualizations

- **Average Staff Allocation by Department:** Shows staff distribution across departments.
- **Total Beds by Department:** Compares the number of beds available in each department.
- **Beds by Ward Type:** Displays bed distribution across different ward types.
- **Discharges by Disease Category:** Shows discharge volume for each disease category.
- **Monthly Bed Utilization by Department:** Tracks bed utilization trends over time.
- **Resource Distribution Analysis:** Helps identify departments or ward types with higher or lower resource availability.

---

## Dashboard Interactivity

All dashboards include interactive features to support detailed analysis:

- Filters allow users to view specific departments, dates, admission types, and ward categories.
- KPI cards provide quick summaries of important healthcare metrics.
- Charts update dynamically based on selected filters.
- Dashboard navigation buttons allow users to move between the four dashboards.
- Visual comparisons help identify trends, performance gaps, and resource utilization patterns.
# Conclusion

The Hospital Operations and Patient Analysis Dashboard provides an integrated analytical view of hospital operations.

The project follows a complete data analytics workflow from data collection and cleaning to KPI generation, visualization, testing, documentation, and final project delivery.

---
## Project Structure

The project is organized into multiple modules covering data collection, data cleaning, KPI development, dashboard creation, and project documentation.

```text
Hospital-Operations-and-Patient-Analytics-Dashboard-Group-2/
│
├── Module 1/
│   ├── DataCollection.py
│   └── hospital_raw_data.xlsx
│
├── Module 2/
│   ├── Data Cleaning.ipynb
│   └── hospital_cleaned (1).csv
│
├── Module 3/
│   ├── Module_3.ipynb
│   └── hospital_final_dataset_with_kpis.xlsx
│
├── Module 4/
│   └── MedTrack_Module4.pdf
│
├── Module 5/
│   ├── Powerbi Dashboards/
│   │   └── Module5_Hospital_Dashboards.pbix
│   │
│   └── Tableau/
│       ├── Hospital Overview.png
│       └── Patient Flow.png
│
├── Module 6/
│   ├── Powerbi Dashboards/
│   │   └── Module6_Hospital_Dashboards.pbix
│   │
│   └── Tableau/
│       ├── Department Analytics.png
│       └── Resource Utilization.png
│
├── Module 7/
│   ├── Powerbi Dashboard/
│   │   └── Hospital Analytics and patients.pbix
│   │
│   └── Tableau Dashboard/
│       ├── .gitkeep
│       └── Tableau dashboard.twbx
│
├── Module 8/
│   ├── Dashboard/
│   │   ├── Powerbi/
│   │   │   ├── .gitkeep
│   │   │   └── Hospital Analytics and patients.pbix
│   │   │
│   │   └── Tableau/
│   │       ├── .gitkeep
│   │       └── Tableau dashboard.twbx
│   │
│   ├── Data/
│   │   ├── .gitkeep
│   │   ├── hospital_cleaned (1).csv
│   │   ├── hospital_final_dataset_with_kpis.xlsx
│   │   └── hospital_raw_data.xlsx
│   │
│   ├── Docs/
│   │   ├── .gitkeep
│   │   ├── Dashboard Guide.pdf
│   │   ├── Dataset Sources.pdf
│   │   ├── Healthcare operations methodology.pdf
│   │   ├── KPI Calculations.pdf
│   │   └── MedTrack_Final Document.pdf
│   │
│   └── Scripts/
│       ├── .gitkeep
│       ├── Data Cleaning.ipynb
│       └── Hospital_KPI's.ipynb
│
└── README.md
```

