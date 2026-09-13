# KPI Definitions

The Tableau workbook uses the following key performance indicators (KPIs). Percentages are displayed as percentages in the dashboard, while ratio-based calculations are converted to percentage format where required.

| KPI | Definition | Interpretation |
| --- | --- | --- |
| Bed Occupancy Rate | Average of `Bed_Occupancy_Rate_%` from the cleaned source | Average proportion of department bed capacity occupied within the selected filter context. |
| Bed Utilization Rate | Average of `Bed_Occupancy_Rate_%` | Represents the average bed occupancy level across the selected records. |
| Staff Utilization Rate | Average of `Staff_Utilization_%_Derived` | Represents the average percentage of staff utilization in the selected scope. |
| Readmission Rate | Patients with `Readmission = Yes` divided by total patients | Proportion of patients marked as readmitted. |
| Efficiency Score | `(Bed Utilization Rate × 0.40) + (Staff Utilization Rate × 0.40) + ((1 − Readmission Rate) × 0.20)` | Composite operational efficiency measure based on bed utilization, staff utilization, and non-readmission performance. It is not a clinical quality score. |
| Resource Utilization Score | Same weighted structure as the Efficiency Score in the workbook | Composite measure representing overall resource and operational performance. |
| Patients Transferred | Patients where `Transferred = Yes` | Number of patients marked as transferred. |
| Transferred Rate | Patients transferred divided by total patients | Percentage of patients marked as transferred. |
| Average Daily Admissions | Total admissions divided by distinct `Admission Date` | Average number of admissions per admission date present in the selected data. |
| Average Daily Discharges | Total discharges divided by distinct `Discharge Date` | Average number of discharges per discharge date present in the selected data. |
| Equipment Utilization Rate | Equipment with `Equipment Status = In Use` divided by total observed equipment | Percentage of observed equipment currently marked as in use. |
| Average Department Bed Capacity | Average of `Dept_Bed_Capacity_Derived` | Average department-level bed capacity in the selected scope. |
| Length of Stay | `Discharge Date − Admission Date` in days | Number of days between admission and discharge. |
| Average Length of Stay | Average of `Length of Stay` | Average number of days patients stay in the hospital. |
| Total Revenue | Sum of `Billing Amount` | Total billing/revenue amount within the selected filter context. |
| Average Age | Average of `Age` | Average age of patients in the selected scope. |
| Total Departments | Count of distinct `Department` values | Number of departments represented in the selected data. |
| Average Doctors | Average number of doctors in the selected scope | Indicates the average doctor availability across the selected records. |
| Maximum Nurses | Maximum number of nurses in the selected scope | Highest recorded nurse count within the selected scope. |
| Average ICU Capacity | Average of `Dept_ICU_Bed_Capacity_Derived` | Average ICU bed capacity across the selected records. |

## Validated KPI Values

The following values were independently validated using Python/Pandas and compared with the Tableau dashboard:

| KPI | Validated Value |
| --- | ---: |
| Total Admissions | 10,000 |
| Total Revenue | ₹2.50 Billion |
| Average Length of Stay | 78.78 days |
| Average Age | 45.30 years |
| Readmission Rate | 49.87% |
| Bed Utilization Rate | 36.76% |
| Staff Utilization Rate | 57.92% |
| Patients Transferred | 1,760 |
| Transferred Rate | 17.60% |
| Average Daily Admissions | 19.05 |
| Equipment Utilization Rate | 33.55% |
| Average Department Bed Capacity | 491.69 |
| Average ICU Capacity | 98.70 |
| Efficiency Score | 47.90% |

## Efficiency Score Calculation

The Tableau Efficiency Score uses the following weighted formula:

`(Bed Utilization Rate × 0.40) + (Staff Utilization Rate × 0.40) + ((1 − Readmission Rate) × 0.20)`

Using the validated decimal values:

- Bed Utilization Rate = 0.36757
- Staff Utilization Rate = 0.57925
- Readmission Rate = 0.49870

Therefore:

`(0.36757 × 0.40) + (0.57925 × 0.40) + ((1 − 0.49870) × 0.20)`

`= 0.14703 + 0.23170 + 0.10026`

`= 0.47899`

Therefore, the final Efficiency Score is approximately:

**47.90%**

## Reading the KPIs

- Always record the active filters when reporting a KPI.
- Compare like-for-like scopes. Hospital, department, and time period should be consistent.
- Use distinct patients when calculating patient-level metrics where appropriate.
- Check the aggregation level before comparing KPI values.
- Do not interpret a high or low composite score as proof of clinical quality.
- Investigate the individual component KPIs and underlying records before making operational conclusions.

## KPI Caveats

The workbook uses averages of row-level derived percentages for several utilization metrics. Therefore, the result may differ from a ratio calculated using total occupied beds divided by total bed capacity.

For example, the dashboard's **36.76% Bed Utilization Rate** represents the average of the `Bed_Occupancy_Rate_%` field. A different calculation based on `Bed Occupied = Yes` produces **50.36%**.

These calculations answer different questions. For official reporting, the denominator, aggregation method, and reporting level should be agreed upon with the data owner.

The dashboard value of approximately **492 beds** represents `Dept_Bed_Capacity_Derived`. Therefore, the recommended KPI label is **Average Department Bed Capacity**, rather than simply Average Available Beds.