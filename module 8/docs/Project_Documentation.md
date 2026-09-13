# Hospital Operations and Patient Analysis

## 1. Project Overview

This project provides a Tableau dashboard suite for exploring hospital operations, patient flow, department performance, and resource utilization.

The project is designed for operational analysis rather than clinical decision-making. It allows users to compare hospitals and departments, identify capacity and utilization patterns, and examine patient, staffing, equipment, and financial information.

## 2. Repository Structure

| Location | Purpose |
| --- | --- |
| `data/Hospital_RawDataset_Updated.csv` | Raw input dataset |
| `data/hospital_cleaned.csv` | Cleaned and enriched Tableau source |
| `scripts/` | Data preparation, cleaning, and validation scripts |
| `docs/` | Project documentation and validation material |
| `dashboard/Hospital Operations and Patient Analysis.twb` | Tableau workbook |

The cleaned dataset contains **53 columns**. In addition to source attributes, it includes derived fields for age groups, admission month and year, length-of-stay categories, bed occupancy, staffing utilization, admissions, and department capacity.

## 3. Objectives

The main objectives of the project are:

- Monitor bed, ICU, staff, and equipment capacity.
- Compare operational performance across hospitals, states, cities, and departments.
- Understand admissions, discharges, transfers, length of stay, and readmissions.
- Analyze department-level patient volume and resource utilization.
- Identify operational patterns that may require further investigation.
- Support evidence-based operational analysis through filters and dashboard actions.
- Present healthcare data through interactive and easy-to-understand Tableau dashboards.

## 4. Dashboard Scope

### Hospital Overview

Provides a high-level view of hospital activity and operational performance.

Key areas include:

- Total admissions
- Total revenue
- Average length of stay
- Readmission rate
- Efficiency score
- Department count
- Monthly admission trends
- Revenue trends
- Admissions by state
- Insurance analysis

### Department Analysis

Supports department-level comparison of:

- Patient volume
- Department capacity
- Staff utilization
- Bed occupancy
- Average length of stay
- Test result distribution
- Transfer activity

It is the primary dashboard for identifying departments that may require operational review.

### Patient Flow

Shows patient movement and admission-related patterns, including:

- Admissions
- Discharges
- Transfers
- Admission types
- Age groups
- Length-of-stay categories
- Daily admission patterns

It helps users understand patient demand, movement, and hospital stay patterns.

### Resource Utilization

Focuses on the utilization of:

- Hospital beds
- Staff
- ICU capacity
- Equipment

It also presents resource utilization and efficiency measures for comparative operational monitoring.

## 5. Data Flow

The project follows the following data flow:

1. The raw CSV dataset is collected and stored in the `data/` folder.
2. The raw data is cleaned and validated using Python/Pandas.
3. Additional analytical fields are created during the data-preparation process.
4. The cleaned CSV is loaded into Tableau as a text data source.
5. Tableau worksheets aggregate the records into dashboard-level views.
6. Dashboard filters, parameters, and actions allow users to interact with the visualizations.
7. KPI results are independently validated using Python/Pandas.

The workbook uses a local connection to `hospital_cleaned.csv`. When moving the project to another machine, update the Tableau data-source path before refreshing or publishing the workbook.

## 6. Technology Stack

| Technology | Purpose |
| --- | --- |
| Python | Data collection, cleaning, and validation |
| Pandas | Data manipulation and KPI validation |
| NumPy | Numerical calculations |
| Tableau Desktop | Dashboard development and visualization |
| Tableau Public | Optional dashboard publishing |
| GitHub | Project version control and documentation |
| Markdown | Project documentation |

## 7. Key Validated Results

The following major results were independently calculated and validated:

| KPI | Value |
| --- | ---: |
| Total Admissions | 10,000 |
| Total Revenue | ₹2.50 Billion |
| Average Length of Stay | 78.78 days |
| Average Age | 45.30 years |
| Readmission Rate | 49.87% |
| Bed Utilization Rate | 36.76% |
| Staff Utilization Rate | 57.92% |
| Patients Transferred | 1,760 |
| Transfer Rate | 17.60% |
| Average Daily Admissions | 19.05 |
| Equipment Utilization Rate | 33.55% |
| Average Department Bed Capacity | 491.69 |
| Average ICU Capacity | 98.70 |
| Efficiency Score | 47.90% |

## 8. Efficiency Score

The project uses a composite Efficiency Score to provide a comparative view of operational performance.

The formula is:

`Efficiency Score = (Bed Utilization × 0.40) + (Staff Utilization × 0.40) + ((1 - Readmission Rate) × 0.20)`

The validated overall score is approximately:

**47.90%**

The score is an operational comparison metric and should not be interpreted as a clinical quality or patient-safety score.

## 9. Data Validation

