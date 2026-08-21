# Hospital Operations and Patient Analytics Dashboard - Group 2

## Project Overview

The Hospital Operations and Patient Analytics Dashboard project focuses on analyzing hospital operational and patient admission data to generate meaningful insights and support data-driven decision-making.

The project includes data collection, data preparation, data cleaning, transformation, KPI engineering, data analysis, and interactive dashboard development using Microsoft Power BI.

The final solution consists of four interconnected dashboard pages:

- Hospital Overview
- Patient Flow
- Department Analytics
- Resource Utilization


## Project Objectives

- Collect and prepare hospital operational and patient admission data
- Analyze patient admission patterns
- Examine department-related information
- Handle missing and inconsistent data
- Standardize healthcare-related data
- Transform raw data into an analysis-ready format
- Develop meaningful healthcare KPIs
- Create interactive Power BI dashboards
- Implement slicers, filters, and navigation
- Generate actionable insights from hospital data


# Milestone 1: Data Collection and Preparation

## Module 1: Hospital Data Collection

### Tasks

- Download publicly available hospital datasets
- Collect patient admission records
- Gather department-related information
- Gather healthcare operational data
- Prepare the collected datasets for analysis
- Validate the completeness and structure of the data


### Deliverables

- hospital_raw_data.csv
- data_collection.py


### Evaluation Criteria

- Successful dataset collection and preparation
- Dataset completeness above 95%
- Required fields available for healthcare analytics


## Module 2: Data Cleaning & Transformation

### Tasks

- Inspect the dataset structure
- Remove duplicate records
- Check and handle missing values
- Standardize department names
- Standardize categorical values
- Correct data types where required
- Transform healthcare-related indicators
- Prepare an analysis-ready dataset


### Deliverables

- hospital_cleaned.csv
- hospital_cleaning.ipynb


### Evaluation Criteria

- Clean and consistent dataset
- Missing values handled appropriately
- Consistent operational metrics
- Dataset ready for analysis and visualization


# Data Cleaning Process

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
Column and Data Type Standardization
        ↓
Department and Category Standardization
        ↓
Healthcare Indicator Transformation
        ↓
Final Data Validation
        ↓
Cleaned Dataset


# Milestone 2: KPI Engineering and Dashboard Development

## Module 3: Hospital KPI Engineering

### Tasks

Develop and calculate important hospital performance indicators, including:

- Total Admissions
- Average Length of Stay
- Readmission Rate
- Department Efficiency
- Occupancy-related metrics based on available data
- Bed Utilization metrics based on available data


### KPI Definitions

#### Total Admissions

Measures the total number of patient admission records.

Total Admissions
        =
Count of Admission Records


#### Average Length of Stay

Measures the average number of days patients stay in the hospital.

Average Length of Stay
        =
Average of Length of Stay Days


#### Readmission Rate

Measures the proportion of patients who are readmitted based on the available readmission information.


#### Department Efficiency

Used to compare the operational performance of hospital departments based on the developed efficiency measure.


#### Bed Utilization

Used to analyze hospital bed-related resource utilization based on the available dataset and calculation.


### Deliverables

- hospital_final_dataset.xlsx
- KPI measures and calculated fields
- Power BI data model


### Evaluation Criteria

- KPIs calculated correctly
- Measures respond to slicers and filters
- Dataset optimized for Power BI visualization


# Module 4: Dashboard Planning and Development

### Tasks

Design and develop four interactive Power BI dashboard pages:

- Hospital Overview
- Patient Flow
- Department Analytics
- Resource Utilization


Define and implement:

- KPI cards
- Charts and visualizations
- Slicers
- Filters
- Page navigation
- Visual interactions
- Department comparisons


### Deliverables

- dashboard_storyboard.pdf
- Hospital_Operations_Analytics.pbix


### Evaluation Criteria

- Dashboard layout completed
- Four dashboard pages developed
- Interactive functionality verified
- Filters and slicers working correctly


# Dashboard Development Process

Cleaned Dataset
        ↓
Data Import into Power BI
        ↓
Data Validation
        ↓
DAX Measure Creation
        ↓
