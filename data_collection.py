import pandas as pd
from pathlib import Path

# ============================================================
# MEDTRACK_DV - MODULE 1
# DATA COLLECTION & INTEGRATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = BASE_DIR / "hospital_raw_data.csv"


# ============================================================
# LOAD CSV FILES
# ============================================================

def load_csv(filename):
    file_path = BASE_DIR / filename

    if not file_path.exists():
        print(f"ERROR: {filename} not found")
        return None

    df = pd.read_csv(file_path)

    print(
        f"Loaded {filename}: "
        f"{df.shape[0]:,} rows x {df.shape[1]} columns"
    )

    return df


# ============================================================
# LOAD DATASETS
# ============================================================

print("=" * 60)
print("MEDTRACK_DV - MODULE 1")
print("HOSPITAL DATA COLLECTION & INTEGRATION")
print("=" * 60)

patient = load_csv("patient.csv")
admission = load_csv("admission.csv")
department = load_csv("department.csv")
ward = load_csv("ward.csv")
bed = load_csv("bed.csv")
disease = load_csv("disease.csv")

employee = load_csv("employee.csv")
doctor = load_csv("doctor.csv")
staff_assignment = load_csv("staff_assignment.csv")


# ============================================================
# CHECK REQUIRED FILES
# ============================================================

required = {
    "patient.csv": patient,
    "admission.csv": admission,
    "department.csv": department,
    "ward.csv": ward,
    "bed.csv": bed,
    "disease.csv": disease
}

missing_files = [
    file_name
    for file_name, dataframe in required.items()
    if dataframe is None
]

if missing_files:
    raise FileNotFoundError(
        "Missing files: " + ", ".join(missing_files)
    )


# ============================================================
# DISPLAY COLUMNS
# ============================================================

print("\nPATIENT COLUMNS")
print(patient.columns.tolist())

print("\nADMISSION COLUMNS")
print(admission.columns.tolist())

print("\nDEPARTMENT COLUMNS")
print(department.columns.tolist())

print("\nWARD COLUMNS")
print(ward.columns.tolist())

print("\nBED COLUMNS")
print(bed.columns.tolist())

print("\nDISEASE COLUMNS")
print(disease.columns.tolist())


# ============================================================
# START WITH ADMISSION TABLE
# ============================================================

hospital_data = admission.copy()

print("\nStarting rows:", len(hospital_data))


# ============================================================
# MERGE PATIENT
# ============================================================

hospital_data = hospital_data.merge(
    patient,
    on="patient_id",
    how="left",
    suffixes=("", "_patient")
)

print(
    "After patient merge:",
    len(hospital_data)
)


# ============================================================
# MERGE DEPARTMENT
# ============================================================

hospital_data = hospital_data.merge(
    department,
    on="department_id",
    how="left",
    suffixes=("", "_department")
)

print(
    "After department merge:",
    len(hospital_data)
)


# ============================================================
# MERGE WARD
# ============================================================

hospital_data = hospital_data.merge(
    ward[
        [
            "ward_id",
            "ward_name",
            "ward_type",
            "total_beds"
        ]
    ],
    on="ward_id",
    how="left"
)

print(
    "After ward merge:",
    len(hospital_data)
)


# ============================================================
# MERGE BED
# ============================================================

hospital_data = hospital_data.merge(
    bed[
        [
            "bed_id",
            "bed_number",
            "bed_status"
        ]
    ],
    on="bed_id",
    how="left"
)

print(
    "After bed merge:",
    len(hospital_data)
)


# ============================================================
# MERGE DISEASE
# ============================================================

hospital_data = hospital_data.merge(
    disease[
        [
            "disease_id",
            "disease_name",
            "disease_category"
        ]
    ],
    on="disease_id",
    how="left"
)

print(
    "After disease merge:",
    len(hospital_data)
)


# ============================================================
# DATE CONVERSION
# ============================================================

hospital_data["admission_date"] = pd.to_datetime(
    hospital_data["admission_date"],
    errors="coerce"
)

hospital_data["discharge_date"] = pd.to_datetime(
    hospital_data["discharge_date"],
    errors="coerce"
)

hospital_data["date_of_birth"] = pd.to_datetime(
    hospital_data["date_of_birth"],
    errors="coerce"
)


# ============================================================
# LENGTH OF STAY
# ============================================================

hospital_data["Length_of_Stay_Days"] = (
    hospital_data["discharge_date"]
    - hospital_data["admission_date"]
).dt.days


# ============================================================
# PATIENT AGE
# ============================================================

hospital_data["Patient_Age"] = (
    (
        hospital_data["admission_date"]
        - hospital_data["date_of_birth"]
    ).dt.days / 365.25
).round(0)


# ============================================================
# AGE GROUP
# ============================================================

hospital_data["Age_Group"] = pd.cut(
    hospital_data["Patient_Age"],
    bins=[0, 17, 30, 45, 60, 75, 120],
    labels=[
        "0-17",
        "18-30",
        "31-45",
        "46-60",
        "61-75",
        "76+"
    ],
    include_lowest=True
)


# ============================================================
# TIME DIMENSIONS
# ============================================================

hospital_data["Admission_Month"] = (
    hospital_data["admission_date"]
    .dt.to_period("M")
    .astype(str)
)

hospital_data["Admission_Year"] = (
    hospital_data["admission_date"]
    .dt.year
)

hospital_data["Admission_Quarter"] = (
    hospital_data["admission_date"]
    .dt.quarter
)


# ============================================================
# BED OCCUPANCY FLAG
# ============================================================

hospital_data["Bed_Occupied_Flag"] = (
    hospital_data["bed_status"]
    .astype(str)
    .str.lower()
    .isin([
        "occupied",
        "booked",
        "assigned"
    ])
    .astype(int)
)


# ============================================================
# DUPLICATE CHECK
# ============================================================

duplicate_rows = hospital_data.duplicated().sum()

duplicate_admissions = (
    hospital_data["admission_id"]
    .duplicated()
    .sum()
)

print("\nDuplicate rows:", duplicate_rows)
print("Duplicate admission IDs:", duplicate_admissions)


# ============================================================
# MISSING VALUE CHECK
# ============================================================

missing_count = hospital_data.isnull().sum()

missing_percentage = (
    hospital_data.isnull().mean() * 100
).round(2)

missing_report = pd.DataFrame({
    "Missing_Count": missing_count,
    "Missing_Percentage": missing_percentage
})

print("\nMissing Value Report")
print(
    missing_report
    .sort_values(
        "Missing_Percentage",
        ascending=False
    )
)


# ============================================================
# DATASET COMPLETENESS
# ============================================================

total_cells = (
    hospital_data.shape[0]
    * hospital_data.shape[1]
)

missing_cells = (
    hospital_data.isnull()
    .sum()
    .sum()
)

completeness = (
    1 - (missing_cells / total_cells)
) * 100

print("\nDataset Completeness:")
print(f"{completeness:.2f}%")


# ============================================================
# SAVE RAW INTEGRATED DATASET
# ============================================================

hospital_data.to_csv(
    OUTPUT_FILE,
    index=False
)


# ============================================================
# FINAL OUTPUT
# ============================================================

print("\n" + "=" * 60)
print("MODULE 1 COMPLETED")
print("=" * 60)

print(
    f"Rows    : {hospital_data.shape[0]:,}"
)

print(
    f"Columns : {hospital_data.shape[1]:,}"
)

print(
    f"File    : {OUTPUT_FILE}"
)

print("=" * 60)