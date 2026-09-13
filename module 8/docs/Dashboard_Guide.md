# Dashboard Guide

## Opening the Workbook

1. Open `dashboard/Hospital Operations and Patient Analysis.twb` in Tableau Desktop.
2. If Tableau reports a missing file, use **Edit Connection** and select `data/hospital_cleaned .csv`.
3. Refresh the data source and confirm that the fields load without errors.
4. Start with **Hospital Overview** for overall context, then move to the dashboard that matches the question.

## Recommended Workflow

1. Select a hospital type, state, city, or hospital.
2. Narrow the period using admission year or month where available.
3. Select a department to investigate capacity, staffing, or patient flow.
4. Read the KPI cards before interpreting charts.
5. Select marks in charts to use the workbook's highlight and filter actions.
6. Clear selections before starting a new comparison.

## Dashboard Selection

| Question | Dashboard |
| --- | --- |
| What is the overall activity and patient mix? | Hospital Overview |
| Which departments have capacity or staffing pressure? | Department Analysis |
| How are admissions, discharges, transfers, or stays changing? | Patient Flow |
| How are beds, staff, ICU beds, and equipment being used? | Resource Utilization |

## Useful Filters

- `Hospital Name`, `Hospital Type`, `City`, and `State` define the facility scope.
- `Department` and `Department ID` define the operational unit.
- `Admission Type`, `Diagnosis`, `Gender`, and `Age Group` define the patient segment.
- `Admission Year` and `Admission Month` define the time context.
- `Equipment Status` identifies equipment availability and maintenance patterns.
- `Readmission` and `Transferred` isolate outcome or movement groups.

## Interpreting Visuals

Hover over a mark to view its underlying value and dimensions.

Use the toolbar's undo or revert controls when a selection produces an unexpected view.

When comparing departments, keep the same hospital and time filters active.

A high occupancy rate can indicate strong demand or constrained capacity. Review available beds, staff utilization, ICU capacity, length of stay, and admissions together rather than interpreting occupancy in isolation.

## Exporting Results

Use Tableau's export options to save a crosstab, view data, or image.

Include the dashboard name, filter state, refresh date, and any relevant caveat with exported results.

Do not export or share patient-level information unless authorized.

## Troubleshooting

| Symptom | Action |
| --- | --- |
| Data source cannot be found | Relink the workbook to `data/hospital_cleaned .csv`. |
| Dates or percentages look wrong | Check Tableau field types and the cleaned CSV schema. |
| A count seems too high | Use distinct `Patient ID` and check whether the view is at patient, department, or equipment grain. |
| A dashboard appears filtered unexpectedly | Clear selections and use **Revert** to restore the initial view. |
| Workbook changes are not visible | Refresh the data source and confirm that the CSV was saved before refreshing. |

## Dashboard Testing

The dashboard suite was tested using a structured QA checklist.

- **Total Test Cases:** 40
- **Passed:** 40
- **Failed:** 0
- **Pass Rate:** 100%
- **Major Issues:** 0
- **KPI Validation:** 100% of tested KPIs matched independent validation

The dashboards were checked for KPI accuracy, chart correctness, filters, navigation, interactions, tooltips, layout, and data quality.