KPI Development
        ↓
Chart Selection
        ↓
Dashboard Design
        ↓
Slicer and Filter Integration
        ↓
Visual Interaction Configuration
        ↓
Page Navigation
        ↓
Dashboard Testing
        ↓
Final Power BI Report


# Dashboard 1: Hospital Overview

The Hospital Overview dashboard provides a high-level summary of overall hospital performance.

### Key Performance Indicators

- Total Admissions
- Department Efficiency
- Average Length of Stay
- Readmission Rate
- Occupancy-related metric
- Bed Utilization


### Analysis Areas

- Overall hospital admissions
- Admission type distribution
- Patient distribution by department
- Department efficiency comparison


### Interactive Features

- Department slicer
- Gender slicer
- Interactive KPI cards
- Cross-filtering between visuals
- Page navigation


# Dashboard 2: Patient Flow

The Patient Flow dashboard focuses on analyzing patient movement and admission patterns.

### Analysis Areas

- Total patient admissions
- Admission trends
- Patient length of stay
- Discharge-related analysis
- Readmission patterns
- Patient distribution


### Interactive Features

- Department-based filtering
- Gender-based filtering
- Time-based filtering where applicable
- Interactive charts and KPI cards


# Dashboard 3: Department Analytics

The Department Analytics dashboard focuses on comparing the performance and patient activity of different hospital departments.

### Analysis Areas

- Department-wise admissions
- Department efficiency
- Average length of stay by department
- Department comparison
- Patient distribution across departments
- Readmission-related trends


### Interactive Features

- Department slicer
- Gender slicer
- Interactive department comparison
- Dynamic KPI values
- Cross-filtering between charts


# Dashboard 4: Resource Utilization

The Resource Utilization dashboard focuses on analyzing patient load and healthcare resource-related patterns.

### Key Performance Indicators

- Total Admissions
- Average Length of Stay
- Department Efficiency
- Bed Utilization


### Analysis Areas

- Patient load by department
- Patient load versus average length of stay
- Department contribution to hospital load
- Average length of stay by admission type
- Resource demand patterns


### Interactive Features

- Department slicer
- Admission Type slicer
- Gender slicer
- Dynamic KPI cards
- Interactive visualizations


# Dashboard Structure

Hospital Operations and Patient Analytics Dashboard
                        │
        ┌───────────────┼───────────────┐
        │               │               │
        ↓               ↓               ↓
Hospital Overview    Patient Flow    Department Analytics
        │               │               │
        └───────────────┼───────────────┘
                        │
                        ↓
              Resource Utilization


# Dashboard Integration

The four dashboards are integrated into a single Power BI report.

Hospital Overview
        ↓
Navigation
        ↓
Patient Flow
        ↓
Navigation
        ↓
Department Analytics
        ↓
Navigation
        ↓
Resource Utilization


# Interactivity and Filtering

The Power BI dashboard includes interactive features that allow users to explore the data dynamically.

### Implemented Features

- Department slicers
- Gender slicers
- Admission Type slicers
- Time-based filtering where applicable
- Interactive KPI cards
- Cross-filtering between visuals
- Page navigation


The interaction process is represented as:

User Selects a Slicer
        ↓
Selected Value Creates Filter Context
        ↓
Connected Dataset is Filtered
        ↓
DAX Measures Recalculate
        ↓
KPI Cards Update
        ↓
Charts and Visuals Update


Example:

All Departments Selected
        ↓
Total Admissions = Overall Admissions

Pediatrics Selected
        ↓
Dataset Filtered to Pediatrics
        ↓
Total Admissions = Pediatrics Admissions

Gender Selected
        ↓
Relevant KPIs and Charts Update


# Milestone 3: Dashboard Integration and Testing

## Module 5: Dashboard Integration

### Tasks

- Integrate all dashboard pages into one Power BI report
- Configure page navigation
- Connect slicers and filters
- Configure visual interactions
- Ensure KPI cards respond to relevant filters
- Maintain consistent dashboard design


### Deliverables

- Integrated Power BI report
- Interactive dashboard navigation


## Module 6: Testing and Validation

