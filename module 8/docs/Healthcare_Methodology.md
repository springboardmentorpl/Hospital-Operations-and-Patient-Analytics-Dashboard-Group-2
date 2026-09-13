# Healthcare Methodology

## Purpose and Analytical Boundary

This project applies descriptive analytics to hospital operations. It summarizes activity recorded in the cleaned dataset and presents patterns related to patient flow, department performance, capacity, staffing, and resource utilization.

The analysis does not diagnose patients, recommend treatment, predict individual outcomes, or establish clinical quality measures. The dashboards are intended for operational analysis and decision support.

## Unit of Analysis

The cleaned dataset is a row-level operational dataset containing hospital, department, patient, bed, equipment, staffing, and event-related attributes.

A row should not automatically be interpreted as one unique patient encounter. The same `Patient ID` may occur across departments or related operational records.

The following counting rules are used:

- Count unique patients using distinct `Patient ID`.
- Count hospitals using distinct `Hospital ID`.
- Count departments using `Department ID` together with hospital context when required.
- Count equipment using distinct `Equipment ID`.
- Treat patient, department, hospital, and equipment analyses as different data grains.
- Do not sum measures across different grains without checking for possible duplication.

## Data Preparation Concepts

The cleaned dataset standardizes dates, categorical values, and numeric fields and provides additional analysis fields.

The following derived fields support dashboard analysis:

- `Age Group`
- `Admission Month`
- `Admission Year`
- `LOS Category`
- `Dept_Bed_Capacity_Derived`
- `Dept_ICU_Bed_Capacity_Derived`
- `Staff_Utilization_%_Derived`

Capacity and utilization fields should be traced back to their preparation logic before being used for official reporting.

Missing transfer destinations can occur when `Transferred = No`. Transfer activity should be interpreted using the following fields together:

- `Transferred`
- `Transfer From Department`
- `Transfer To Department`
- `Transfer Date`
- `Number of Transfers`

## Denominators and Aggregation

Rates are meaningful only when their denominator, aggregation method, and scope are clearly defined.

The dashboard uses distinct patient counts for patient-level metrics where appropriate and averages prepared row-level percentages for some utilization metrics.

For example:

- Readmission Rate = readmitted patients / total patients
- Transferred Rate = transferred patients / total patients
- Equipment Utilization Rate = equipment marked `In Use` / total observed equipment
- Staff Utilization Rate = average of `Staff_Utilization_%_Derived`
- Bed Utilization Rate = average of `Bed_Occupancy_Rate_%`

When comparing hospitals or departments:

1. Apply the same time period and population filters.
2. Confirm that the denominator is comparable.
3. Review volume alongside the rate.
4. Investigate extreme values for missing data, small samples, or duplicated records.

## Length of Stay

Length of Stay (LOS) is calculated as the difference between the admission date and discharge date:

`Length of Stay = Discharge Date - Admission Date`

The result is measured in days and is grouped into the following categories:

- **Short Stay:** 0–30 days
- **Medium Stay:** 31–60 days
- **Long Stay:** 61–90 days
- **Extended Stay:** More than 90 days

Both admission and discharge dates should be valid before calculating LOS.

A discharge date earlier than the admission date should be treated as a data-quality issue.

Same-day stays should remain **0 days** when admission and discharge occur on the same date and should not be silently converted to one day.

## Readmission Analysis

Readmission analysis identifies patients whose `Readmission` value is marked as `Yes`.

The readmission rate is calculated as:

`Readmission Rate = Readmitted Patients / Total Patients × 100`

The dashboard uses patient-level counts for this metric. A high readmission rate should be treated as an operational signal requiring further investigation rather than as direct evidence of poor clinical quality.

## Patient Transfer Analysis

Patient transfer analysis uses the `Transferred` field and related transfer information.

The transfer rate is calculated as:

`Transferred Rate = Transferred Patients / Total Patients × 100`

Transfer counts should be reviewed together with the source department, destination department, transfer date, and number of transfers where available.

## Capacity and Utilization

Bed, ICU, staff, and equipment capacity are operational measures and should not be interpreted as direct measures of healthcare quality.

A high occupancy rate may reflect:

- High patient demand
- Delayed discharge
- Limited capacity
- Increased length of stay
- Timing differences in operational records

