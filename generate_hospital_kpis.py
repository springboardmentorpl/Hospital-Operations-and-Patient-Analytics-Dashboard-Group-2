import pandas as pd

# ============================================================
# 1. FILE PATHS
# ============================================================

INPUT_FILE = "hospital_cleaned.csv"
OUTPUT_FILE = "hospital_final_dataset.xlsx"


# ============================================================
# 2. LOAD CLEANED DATASET
# ============================================================

df = pd.read_csv(INPUT_FILE)

print("Dataset loaded successfully.")
print("Rows    :", len(df))
print("Columns :", len(df.columns))


# ============================================================
# 3. OVERALL HOSPITAL KPI CALCULATIONS
# ============================================================

# Total number of admission records
total_admissions = df["Patient ID"].count()

# Total billing revenue
total_revenue = df["Billing Amount"].sum()

# Average Length of Stay
average_los = df["Length of Stay"].mean()

# Readmission Rate
readmission_rate = (
    df["Readmission"].eq("Yes").sum()
    / total_admissions
) * 100

# Bed Utilization Rate
bed_utilization_rate = (
    df["Bed Occupied"].eq("Yes").sum()
    / total_admissions
) * 100

# Average Staff Utilization Rate
staff_utilization_rate = (
    df["Staff_Utilization_%_Derived"].mean()
)


# ============================================================
# 4. DEPARTMENT-WISE KPI CALCULATIONS
# ============================================================

department_kpis = df.groupby("Department").agg(
    Bed_Utilization_Rate=(
        "Bed Occupied",
        lambda x: (x.eq("Yes").sum() / len(x)) * 100
    ),

    Staff_Utilization_Rate=(
        "Staff_Utilization_%_Derived",
        "mean"
    ),

    Readmission_Rate=(
        "Readmission",
        lambda x: (x.eq("Yes").sum() / len(x)) * 100
    )
).reset_index()


# ============================================================
# 5. DEPARTMENT EFFICIENCY SCORE
# ============================================================

department_kpis["Efficiency_Score"] = (
    department_kpis["Bed_Utilization_Rate"]
    + department_kpis["Staff_Utilization_Rate"]
    + (100 - department_kpis["Readmission_Rate"])
) / 3

department_kpis["Efficiency_Score"] = (
    department_kpis["Efficiency_Score"].round(2)
)


# ============================================================
# 6. OVERALL HOSPITAL KPI SUMMARY
# ============================================================

hospital_kpis = pd.DataFrame({
    "KPI": [
        "Total Admissions",
        "Total Revenue",
        "Average Length of Stay",
        "Readmission Rate (%)",
        "Bed Utilization Rate (%)",
        "Average Staff Utilization Rate (%)"
    ],

    "Value": [
        total_admissions,
        round(total_revenue, 2),
        round(average_los, 2),
        round(readmission_rate, 2),
        round(bed_utilization_rate, 2),
        round(staff_utilization_rate, 2)
    ]
})


# ============================================================
# 7. PRINT KPI SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("              HOSPITAL KPI SUMMARY")
print("=" * 60)

print(f"Total Admissions          : {total_admissions}")
print(f"Total Revenue             : {total_revenue:.2f}")
print(f"Average Length of Stay    : {average_los:.2f} days")
print(f"Readmission Rate          : {readmission_rate:.2f}%")
print(f"Bed Utilization Rate      : {bed_utilization_rate:.2f}%")
print(f"Staff Utilization Rate    : {staff_utilization_rate:.2f}%")

print("=" * 60)


# ============================================================
# 8. DISPLAY DEPARTMENT EFFICIENCY
# ============================================================

print("\n" + "=" * 60)
print("       DEPARTMENT EFFICIENCY SCORE")
print("=" * 60)

print(
    department_kpis[
        [
            "Department",
            "Bed_Utilization_Rate",
            "Staff_Utilization_Rate",
            "Readmission_Rate",
            "Efficiency_Score"
        ]
    ].to_string(index=False)
)


# ============================================================
# 9. EXPORT FINAL EXCEL FILE
# ============================================================

with pd.ExcelWriter(
    OUTPUT_FILE,
    engine="openpyxl"
) as writer:

    # Cleaned patient-level data
    df.to_excel(
        writer,
        sheet_name="Cleaned_Data",
        index=False
    )

    # Overall hospital KPIs
    hospital_kpis.to_excel(
        writer,
        sheet_name="Hospital_KPIs",
        index=False
    )

    # Department-wise KPIs
    department_kpis.to_excel(
        writer,
        sheet_name="Department_KPIs",
        index=False
    )


# ============================================================
# 10. COMPLETION MESSAGE
# ============================================================

print("\n" + "=" * 60)
print("FINAL EXPORT COMPLETED SUCCESSFULLY ✅")
print("=" * 60)

print("Final Excel file:", OUTPUT_FILE)
print("Sheets created:")
print("1. Cleaned_Data")
print("2. Hospital_KPIs")
print("3. Department_KPIs")