The cleaned dataset and dashboard KPIs were validated using Python/Pandas.

Validation included:

- Dataset row and column count checks
- Duplicate identifier checks
- Missing-value checks
- Date validation
- Length of Stay recalculation
- Patient count validation
- Revenue validation
- Readmission rate validation
- Transfer rate validation
- Bed utilization validation
- Staff utilization validation
- Equipment utilization validation
- Efficiency score validation

The calculated Length of Stay was independently compared with the dataset value and matched successfully.

## 10. Dashboard Testing

The completed Tableau dashboards were tested using a structured QA checklist.

| Testing Metric | Result |
| --- | ---: |
| Total Test Cases | 40 |
| Passed | 40 |
| Failed | 0 |
| Pass Rate | 100% |
| Major Issues | 0 |
| Tested KPI Validation | 100% |

Testing covered:

- KPI accuracy
- Chart calculations
- Filters
- Dashboard navigation
- Cross-filtering
- Dashboard actions
- Tooltips
- Layout
- Data quality
- KPI formatting

## 11. Important Metric Notes

### Bed Utilization

The dashboard's Bed Utilization Rate of **36.76%** represents the average of the prepared `Bed_Occupancy_Rate_%` field.

A separate count-based calculation using `Bed Occupied = Yes` produces approximately **50.36%**.

These values use different calculation methods and should not be treated as interchangeable.

### Department Bed Capacity

The dashboard value of approximately **492 beds** represents the average of `Dept_Bed_Capacity_Derived`.

Therefore, the recommended KPI label is:

**Average Department Bed Capacity**

rather than simply Average Available Beds.

## 12. Key Operational Findings

The analysis provides several operational insights:

- The hospital recorded **10,000 admissions** in the analyzed dataset.
- The average Length of Stay was approximately **78.78 days**, indicating a substantial proportion of extended stays.
- The overall readmission rate was **49.87%**.
- Staff utilization averaged approximately **57.92%**.
- Bed utilization averaged approximately **36.76%** based on the prepared occupancy-rate field.
- Equipment utilization was approximately **33.55%**.
- Approximately **17.60%** of patients were marked as transferred.
- Oncology recorded the highest average Length of Stay among the departments.
- ICU recorded the highest staff utilization among the departments.
- Psychiatry recorded the highest average bed occupancy among the departments.

These findings are descriptive and should be investigated further using appropriate operational and clinical context.

## 13. Intended Users

The dashboard can be used by:

- Hospital operations analysts
- Department managers
- Capacity planners
- Resource planning teams
- Data analysts
- Project reviewers

The results should be interpreted with local operational context and should not replace clinical judgment, staffing policies, financial controls, or official hospital reporting systems.

## 14. Limitations

- The dataset is an analytical extract and not a live hospital information system.
- Several capacity and utilization fields are derived values and should be validated against source-system definitions before production use.
- Daily admissions and daily discharges are calculated using patient counts divided by distinct dates present in the dataset. They do not represent a calendar-day census.
- A patient may appear in more than one department-related record.
- Patient-level counts should use distinct `Patient ID` where appropriate.
- Different data grains should not be combined without checking for duplication.
- The dashboard provides descriptive analysis and does not establish causation.
- Composite scores should not be interpreted as clinical quality measures.
- The dataset contains patient-related attributes, so access and publication must follow applicable privacy and organizational policies.

## 15. Maintenance Checklist

Before publishing or updating the project:

- Confirm the cleaned CSV path in Tableau.
- Check column names and data types after each refresh.
- Validate admission and discharge date ranges.
- Check duplicate identifiers.
- Check missing values.
- Validate transfer-related fields.
- Recalculate important KPIs using the validation scripts.
- Re-run the validation notebook before publishing an updated workbook.
- Re-test filters and dashboard actions.
- Check KPI formatting and percentage displays.
- Verify consistency across all four dashboards.
- Confirm that the final documentation matches the current workbook.
- Avoid publishing identifiable patient-level information.

## 16. Final Deliverables

The final project contains:

- Cleaned hospital dataset
- Data preparation and validation scripts
- Tableau workbook
- Four integrated dashboards
- KPI definitions
- Dashboard user guide
- Healthcare methodology documentation
- Dashboard testing and QA documentation
- GitHub project repository

## 17. Conclusion

The Hospital Operations and Patient Analysis project demonstrates how healthcare operational data can be cleaned, validated, analyzed, and transformed into an interactive Tableau dashboard suite.

The four dashboards provide complementary views of hospital performance:

**Hospital Overview → Patient Flow → Department Analysis → Resource Utilization**

Together, they provide a structured approach to understanding patient activity, department performance, capacity, staffing, and equipment utilization.

The project combines Python-based data preparation and validation with Tableau-based interactive visualization to support clear, evidence-based operational analysis.