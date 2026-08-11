# MedTrack_DV — Hospital Operations & Patient Analytics Dashboard

## Milestone 1: Data Collection and Preparation (Weeks 1–2)

### Module 1: Hospital Data Collection

Loads the raw patient admission data, enriches it with the operational
fields (Department, Hospital, Region, Admission/Discharge dates, Patient
Type) needed for later KPI and dashboard work, and produces a single
integrated dataset.

- Input: `data/hospital_data_analysis.csv`
- Output: `data/hospital_raw_data.csv` — 984 rows, 16 columns, 100% complete (target >95%)
- Notebook: `notebooks/hospital_data_collection.ipynb`
- Script: `scripts/data_collection.py`

### Module 2: Data Cleaning & Transformation

Takes `hospital_raw_data.csv` and produces a clean, Tableau-ready dataset:
removes duplicates, handles missing data, standardizes department names,
normalizes types/ranges on the healthcare indicators, and adds a few
derived fields for dashboard use.

- Input: `data/hospital_raw_data.csv`
- Output: `data/hospital_cleaned.csv` — 984 rows, 20 columns, 0% missing (target <2%)
- Notebook: `notebooks/hospital_cleaning.ipynb`
- New fields added: `Admission_Year`, `Admission_Month`, `Admission_Month_Name`, `Is_Readmitted`

### Folder structure
```
medtrack_dv/
├── data/
│   ├── hospital_data_analysis.csv   # original source data
│   ├── hospital_raw_data.csv        # Module 1 output
│   └── hospital_cleaned.csv         # Module 2 output
├── notebooks/
│   ├── hospital_data_collection.ipynb
│   └── hospital_cleaning.ipynb
├── scripts/
│   └── data_collection.py           # script version of Module 1
└── README.md
```

### How to run
```bash
pip install pandas numpy jupyter
jupyter notebook notebooks/hospital_data_collection.ipynb   # Module 1
jupyter notebook notebooks/hospital_cleaning.ipynb           # Module 2
```
or run the Module 1 script version:
```bash
python scripts/data_collection.py
```

### Next step
Module 3 — Hospital KPI Engineering (`generate_hospital_kpis.py`).
