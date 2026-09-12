import pandas as pd

df = pd.read_csv("data/clean/hospital_cleaned.csv")

print("Dataset loaded successfully!")
print("Shape:", df.shape)
print("Unique admissions:", df["admission_id"].nunique())
print("Unique patients:", df["patient_id"].nunique())

# KPI 1: Total Admissions
total_admissions = df["admission_id"].nunique()

print("\n=== HOSPITAL KPIs ===")
print("Total Admissions:", total_admissions)

# KPI 2: Occupancy Rate
total_beds = 415
occupied_beds = 270

occupancy_rate = (occupied_beds / total_beds) * 100

print("Occupancy Rate:", round(occupancy_rate, 2), "%")

# KPI 3: Average Length of Stay
average_length_of_stay = df["length_of_stay"].mean()

print("Average Length of Stay:", round(average_length_of_stay, 2), "days")

# KPI 4: Readmission Rate
total_unique_patients = df["patient_id"].nunique()

patient_admission_counts = df.groupby("patient_id")["admission_id"].nunique()

readmitted_patients = (patient_admission_counts > 1).sum()

readmission_rate = (readmitted_patients / total_unique_patients) * 100

print("Readmission Rate:", round(readmission_rate, 2), "%")

# KPI 5: Bed Utilization Rate
bed_utilization_rate = (occupied_beds / total_beds) * 100

print("Bed Utilization Rate:", round(bed_utilization_rate, 2), "%")

# KPI 6: Department Efficiency Score

department_metrics = df.groupby("department_name").agg(
    total_admissions=("admission_id", "nunique"),
    unique_patients=("patient_id", "nunique"),
    average_length_of_stay=("length_of_stay", "mean")
).reset_index()

# Count patients with more than one admission within each department
department_readmissions = (
    df.groupby(["department_name", "patient_id"])["admission_id"]
    .nunique()
    .reset_index(name="admission_count")
)

department_readmissions = (
    department_readmissions[department_readmissions["admission_count"] > 1]
    .groupby("department_name")
    .size()
    .reset_index(name="readmitted_patients")
)

# Merge readmission counts
department_metrics = department_metrics.merge(
    department_readmissions,
    on="department_name",
    how="left"
)

department_metrics["readmitted_patients"] = (
    department_metrics["readmitted_patients"].fillna(0)
)

# Department readmission rate
department_metrics["readmission_rate"] = (
    department_metrics["readmitted_patients"]
    / department_metrics["unique_patients"]
) * 100

# Efficiency score: lower readmission rate = higher efficiency
department_metrics["efficiency_score"] = (
    100 - department_metrics["readmission_rate"]
)

print("\n=== DEPARTMENT EFFICIENCY ===")
print(department_metrics.round(2).to_string(index=False))


# ==========================================
# CREATE FINAL EXCEL DATASET
# ==========================================

# Overall hospital KPIs
hospital_kpis = pd.DataFrame({
    "KPI": [
        "Total Admissions",
        "Occupancy Rate",
        "Average Length of Stay",
        "Readmission Rate",
        "Bed Utilization Rate"
    ],
    "Value": [
        total_admissions,
        round(occupancy_rate, 2),
        round(average_length_of_stay, 2),
        round(readmission_rate, 2),
        round(bed_utilization_rate, 2)
    ]
})

# Add Department Efficiency Score as a separate sheet
department_efficiency = department_metrics.copy()

# Save everything into one Excel workbook
output_file = "hospital_final_dataset.xlsx"

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:

    # Main admission-level dataset
    df.to_excel(
        writer,
        sheet_name="Hospital_Data",
        index=False
    )

    # Overall hospital KPIs
    hospital_kpis.to_excel(
        writer,
        sheet_name="Hospital_KPIs",
        index=False
    )

    # Department-level efficiency
    department_efficiency.to_excel(
        writer,
        sheet_name="Department_Efficiency",
        index=False
    )

print("\n========================================")
print("Excel file created successfully!")
print("File:", output_file)
print("========================================")