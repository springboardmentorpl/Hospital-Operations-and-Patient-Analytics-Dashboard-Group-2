# Hospital-Operations-and-Patient-Analytics-Dashboard-Group-2

Hospital Operations & Patient Analytics Dashboard

Project Track: Data Visualization / Data Analytics
Program: Infosys Springboard Virtual Internship 7.0 – Batch 2
Project: Hospital Operations & Patient Analytics
Primary Tool: Power BI
Supporting Tools: Power Query, DAX, Excel/CSV

1. Project Overview

The Hospital Operations & Patient Analytics Dashboard is an interactive Business Intelligence solution developed to transform hospital patient and operational data into meaningful insights.

The dashboard provides management with a consolidated view of:

Patient volume and admissions

Patient journey and outcomes

Service demand and performance

Bed/resource utilization

Patient satisfaction

Staff/resource performance

Cost and financial indicators

Infosys describes its Springboard Virtual Internship as a project-based learning experience designed to provide practical exposure, guided learning and industry-oriented skills. The current Infosys ESG report describes the Virtual Internship Program as an 8-week program with project work and mentorship.
Source: Infosys

2. Problem Statement

Hospitals generate large amounts of patient and operational data. When this information is stored as raw tabular data, management may find it difficult to quickly understand patient flow, service demand, resource utilization and performance.

The project addresses the following problems:

Lack of centralized visibility into hospital performance.

Difficulty monitoring patient admissions and patient flow.

Limited visibility into service-level demand and performance.

Difficulty tracking operational resources such as beds.

Difficulty analyzing patient satisfaction.

Difficulty identifying trends across time and departments.

Dependence on manual/static reporting.

Business Questions

How many patients are being handled?

What are the admission trends?

Which departments/services have higher demand?

What are the major patient conditions?

What is the average length of stay?

How is patient satisfaction performing?

How efficiently are resources being utilized?

Which services or operational areas require attention?

3. Proposed Solution

The proposed solution is an interactive Power BI Hospital Operations & Patient Analytics Dashboard.

The end-to-end workflow is:

Raw Hospital Data
        ↓
Data Understanding
        ↓
Data Cleaning
        ↓
Data Transformation
        ↓
Data Modeling
        ↓
DAX Measures & KPIs
        ↓
Interactive Visualizations
        ↓
Dashboard Pages
        ↓
Business Insights
        ↓
Management Decision Support

The solution converts raw hospital records into KPI cards, trends, comparisons, distributions and scorecards.

4. Project Objectives

Build a centralized hospital analytics dashboard.

Monitor patient volume and admissions.

Analyze patient conditions and outcomes.

Understand service demand and performance.

Monitor operational KPIs.

Analyze patient satisfaction.

Track resource utilization.

Provide interactive filtering.

Reduce dependency on manual reporting.

Support data-driven hospital management decisions.

5. Dataset

The working hospital dataset used during the project contains approximately:

984 patient records

15 columns

The data contains patient/service-related attributes such as:

Patient demographics

Condition

Service

Medication

Admission/discharge information

Patient outcome

Length of stay

Satisfaction

Cost/payment-related information

Operational indicators

Update the dataset size above if your final submitted dataset differs from the working dataset.

6. Complete Project Workflow

Phase 1 – Problem Understanding

The hospital business requirement was analyzed first. The main objective was to convert operational and patient information into an interactive dashboard that management could use for monitoring and analysis.

Phase 2 – Data Collection

The hospital data was collected in structured tabular format and reviewed for:

Number of records and columns

Data types

Categorical fields

Numerical fields

Date fields

Missing values

Duplicate records

Inconsistent values

Phase 3 – Data Cleaning

The data was prepared before visualization by:

Checking missing values

Checking duplicates

Correcting data types

Standardizing categorical values

Formatting dates

Removing unnecessary fields

Creating required analytical fields

Validating numerical values

Phase 4 – Data Transformation

Power Query was used to prepare analysis-ready data.

Import Data
   ↓
Profile Columns
   ↓
Clean Data
   ↓
Change Data Types
   ↓
Standardize Fields
   ↓
