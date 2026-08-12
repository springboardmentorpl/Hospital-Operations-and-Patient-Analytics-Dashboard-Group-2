import pandas as pd

# ============================================================
# HOSPITAL KPI ENGINEERING
# ============================================================

# Load dataset
df = pd.read_csv("hospital patient.csv")

# ------------------------------------------------------------
# DATA CLEANING
# ------------------------------------------------------------

# Remove duplicate rows
df = df.drop_duplicates()

# Convert dates
df["Admission_Date"] = pd.to_datetime(
    df["Admission_Date"], dayfirst=True, errors="coerce"
)

df["Discharge_Date"] = pd.to_datetime(
    df["Discharge_Date"], dayfirst=True, errors="coerce"
)

# Convert numeric columns
df["Length_of_Stay"] = pd.to_numeric(
    df["Length_of_Stay"], errors="coerce"
)

df["Satisfaction"] = pd.to_numeric(
    df["Satisfaction"], errors="coerce"
)

df["Total_Cost"] = pd.to_numeric(
    df["Total_Cost"], errors="coerce"
)

# Remove records with missing important values
df = df.dropna(
    subset=["Patient_ID", "Admission_Date",
            "Discharge_Date", "Length_of_Stay"]
)

# ============================================================
# KPI 1 - TOTAL ADMISSIONS
# ============================================================

total_admissions = len(df)

# ============================================================
# KPI 2 - AVERAGE LENGTH OF STAY
# ============================================================

average_length_of_stay = df["Length_of_Stay"].mean()

# ============================================================
# KPI 3 - READMISSION RATE
# ============================================================

readmitted_patients = (
    df["Readmission"]
    .astype(str)
    .str.strip()
    .str.lower()
    .eq("yes")
    .sum()
)

readmission_rate = (
    readmitted_patients / total_admissions
) * 100

# ============================================================
# KPI 4 & 5 - OCCUPANCY RATE / BED UTILIZATION RATE
# ============================================================

# Your dataset does not contain a bed-capacity column.
# We use 100 beds as the project assumption.
TOTAL_BEDS = 100

# Hospital analysis period
start_date = df["Admission_Date"].min()
end_date = df["Discharge_Date"].max()

number_of_days = (end_date - start_date).days + 1

# Total occupied bed-days
occupied_bed_days = df["Length_of_Stay"].sum()

# Available bed-days
available_bed_days = TOTAL_BEDS * number_of_days

# Occupancy Rate
occupancy_rate = (
    occupied_bed_days / available_bed_days
) * 100

# Bed Utilization Rate
bed_utilization_rate = (
    occupied_bed_days / available_bed_days
) * 100

# ============================================================
# KPI 6 - DEPARTMENT EFFICIENCY SCORE
# ============================================================

# Your dataset has no Department column.
# We use Condition as the operational group/proxy.
department_col = "Condition"

department_data = df.groupby(department_col).agg(
    Patients=("Patient_ID", "count"),
    Average_LOS=("Length_of_Stay", "mean"),
    Readmission_Rate=(
        "Readmission",
        lambda x: (
            x.astype(str)
            .str.strip()
            .str.lower()
            .eq("yes")
            .mean()
            * 100
        )
    ),
    Average_Satisfaction=("Satisfaction", "mean"),
    Total_Revenue=("Total_Cost", "sum")
).reset_index()

# Min-Max normalization
def normalize(series):
    min_value = series.min()
    max_value = series.max()

    if max_value == min_value:
        return pd.Series([100] * len(series), index=series.index)

    return (
        (series - min_value) /
        (max_value - min_value)
    ) * 100


# Higher satisfaction = better
satisfaction_score = normalize(
    department_data["Average_Satisfaction"]
)

# Lower LOS = better
los_score = 100 - normalize(
    department_data["Average_LOS"]
)

# Lower readmission = better
readmission_score = 100 - normalize(
    department_data["Readmission_Rate"]
)

# Final efficiency score
department_data["Efficiency_Score"] = (
    satisfaction_score * 0.40
    + los_score * 0.30
    + readmission_score * 0.30
)

department_data["Efficiency_Score"] = (
    department_data["Efficiency_Score"].round(2)
)

# ============================================================
# KPI SUMMARY
# ============================================================

kpi_summary = pd.DataFrame({
    "KPI": [
        "Total Admissions",
        "Occupancy Rate",
        "Average Length of Stay",
        "Readmission Rate",
        "Bed Utilization Rate",
        "Department Efficiency Score"
    ],
    "Value": [
        total_admissions,
        round(occupancy_rate, 2),
        round(average_length_of_stay, 2),
        round(readmission_rate, 2),
        round(bed_utilization_rate, 2),
        round(department_data["Efficiency_Score"].mean(), 2)
    ],
    "Unit": [
        "Patients",
        "%",
        "Days",
        "%",
        "%",
        "Score / 100"
    ]
})

# ============================================================
# CREATE TABLEAU-READY DATA
# ============================================================

df["Occupancy_Rate"] = round(occupancy_rate, 2)

df["Bed_Utilization_Rate"] = round(
    bed_utilization_rate, 2
)

df["Average_Length_of_Stay"] = round(
    average_length_of_stay, 2
)

df["Readmission_Rate"] = round(
    readmission_rate, 2
)

# ============================================================
# EXPORT TO EXCEL
# ============================================================

output_file = "hospital_final_dataset.xlsx"

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:

    # Clean patient data
    df.to_excel(
        writer,
        sheet_name="Patient_Data",
        index=False
    )

    # Overall KPI summary
    kpi_summary.to_excel(
        writer,
        sheet_name="KPI_Summary",
        index=False
    )

    # Department / condition analysis
    department_data.to_excel(
        writer,
        sheet_name="Department_Analysis",
        index=False
    )

print("\n")
print("=" * 55)
print("       HOSPITAL KPI REPORT")
print("=" * 55)

print("\nKPI 1 - TOTAL ADMISSIONS")
print("Total Admissions:", total_admissions)

print("\nKPI 2 - AVERAGE LENGTH OF STAY")
print(
    "Average Length of Stay:",
    round(average_length_of_stay, 2),
    "days"
)

print("\nKPI 3 - READMISSION RATE")
print("Readmitted Patients:", readmitted_patients)
print(
    "Readmission Rate:",
    round(readmission_rate, 2),
    "%"
)

print("\nKPI 4 - OCCUPANCY RATE")
print("Assumed Total Beds:", TOTAL_BEDS)
print(
    "Occupancy Rate:",
    round(occupancy_rate, 2),
    "%"
)

print("\nKPI 5 - BED UTILIZATION RATE")
print(
    "Bed Utilization Rate:",
    round(bed_utilization_rate, 2),
    "%"
)

print("\nKPI 6 - DEPARTMENT EFFICIENCY SCORE")
print(
    "Average Efficiency Score:",
    round(department_data["Efficiency_Score"].mean(), 2),
    "/ 100"
)

print("\n" + "=" * 55)
print("Excel file created successfully!")
print("File:", output_file)
print("=" * 55)