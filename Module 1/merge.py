import pandas as pd

# Read the original CSV files
patient = pd.read_csv("data/patient.csv")
admission = pd.read_csv("data/admission.csv")
department = pd.read_csv("data/department.csv")
ward = pd.read_csv("data/ward.csv")
bed = pd.read_csv("data/bed.csv")

# Merge Admission + Patient
merged = pd.merge(
    admission,
    patient,
    on="patient_id",
    how="left"
)

# Merge Department
merged = pd.merge(
    merged,
    department,
    on="department_id",
    how="left"
)

# Merge Ward
merged = pd.merge(
    merged,
    ward,
    on="ward_id",
    how="left"
)

# Merge Bed
merged = pd.merge(
    merged,
    bed,
    on="bed_id",
    how="left"
)

# Display the raw merged dataset
print("\n========== RAW MERGED DATASET ==========")
print(merged.head(10))

print("\nRows:", len(merged))
print("Columns:", len(merged.columns))

# Save the RAW dataset
merged.to_csv(
    "hospital_raw_dataset.csv",
    index=False
)

print("\n========================================")
print("RAW DATASET SAVED SUCCESSFULLY!")
print("File: hospital-raw-datasets.csv")
print("========================================")