Create Required Columns
   ↓
Load Prepared Data

Phase 5 – Data Modeling

The prepared data was structured to support analysis across dimensions such as:

Time

Department

Service

Condition

Gender

Outcome

Insurance/payment

Operational indicators

Phase 6 – KPI & DAX Development

Measures were created for important business metrics such as patient count, average length of stay, satisfaction, admission conversion and cost.

Phase 7 – Dashboard Development

Power BI visuals were organized into four analytical sections.

Phase 8 – Testing & Validation

Dashboard filters, KPIs and visual interactions were checked to ensure that the displayed results respond correctly to selections.

Phase 9 – Documentation & Presentation

The final dashboard, blueprint, presentation and project documentation were prepared to communicate the solution and business value.

7. Dashboard Structure

The project is organized into four major analytical areas.

Page 1 – Hospital Patient Analytics

Purpose

Provides an overall view of patient activity and hospital performance.

Filters

Admission Date

Department

Condition

Gender

Insurance

KPIs

Total Patients

Admissions

Average Length of Stay

Bed Utilization

Patient Satisfaction

Visuals

Patient Admissions Trend

Patient Distribution by Department

Condition / Diagnosis Mix

Operational Performance Scorecard

Page 2 – Service Performance

Purpose

Analyzes demand and performance across hospital services.

Filters

Month / Year

Service

Department

Patient Type

Outcome

KPIs

Total Requests

Admitted

Refused

Average Wait Time

Service Satisfaction

Visuals

Service Demand Trend

Admission Conversion by Service

Service Performance / Outcome

Service Scorecard

Page 3 – Staff Management

Purpose

Provides visibility into workforce utilization and staff performance.

Filters

Month / Year

Department

Staff Role

Shift

Service

KPIs

Total Staff

Average Attendance

Staff Utilization

Average Workload

Staff Satisfaction

Visuals

Staff Attendance Trend

Staff Distribution by Department

Workload vs Satisfaction

Staff Performance Scorecard

Page 4 – Financial Overview

Purpose

Provides a high-level view of hospital revenue, costs and financial indicators.

Filters

Year

Department

Service

Insurance

Payment Status

KPIs

Total Revenue

Total Cost

Average Patient Cost

Insurance Claims

Profit / Margin

Visuals

Revenue Trend

Revenue by Department / Service

Cost Distribution

Financial Performance Scorecard

8. Key Values / KPIs

KPI

Business Purpose

Total Patients

Measures patient volume

Admissions

Measures admitted patients

Average LOS

Measures average patient stay

Bed Utilization

Monitors resource utilization

Satisfaction

Measures patient experience

Total Requests

Measures service demand

Admitted

Measures successful admissions

Refused

Monitors refused requests

Average Cost

Monitors patient/service cost

Readmission

Helps monitor repeat visits

9. Visualization Techniques

Visual

Purpose

KPI Card

Quick performance summary

Line Chart

Time-based trends

Bar Chart

Department/service comparison

Donut Chart

Composition/share

Funnel Chart

Request-to-admission flow

Scatter Chart

Relationship between metrics

Matrix

KPI/service scorecard

Slicer

Interactive filtering

10. Key Features

Centralized Dashboard

Provides a single interface for hospital analytics.

KPI Monitoring

Important performance indicators are displayed prominently.

Patient Analytics

Analyzes patient volume, conditions, outcomes and satisfaction.

Service Analytics

Compares service demand and admission performance.

Staff Analytics

Provides visibility into attendance, workload and utilization.

Financial Analytics

Tracks revenue, cost and related financial indicators.

Interactive Slicers

Allows users to filter the dashboard by different business dimensions.

Trend Analysis

Line charts reveal changes over time.

Comparative Analysis

Bar charts support department and service comparisons.

Scorecards

Matrix visuals provide structured KPI monitoring.

Dashboard Navigation

Users can move between the four analytical pages.

11. Example Calculations

Total Patients

Total Patients = COUNT(Patient ID)

Average Length of Stay

Average LOS = AVERAGE(Length of Stay)

Average Satisfaction

