"""
MedTrack_DV - Module 1: Hospital Data Collection
--------------------------------------------------
Purpose:
    Loads the raw patient-level source data, enriches it with the
    operational fields needed for later modules (Department, Hospital,
    Region, Admission/Discharge dates, Patient Type), and saves a single
    integrated dataset: hospital_raw_data.csv

Source file:
    hospital_data_analysis.csv  (Patient Admission Dataset)

Output file:
    hospital_raw_data.csv

Note on enrichment:
    The source file is patient/clinical-level (Condition, Procedure, Cost,
    Length of Stay, Readmission, Outcome, Satisfaction). It does not contain
    hospital operations fields (Department, Hospital, Region, dates) that
    the dashboard KPIs need. This script derives Department from Condition
    using a documented mapping, and generates Hospital / Region / dates /
    Patient Type with a fixed random seed so the enrichment is deterministic
    and reproducible (not real hospital records).
"""

import pandas as pd
import numpy as np
from pathlib import Path

# ---------------------------------------------------------------
# Config
# ---------------------------------------------------------------
RAW_SOURCE_FILE = "hospital_data_analysis.csv"
OUTPUT_FILE = "hospital_raw_data.csv"
RANDOM_SEED = 42

HOSPITALS = [
    "City Care Hospital",
    "Green Valley Hospital",
    "Sunrise Medical Center",
    "Metro Health Institute",
    "HealthPlus Hospital",
]

REGIONS = ["North", "South", "East", "West", "Central"]

PATIENT_TYPES = ["Inpatient", "Outpatient", "Emergency", "Day Care"]
PATIENT_TYPE_WEIGHTS = [0.58, 0.32, 0.07, 0.03]  # roughly matches sample dashboard mix

# Condition -> Department mapping (documented assumption)
CONDITION_TO_DEPARTMENT = {
    "Heart Disease": "Cardiology",
    "Heart Attack": "Cardiology",
    "Diabetes": "General Medicine",
    "Hypertension": "General Medicine",
    "Respiratory Infection": "General Medicine",
    "Kidney Stones": "General Medicine",
    "Osteoarthritis": "Orthopedics",
    "Fractured Arm": "Orthopedics",
    "Fractured Leg": "Orthopedics",
    "Stroke": "ICU",
    "Cancer": "Surgery",
    "Prostate Cancer": "Surgery",
    "Appendicitis": "Surgery",
    "Allergic Reaction": "Emergency",
    "Childbirth": "Pediatrics",
}


def load_raw_data(path: str) -> pd.DataFrame:
    """Load the source patient admission dataset."""
    df = pd.read_csv(path)
    print(f"Loaded {len(df)} rows, {len(df.columns)} columns from {path}")
    return df


def add_department(df: pd.DataFrame) -> pd.DataFrame:
    df["Department"] = df["Condition"].map(CONDITION_TO_DEPARTMENT)
    unmapped = df["Department"].isna().sum()
    if unmapped:
        print(f"WARNING: {unmapped} rows had an unmapped Condition -> set to 'General Medicine'")
        df["Department"] = df["Department"].fillna("General Medicine")
    return df


def add_hospital_and_region(df: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    df["Hospital"] = rng.choice(HOSPITALS, size=len(df))
    df["Region"] = rng.choice(REGIONS, size=len(df))
    return df


def add_patient_type(df: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    df["Patient_Type"] = rng.choice(PATIENT_TYPES, size=len(df), p=PATIENT_TYPE_WEIGHTS)
    return df


def add_admission_discharge_dates(df: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    start = pd.Timestamp("2024-01-01")
    end = pd.Timestamp("2024-12-31")
    date_range_days = (end - start).days
    offsets = rng.integers(0, date_range_days + 1, size=len(df))
    df["Admission_Date"] = start + pd.to_timedelta(offsets, unit="D")
    df["Discharge_Date"] = df["Admission_Date"] + pd.to_timedelta(df["Length_of_Stay"], unit="D")
    return df


def reorder_columns(df: pd.DataFrame) -> pd.DataFrame:
    ordered = [
        "Patient_ID", "Hospital", "Region", "Department", "Patient_Type",
        "Admission_Date", "Discharge_Date", "Age", "Gender", "Condition",
        "Procedure", "Cost", "Length_of_Stay", "Readmission", "Outcome",
        "Satisfaction",
    ]
    return df[ordered]


def summarize(df: pd.DataFrame) -> None:
    completeness = 100 * (1 - df.isna().sum().sum() / df.size)
    print(f"Final dataset: {len(df)} rows, {len(df.columns)} columns")
    print(f"Dataset completeness: {completeness:.2f}%")
    print(f"Hospitals: {df['Hospital'].nunique()} | Regions: {df['Region'].nunique()} | Departments: {df['Department'].nunique()}")
    print(f"Date range: {df['Admission_Date'].min().date()} to {df['Admission_Date'].max().date()}")


def main():
    rng = np.random.default_rng(RANDOM_SEED)

    df = load_raw_data(RAW_SOURCE_FILE)
    df = add_department(df)
    df = add_hospital_and_region(df, rng)
    df = add_patient_type(df, rng)
    df = add_admission_discharge_dates(df, rng)
    df = reorder_columns(df)

    summarize(df)

    Path(OUTPUT_FILE).parent.mkdir(parents=True, exist_ok=True) if Path(OUTPUT_FILE).parent != Path("") else None
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"\nSaved integrated dataset to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
