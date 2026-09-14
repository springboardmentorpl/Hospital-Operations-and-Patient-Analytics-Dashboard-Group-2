
---

# `KPI_DEFINITIONS.md`

```markdown
# MedTrack_DV — KPI Definitions

## 1. Overview

The MedTrack_DV Tableau workbook contains healthcare operational KPIs covering patient volume, admissions, length of stay, occupancy, readmission, waiting time, patient satisfaction, hospital capacity and department efficiency.

The project requires a minimum of six KPIs. The Tableau workbook contains more than six KPI measures.

---

## 2. Total Patients

### Tableau Worksheet

`KPI - Total Patients`

### Field

`patient_id`

### Aggregation

`COUNTD(patient_id)`

### Definition

Total number of unique patients represented within the selected dashboard context.

### Purpose

Measures overall patient volume.

---

## 3. Total Admissions

### Tableau Calculated Field

`Total Admissions`

### Field

`patient_admission_flag`

### Calculation

`COUNT(patient_admission_flag)`

### Definition

Counts admission records represented by the patient admission flag.

### Purpose

Measures hospital admission volume.

---

## 4. Average Length of Stay

### Tableau Worksheet

`KPI - Average LOS`

### Field

`length_of_stay_days`

### Aggregation

`AVG(length_of_stay_days)`

### Definition

Average number of days represented by patient length-of-stay records.

### Purpose

Measures patient stay duration and supports operational efficiency analysis.

---

## 5. Occupancy Rate

### Tableau Worksheet

`KPI – Occupancy Rate`

### Field

`bed_occupancy_rate`

### Aggregation

`AVG(bed_occupancy_rate)`

### Definition

Average prepared bed occupancy rate within the selected dashboard context.

### Purpose

Measures hospital occupancy and capacity pressure.

---

## 6. Readmission Rate

### Tableau Worksheet

`KPI - Readmission Rate`

### Field

`is_readmitted`

### Aggregation

`AVG(is_readmitted)`

### Definition

Average value of the readmission indicator.

When `is_readmitted` is represented as a binary 0/1 field, the average represents the proportion of records marked as readmitted.

### Purpose

Supports analysis of patient outcomes and hospital performance.

---

## 7. Bed Utilization Rate

### Tableau Worksheet

`KPI 5 — Bed Utilization Rate`

### Field

`bed_occupancy_rate`

### Aggregation

`AVG(bed_occupancy_rate)`

### Definition

The workbook uses the prepared bed occupancy rate as the bed utilization indicator.

### Purpose

Measures utilization of hospital bed capacity.

---

## 8. Total Beds

### Tableau Worksheet

`KPI 1 — Total Beds`

### Field

`total_beds`

### Aggregation

`SUM(total_beds)`

### Definition

Total bed-capacity measure within the selected dashboard context.

### Purpose

Provides an indication of available hospital capacity.

---

## 9. Occupied Beds

### Tableau Worksheet

`KPI 2 — Occupied Beds`

### Field

`occupied_beds`

### Aggregation

`SUM(occupied_beds)`

### Definition

Total occupied-bed measure within the selected dashboard context.

### Purpose

Measures occupied hospital bed capacity.

---

## 10. Average Wait Time

### Tableau Worksheet

`KPI 3 — Average Wait Time`

### Field

`patient_waittime`

### Aggregation

`AVG(patient_waittime)`

### Definition

Average patient waiting time within the selected dashboard context.

### Purpose

Measures patient-flow efficiency and waiting-time pressure.

---

## 11. Patients Waiting >45 Minutes

### Tableau Worksheet

`KPI 4 — Patients Waiting >45 Min`

### Supporting Field

`waittime_over_45min`

### Patient Field

`patient_id`

### Definition

Measures patients associated with the wait-time-over-45-minute indicator.

### Purpose

Highlights longer waiting times and potential patient-flow bottlenecks.

---

## 12. Patient Satisfaction Score

### Tableau Worksheet

`KPI - Satisfaction Score`

### Field

`patient_satisfaction_score`

### Aggregation

`AVG(patient_satisfaction_score)`

### Definition

Average patient satisfaction score within the selected dashboard context.

### Purpose

Provides an indicator of patient experience.

---

## 13. Department Efficiency Score

### Tableau Worksheet

`Department Efficiency Score`

### Field

`department_efficiency_score`

### Aggregation

`AVG(department_efficiency_score)`

### Definition

Average department efficiency score.

### Purpose

Supports comparison of operational efficiency across departments.

---

## 14. KPI Summary

| KPI | Tableau Field | Aggregation |
|---|---|---|
| Total Patients | `patient_id` | COUNTD |
| Total Admissions | `patient_admission_flag` | COUNT |
| Average LOS | `length_of_stay_days` | AVG |
| Occupancy Rate | `bed_occupancy_rate` | AVG |
| Readmission Rate | `is_readmitted` | AVG |
| Bed Utilization Rate | `bed_occupancy_rate` | AVG |
| Total Beds | `total_beds` | SUM |
| Occupied Beds | `occupied_beds` | SUM |
| Average Wait Time | `patient_waittime` | AVG |
| Patients Waiting >45 Min | `waittime_over_45min` / `patient_id` | Patient count |
| Satisfaction Score | `patient_satisfaction_score` | AVG |
| Department Efficiency Score | `department_efficiency_score` | AVG |

---

## 15. KPI Usage by Dashboard

| Dashboard | Main KPIs |
|---|---|
| Hospital Overview | Total Patients, Average LOS, Occupancy Rate, Readmission Rate, Satisfaction Score |
| Patient Flow | Total Patients, Average Wait Time, Patients Waiting >45 Min, Average LOS |
| Department Analytics | KPI #2, Average Wait Time, Average LOS, Readmission Rate, Department Efficiency Score |
| Resource Utilization | Total Beds, Occupied Beds, Bed Utilization Rate, Average LOS, Average Wait Time |

---

## 16. KPI Validation

The project evaluation target is:

**KPI Accuracy > 95%**

All KPI calculations should be validated against the underlying cleaned and enriched dataset before final project delivery.

---

## 17. KPI Interpretation

KPI values depend on:

- Selected filters
- Selected time period
- Selected department
- Dataset records included in the dashboard

The KPIs are intended for healthcare operations analytics and are not clinical diagnosis or treatment measures.