Average Satisfaction = AVERAGE(Patient Satisfaction)

Admission Conversion Rate

Admission Conversion Rate =
Admitted Requests / Total Requests × 100

Average Patient Cost

Average Patient Cost =
Total Patient Cost / Total Patients

The exact DAX syntax should match the final field names in the Power BI model.

12. Technologies Used

Power BI

Used for dashboard development, visualization, KPI cards, filters, navigation and interactive reporting.

Power Query

Used for data cleaning, transformation and preparation.

DAX

Used for measures, KPIs, aggregations and business calculations.

Excel / CSV

Used as the structured source format for hospital data.

13. Business Insights Supported

The dashboard is designed to help identify:

Overall patient volume

Admission patterns

High-demand services

Patient condition distribution

Average length of stay

Resource utilization

Patient satisfaction

Service conversion performance

Staff workload/utilization

Revenue and cost patterns

Insurance/payment activity

Operational areas requiring attention

These insights can support resource allocation, staffing, service capacity planning, patient-flow monitoring and cost monitoring.

14. Expected Business Impact

The solution can help hospital stakeholders:

Reduce dependency on manual reporting.

Monitor important KPIs from one place.

Identify operational bottlenecks.

Understand patient demand.

Improve resource planning.

Compare department/service performance.

Monitor patient experience.

Support data-driven decisions.

15. Project Deliverables

Hospital Dataset
      ↓
Cleaned / Transformed Data
      ↓
Data Model
      ↓
DAX Measures
      ↓
Power BI Dashboard
      ↓
Dashboard Blueprint
      ↓
Project Presentation
      ↓
Project Documentation

16. Skills Demonstrated

Data Analytics

Business Intelligence

Power BI

Power Query

DAX

Data Cleaning

Data Transformation

Data Modeling

KPI Development

Data Visualization

Dashboard Design

Healthcare Analytics

Business Problem Solving

Analytical Thinking

Data-driven Decision Making

17. Internship Learning Outcomes

This project provided practical exposure to converting a business problem into an analytical solution.

Major learning outcomes include:

Understanding business requirements

Working with structured healthcare data

Cleaning and preparing data

Designing meaningful KPIs

Selecting suitable visualizations

Building interactive dashboards

Communicating insights through data

Applying a structured analytics workflow

Understanding how BI supports business decisions

Infosys states that Springboard's internship ecosystem is intended to help learners move from academic knowledge toward practical, industry-oriented readiness through project-based learning and mentorship.

18. Recommended Repository Structure

Hospital-Operations-Patient-Analytics/
│
├── README.md
│
├── Dataset/
│   └── hospital_patient_data.csv
│
├── PowerBI/
│   └── Hospital_Operations_Patient_Analytics.pbix
│
├── Documentation/
│   ├── Project_Report.pdf
│   └── Dashboard_Blueprint.pptx
│
├── Screenshots/
│   ├── hospital_patient_analytics.png
│   ├── service_performance.png
│   ├── staff_management.png
│   └── financial_overview.png
│
└── Presentation/
    └── Project_Presentation.pptx

19. Final Summary

The Hospital Operations & Patient Analytics Dashboard is a Power BI-based healthcare Business Intelligence solution that transforms hospital data into an interactive management dashboard.

The solution focuses on four major areas:

Hospital Patient Analytics
          ↓
Service Performance
          ↓
Staff Management
          ↓
Financial Overview

The project demonstrates an end-to-end analytics workflow covering problem understanding, data preparation, transformation, modeling, KPI development, visualization, dashboard design and business insight generation.

Acknowledgement

This project was developed as part of the Infosys Springboard Virtual Internship 7.0 – Batch 2.

The internship provided an opportunity to apply data analytics and visualization concepts to a hospital operations use case and develop an end-to-end Business Intelligence solution.

Keywords

Infosys Springboard Virtual Internship 7.0 Batch 2 Power BI Healthcare Analytics Hospital Analytics Data Analytics Business Intelligence Dashboard DAX Power Query Data Visualization Patient Analytics Hospital Operations KPI Data Cleaning Data Modeling