### Tasks

- Test KPI calculations
- Test slicer functionality
- Test chart interactions
- Test page navigation
- Verify DAX measures
- Validate dashboard results against the dataset
- Identify and correct visualization issues


### Evaluation Criteria

- KPI calculations are correct
- Slicers filter connected visuals
- KPI cards respond to filter selections
- Navigation works correctly
- Dashboard pages function as expected


# Problems Faced and Solutions

## Problem 1: KPI Cards Did Not Respond to Slicers

Initially, some KPI cards displayed values that did not change when users selected a department or other slicer values.

### Cause

The cards were initially connected to fields or values that were not properly responding to the filter context of the main dataset.

### Solution

The existing Power BI measures were identified and used in the card visuals. The card values were connected to appropriate measures based on the main dataset.

Slicer Selection
        ↓
Dataset Filter
        ↓
DAX Measure Recalculation
        ↓
Updated KPI Card


## Problem 2: Visual Interactions

Some charts or KPI cards initially did not respond correctly to slicer selections.

### Solution

Visual interactions were checked and configured so that slicers could filter the appropriate visuals.

Select Slicer
        ↓
Configure Edit Interactions
        ↓
Enable Filter Interaction
        ↓
Connected Visual Updates


## Problem 3: Duplicate Measure Name

While creating a measure for Total Admissions, Power BI indicated that a measure with the same name already existed.

### Solution

The existing measure was identified and reused instead of creating an unnecessary duplicate measure.


## Problem 4: Resource-Related KPI Limitations

Some real-world healthcare KPIs require additional data, such as total available bed capacity.

### Solution

The analysis was limited to metrics that could be meaningfully calculated from the available dataset. Resource-related metrics were interpreted based on the fields and calculations available in the project dataset.


# Testing Workflow

Power BI Dashboard
        ↓
KPI Validation
        ↓
Slicer Testing
        ↓
Visual Interaction Testing
        ↓
Navigation Testing
        ↓
Result Verification
        ↓
Issue Identification
        ↓
Correction
        ↓
Final Validation


# Final Project Workflow

Hospital Dataset Collection
        ↓
Data Cleaning and Transformation
        ↓
Healthcare KPI Engineering
        ↓
Power BI Dashboard Development
        ↓
Dashboard Integration
        ↓
Testing and Validation
        ↓
Documentation
        ↓
Final Project Delivery


# Tools and Technologies

- Python
- Pandas
- Jupyter Notebook
- Microsoft Power BI
- Power Query
- DAX
- Microsoft Excel
- GitHub


# Project Structure

Hospital-Operations-and-Patient-Analytics/
│
├── data/
│   ├── hospital_raw_data.csv
│   ├── hospital_cleaned.csv
│   └── hospital_final_dataset.xlsx
│
├── notebooks/
│   └── hospital_cleaning.ipynb
│
├── scripts/
│   └── data_collection.py
│
├── powerbi/
│   └── Hospital_Operations_Analytics.pbix
│
├── dashboard/
│   └── dashboard_storyboard.pdf
│
├── images/
│   ├── hospital_overview.png
│   ├── patient_flow.png
│   ├── department_analytics.png
│   └── resource_utilization.png
│
└── README.md


# Project Outcome

The final project delivers a unified and interactive Power BI Hospital Operations and Patient Analytics Dashboard consisting of four analytical pages:

1. Hospital Overview
2. Patient Flow
3. Department Analytics
4. Resource Utilization

The project transforms raw hospital and patient admission data into meaningful KPIs and interactive visualizations.

Users can explore hospital performance through filters, slicers, interactive charts, and dynamic KPI cards.

The dashboard supports analysis of patient admissions, patient flow, department performance, length of stay, and healthcare resource utilization.


# Future Enhancements

- Real-time hospital data integration
- Predictive analysis for patient admissions
- Patient readmission prediction using machine learning
- Length of stay prediction
- Advanced bed occupancy analysis
- Resource demand forecasting
- Automated alerts for high patient load
- Integration with healthcare management systems


# Author

Pricilla G

B.Tech in Artificial Intelligence and Data Science

Group 2
