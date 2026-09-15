# Module 7 – Testing & Validation

## Project
**Hospital Operations & Patient Analytics Dashboard (MedTrack_DV)**

## Purpose
This module validates the KPI calculations, healthcare metrics, dashboard interactions, and patient-flow analytics of the MedTrack_DV dashboard suite.

## QA Checklist

| Test ID | Test Area | Validation Check | Expected Result | Status |
|---|---|---|---|---|
| QA-01 | KPI | Validate Total Admissions | Value matches the source/final dataset for the selected filters | ☐ verified |
| QA-02 | KPI | Validate Occupancy Rate | Calculated value is consistent with the underlying data | ☐ verified |
| QA-03 | KPI | Validate Average Length of Stay | Dashboard value matches the calculated dataset value | ☐ verified |
| QA-04 | KPI | Validate Readmission Rate | Dashboard value matches the calculated dataset value | ☐ verified |
| QA-05 | KPI | Validate Bed Utilization Rate | Dashboard value is consistent with the underlying data | ☐ verified |
| QA-06 | KPI | Validate Department Efficiency Score | Department-level value is calculated consistently | ☐ Pending |
| QA-07 | Healthcare Metrics | Verify admission and discharge metrics | Values update correctly according to the selected filters | ☐ verified |
| QA-08 | Dashboard Interaction | Test date-range filter | All relevant dashboard views respond correctly | ☐ verified |
| QA-09 | Dashboard Interaction | Test hospital filter | Dashboard visuals update according to hospital selection | ☐ verified |
| QA-10 | Dashboard Interaction | Test department filter | Department-related visuals update correctly | ☐ verified |
| QA-11 | Dashboard Interaction | Test region filter | Region-related visuals update correctly | ☐ verified |
| QA-12 | Navigation | Test navigation between dashboards | Correct dashboard opens from each navigation control | ☐ Pending |
| QA-13 | Patient Flow | Validate admission trends | Trend reflects the underlying admission data | ☐ verified |
| QA-14 | Patient Flow | Validate discharge tracking | Discharge values/trends correspond to the dataset | ☐ verified |
| QA-15 | Patient Flow | Validate average-stay analysis | Average stay is represented consistently | ☐ verified |
| QA-16 | Patient Flow | Validate peak patient-load analysis | Peak periods are represented correctly | ☐ verified |

## Acceptance Criteria

- No major dashboard issues.
- KPI calculations are validated.
- Healthcare metrics are verified.
- Dashboard interactions function correctly.
- Patient-flow analytics are validated.
- Target KPI accuracy: **above 95%**.

> **Important:** Statuses are intentionally left as **Pending** until the dashboard is actually tested. Update them to **Pass** or **Fail** after verification.