A low utilization rate may reflect:

- Lower patient demand
- Available excess capacity
- Planned readiness
- Operational scheduling
- Incomplete activity capture

Therefore, utilization should be interpreted together with admissions, discharges, length of stay, staffing, ICU capacity, and equipment status.

## Bed Utilization

The dashboard's Bed Utilization Rate is based on the average of the prepared `Bed_Occupancy_Rate_%` field.

The dashboard value is approximately:

**36.76%**

This should not be confused with the separate count-based calculation using `Bed Occupied = Yes`, which produces approximately **50.36%**.

These calculations use different methods and answer different operational questions.

## Staff Utilization

Staff Utilization Rate represents the average value of the prepared `Staff_Utilization_%_Derived` field.

The validated overall dashboard value is approximately:

**57.92%**

This measure should be interpreted together with patient volume, department workload, and available staffing capacity.

## Equipment Utilization

Equipment utilization is calculated using equipment status.

`Equipment Utilization Rate = Equipment marked "In Use" / Total Observed Equipment × 100`

The validated equipment utilization rate is:

**33.55%**

Equipment status categories include values such as:

- In Use
- Available
- Under Maintenance

Equipment utilization should therefore be interpreted together with equipment availability and maintenance status.

## Department Analysis

Department-level analysis compares:

- Patient volume
- Average Length of Stay
- Staff utilization
- Bed occupancy
- Test result distribution
- Transfer activity
- Department capacity

Department comparisons should use consistent filters and aggregation levels.

A department with high patient volume does not necessarily have poor performance. Volume should be considered together with capacity, staffing, length of stay, and utilization.

## Resource Utilization Score

The dashboard uses a composite efficiency/resource score based on:

- 40% Bed Utilization
- 40% Staff Utilization
- 20% Non-readmission performance

The formula is:

`Efficiency Score = (Bed Utilization × 0.40) + (Staff Utilization × 0.40) + ((1 - Readmission Rate) × 0.20)`

The validated overall score is approximately:

**47.90%**

This is a comparative operational metric and should not be interpreted as a clinical quality or patient-safety score.

## Data Quality Controls

Before analysis or publication, perform the following checks:

- Required identifiers are present and formatted consistently.
- Admission and discharge dates parse correctly.
- Discharge dates are not earlier than admission dates.
- Numeric fields contain valid numeric values.
- Numeric values fall within reasonable ranges.
- Yes/No fields use consistent spelling and capitalization.
- Categorical values use consistent labels.
- Derived percentages are within the expected 0–100% range.
- Distinct patient and hospital counts remain stable after data refresh.
- Transfer fields are consistent with the `Transferred` indicator.
- Length of Stay values are consistent with admission and discharge dates.
- Duplicate records are reviewed before patient-level calculations.

## Validation Methodology

Important dashboard KPIs were independently calculated using Python/Pandas and compared with the Tableau results.

The validation process included:

1. Loading the cleaned dataset.
2. Checking row counts and unique identifiers.
3. Recalculating major KPIs independently.
4. Validating Length of Stay using admission and discharge dates.
5. Comparing Python results with Tableau dashboard values.
6. Checking dashboard filters and interactions.
7. Recording the results in the QA checklist.

The dashboard testing resulted in:

- **40 test cases**
- **40 passed**
- **0 failed**
- **100% pass rate**
- **0 major issues**

## Privacy and Responsible Use

The dataset contains patient-related and healthcare attributes such as patient identifiers, diagnosis, treatment, medication, test results, and blood type.

Access to patient-related information should therefore be limited to authorized users.

For public dashboards and portfolio demonstrations:

- Prefer aggregated results.
- Avoid publishing identifiable patient-level information.
- Avoid displaying unnecessary personal or health-related attributes.
- Review small groups before sharing externally.
- Follow applicable privacy and data-protection requirements.
- Do not use the dashboard as the sole basis for clinical, staffing, or patient-level decisions.

This project is intended as an operational analytics and visualization project rather than a clinical decision-support system.

## Final Interpretation

The methodology focuses on consistent definitions, appropriate denominators, correct aggregation levels, independent KPI validation, and responsible interpretation of healthcare operational data.

Dashboard results should be interpreted within their filter context and supported by the underlying data rather than viewed as standalone indicators of hospital quality.