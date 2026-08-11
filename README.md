# Hospital Operations and Patient Analytics Dashboard - Group 2

##  Project Overview

The **Hospital Operations and Patient Analytics Dashboard** project focuses on analyzing hospital operational and patient-related data to generate meaningful insights and support data-driven decision-making.

The project includes data collection, data preparation, data cleaning, transformation, analysis, KPI development, and dashboard creation.

---

##  Project Objectives

- Collect and prepare hospital operational data
- Analyze patient admission records
- Examine department-related information
- Handle missing and inconsistent data
- Standardize healthcare-related data
- Normalize operational indicators
- Develop meaningful healthcare KPIs
- Create an interactive analytics dashboard
- Generate actionable insights from hospital data

---

#  Milestone 1: Data Collection and Preparation

## Module 1: Hospital Data Collection

### Tasks

- Download hospital operational datasets
- Collect patient admission records
- Gather department and resource-related information
- Prepare the collected healthcare dataset for analysis
- Validate the completeness and structure of the dataset

### Deliverables

- `hospital_raw_data.csv`
- `data_collection.py`

### Evaluation Criteria

- Successful dataset preparation/integration
- Dataset completeness above 95%

---

## Module 2: Data Cleaning & Transformation

### Tasks

- Remove duplicate records
- Handle missing patient data
- Standardize department names
- Standardize categorical values
- Normalize healthcare indicators
- Prepare analysis-ready datasets

### Deliverables

- `hospital_cleaned.csv`
- `hospital_cleaning.ipynb`

### Evaluation Criteria

- Less than 2% missing values
- Consistent operational metrics

---

#  Data Cleaning Process

The hospital dataset is processed through the following workflow:

```text
Raw Hospital Dataset
        ↓
Data Collection
        ↓
Dataset Inspection
        ↓
Data Quality Assessment
        ↓
Duplicate Record Check
        ↓
Missing Value Analysis
        ↓
Missing Data Handling
        ↓
Column Standardization
        ↓
Department Standardization
        ↓
Healthcare Indicator Normalization
        ↓
Final Data Validation
        ↓
Cleaned Dataset
