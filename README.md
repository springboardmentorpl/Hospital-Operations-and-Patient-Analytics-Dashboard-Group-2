# MedTrack_DV

## Hospital Operations & Patient Analytics Dashboard — Group 2

An interactive Tableau dashboard suite for hospital operations and patient analytics, built from publicly available hospital and patient admission datasets.

---

## Dashboards

The final Tableau workbook `Dashboard/MedTrack_DV.twb` contains four interconnected dashboards:

| # | Dashboard | Focus |
|---|---|---|
| 1 | Hospital Overview | Hospital performance KPIs, admissions, occupancy, readmission, satisfaction |
| 2 | Patient Flow | Admission trends, waiting time, admission status/shifts, length of stay |
| 3 | Department Analytics | Department performance, efficiency, readmission, wait-time comparison |
| 4 | Resource Utilization | Bed capacity, occupancy, bed utilization, department efficiency |

---

## Repository Structure

```text
├── Scripts/        → Python code (collection, cleaning, KPI engineering)
├── Module 1–3/     → Data (raw, cleaned/enriched, final KPI dataset)
├── Module 4/       → Dashboard storyboard (planning)
├── Module 5–7/     → Dashboard development and validated workbooks
├── Dashboard/      → Final Tableau workbook (MedTrack_DV)
├── Module 8/       → Final documentation package
└── Documents/      → Project documentation
```

---

## Documentation

All documentation is delivered as PDF in [`Documents/`](Documents/):

| Document | Contents |
|---|---|
| [FINAL_PROJECT_DOCUMENTATION.pdf](Documents/FINAL_PROJECT_DOCUMENTATION.pdf) | Complete Module 8 project documentation (incl. future scope) |
| [DATASET_SOURCES.pdf](Documents/DATASET_SOURCES.pdf) | Dataset origin and field reference |
| [KPI_DEFINITIONS.pdf](Documents/KPI_DEFINITIONS.pdf) | All KPI definitions, formulas, worked calculations and computed values |
| [DASHBOARD_GUIDE.pdf](Documents/DASHBOARD_GUIDE.pdf) | Dashboard-by-dashboard user guide |
| [HEALTHCARE_OPERATIONS_METHODOLOGY.pdf](Documents/HEALTHCARE_OPERATIONS_METHODOLOGY.pdf) | End-to-end project methodology |

Markdown sources are kept in the local `Documents/` folder for editing; the versioned deliverables are the PDFs.

---

## Tech Stack

- **Data Collection & Processing:** Python (Pandas, NumPy)
- **Visualization:** Tableau Desktop / Tableau Public
- **Dashboard Integration:** Tableau Filters, Parameters, Actions
- **Documentation:** Markdown, GitHub

---

## Getting Started

1. Clone the repository.
2. Run the scripts in `Scripts/` in order: `data_collection.py` → `data_cleaning_transformation.ipynb` → `generate_hospital_kpis.py`.
3. Open `Dashboard/MedTrack_DV.twb` in Tableau Desktop or publish to Tableau Public.
4. Explore the four dashboards: Hospital Overview → Patient Flow → Department Analytics → Resource Utilization.
