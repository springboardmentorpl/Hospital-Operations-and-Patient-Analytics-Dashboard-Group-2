import pandas as pd
from pathlib import Path


# ============================================================
# HOSPITAL KPI ENGINEERING - MILESTONE 2

print("=" * 70)
print("HOSPITAL OPERATIONS - KPI ENGINEERING")
print("=" * 70)
# ============================================================
# 1. FILE PATHS
BASE_DIR = Path(__file__).resolve().parent

INPUT_FILE = BASE_DIR / "Hospital_ER_Cleaned.csv"
OUTPUT_FILE = BASE_DIR / "hospital_final_dataset.xlsx"
# ============================================================
# 2. LOAD CLEANED DATASET
df = pd.read_csv(INPUT_FILE)
print("\nCleaned dataset loaded successfully!")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
# ============================================================
# 3. REQUIRED COLUMNS
required_columns = [
    "Patient Id",
    "Patient Admission Date",
    "Department Referral",
    "Patient Admission Flag",
    "Patient Satisfaction Score",
    "Patient Waittime",
    "Waittime Normalized",
    "Satisfaction Normalized"
]
missing_columns = [
    column
    for column in required_columns
    if column not in df.columns
]
if missing_columns:
    print("\nERROR: Missing required columns:")

    for column in missing_columns:
        print("-", column)

    raise ValueError(
        "Required columns are missing from the cleaned dataset.")
print("\nAll required columns are available.")
# ============================================================
# 4. DATA TYPE CONVERSION
# Admission date
df["Patient Admission Date"] = pd.to_datetime(
    df["Patient Admission Date"],
    errors="coerce")
# Admission flag
df["Patient Admission Flag"] = pd.to_numeric(
    df["Patient Admission Flag"],
    errors="coerce").fillna(0)
# Numerical columns
numeric_columns = [
    "Patient Satisfaction Score",
    "Patient Waittime",
    "Waittime Normalized",
    "Satisfaction Normalized"]
for column in numeric_columns:
   df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )
# ============================================================
# KPI 1
# TOTAL ADMISSIONS
total_records = len(df)
total_admissions = int(
    df["Patient Admission Flag"].sum()
)
print("\n" + "-" * 70)
print("KPI 1 - TOTAL ADMISSIONS")
print("-" * 70)
print(
    "Total Patient Records:",
    total_records)
print(
    "Total Admissions:",
    total_admissions
)
# ============================================================
# KPI 2
# ADMISSION RATE
#
# Replacement for Occupancy Rate
# because the dataset does not contain bed information.
if total_records > 0:

    admission_rate = (
        total_admissions/ total_records) * 100
else:

    admission_rate = 0
print("\n" + "-" * 70)
print("KPI 2 - ADMISSION RATE")
print("-" * 70)
print(
    f"Admission Rate: "
    f"{admission_rate:.2f}%")
# ============================================================
# KPI 3
# AVERAGE PATIENT WAIT TIME
# Replacement for Average Length of Stay
# because the dataset has no discharge date.
average_wait_time = (df["Patient Waittime"].mean())
print("\n" + "-" * 70)
print("KPI 3 - AVERAGE PATIENT WAIT TIME")
print("-" * 70)
print(
    f"Average Patient Wait Time: "
    f"{average_wait_time:.2f} minutes")
# ============================================================
# KPI 4
# AVERAGE PATIENT SATISFACTION
# Replacement for Readmission Rate
# because the dataset does not contain a readmission indicator.
average_satisfaction = (df["Patient Satisfaction Score"].mean())
print("\n" + "-" * 70)
print("KPI 4 - AVERAGE PATIENT SATISFACTION")
print("-" * 70)
print(
    f"Average Patient Satisfaction: "
    f"{average_satisfaction:.2f}")
# ============================================================
# KPI 5
# PATIENT FLOW EFFICIENCY RATE
# Replacement for Bed Utilization Rate
# Higher normalized waiting-time performance
# = better patient flow.
# Formula:
# (1 - Waittime Normalized) × 100
df["Patient Flow Efficiency Rate"] = ( 1 - df["Waittime Normalized"]) * 100
df["Patient Flow Efficiency Rate"] = (
    df["Patient Flow Efficiency Rate"].clip(0, 100).round(2))
patient_flow_efficiency_rate = (
    df["Patient Flow Efficiency Rate"].mean())
print("\n" + "-" * 70)
print("KPI 5 - PATIENT FLOW EFFICIENCY RATE")
print("-" * 70)
print(
    f"Patient Flow Efficiency Rate: "
    f"{patient_flow_efficiency_rate:.2f}%")
# ============================================================
# KPI 6
# DEPARTMENT EFFICIENCY SCORE
# Satisfaction = 60%
# Waiting-time performance = 40%
# Higher satisfaction = better
# Lower waiting time = better
df["Department Efficiency Score"] = (
(df["Satisfaction Normalized"]* 0.60)+((1 - df["Waittime Normalized"])* 0.40)) * 100

df["Department Efficiency Score"] = (
    df["Department Efficiency Score"]
    .clip(0, 100)
    .round(2)
)


department_efficiency_score = (
    df["Department Efficiency Score"].mean()
)


print("\n" + "-" * 70)
print("KPI 6 - DEPARTMENT EFFICIENCY SCORE")
print("-" * 70)


print(
    f"Overall Department Efficiency Score: "
    f"{department_efficiency_score:.2f}"
)
# ============================================================
# SUPPORTING KPI
# AVERAGE WAIT TIME
print("\n" + "-" * 70)
print("SUPPORTING OPERATIONAL METRICS")
print("-" * 70)
print(
    f"Average Wait Time: "
    f"{average_wait_time:.2f} minutes")
print(
    f"Average Satisfaction: "
    f"{average_satisfaction:.2f}")
# ============================================================
# ADD OVERALL KPI VALUES TO PATIENT DATA
df["Total Admissions KPI"] = (
    total_admissions
)


df["Admission Rate KPI"] = round(
    admission_rate,
    2
)


df["Average Wait Time KPI"] = round(
    average_wait_time,
    2
)


df["Average Satisfaction KPI"] = round(
    average_satisfaction,
    2
)


df["Patient Flow Efficiency KPI"] = round(
    patient_flow_efficiency_rate,
    2
)


df["Overall Department Efficiency KPI"] = round(
    department_efficiency_score,
    2
)
# ============================================================
# DEPARTMENT-LEVEL KPI TABLE
print("\n" + "-" * 70)
print("CREATING DEPARTMENT KPI TABLE")
print("-" * 70)
department_kpis = (

    df.groupby(
        "Department Referral"
    )
    .agg(

        Total_Patient_Records=(
            "Patient Id",
            "count"
        ),

        Total_Admissions=(
            "Patient Admission Flag",
            "sum"
        ),

        Average_Wait_Time=(
            "Patient Waittime",
            "mean"
        ),

        Average_Satisfaction=(
            "Patient Satisfaction Score",
            "mean"
        ),

        Patient_Flow_Efficiency=(
            "Patient Flow Efficiency Rate",
            "mean"
        ),

        Department_Efficiency_Score=(
            "Department Efficiency Score",
            "mean")).reset_index())
# ============================================================
# DEPARTMENT ADMISSION RATE
department_kpis["Admission_Rate"] = (

    department_kpis[
        "Total_Admissions"] / department_kpis["Total_Patient_Records"]) * 100
# ============================================================
# ROUND DEPARTMENT VALUES
department_kpis[
    "Average_Wait_Time"
] = department_kpis[
    "Average_Wait_Time"
].round(2)
department_kpis[
    "Average_Satisfaction"
] = department_kpis[
    "Average_Satisfaction"
].round(2)
department_kpis[
    "Patient_Flow_Efficiency"
] = department_kpis[
    "Patient_Flow_Efficiency"
].round(2)
department_kpis[
    "Department_Efficiency_Score"
] = department_kpis[
    "Department_Efficiency_Score"
].round(2)
department_kpis[
    "Admission_Rate"
] = department_kpis[
    "Admission_Rate"
].round(2)
# ============================================================
# KPI SUMMARY TABLE
kpi_summary = pd.DataFrame({

    "KPI": [

        "Total Admissions",

        "Admission Rate",

        "Average Patient Wait Time",

        "Average Patient Satisfaction",

        "Patient Flow Efficiency Rate",

        "Department Efficiency Score"
    ],


    "Value": [

        total_admissions,

        admission_rate,

        average_wait_time,

        average_satisfaction,

        patient_flow_efficiency_rate,

        department_efficiency_score
    ],


    "Unit": [

        "Patients",

        "%",

        "Minutes",

        "Score",

        "%",

        "Score (0-100)"
    ],


    "Calculation": [

        "Count of admitted patient records",

        "Total Admissions / Total Patient Records × 100",

        "Mean Patient Waittime",

        "Mean Patient Satisfaction Score",

        "(1 - Waittime Normalized) × 100",

        "(Satisfaction Normalized × 60%) + ((1 - Waittime Normalized) × 40%) × 100"
    ]
})


# ============================================================
# ROUND KPI SUMMARY
# ============================================================


kpi_summary["Value"] = (
    kpi_summary["Value"]
    .round(2)
)
# ============================================================
# FINAL DATA QUALITY CHECK
print("\n" + "=" * 70)
print("FINAL DATA QUALITY CHECK")
print("=" * 70)
print(
    "Rows:",
    df.shape[0]
)
print(
    "Columns:",
    df.shape[1]
)
print(
    "Missing values:",
    df.isna().sum().sum()
)
print(
    "Duplicate rows:",
    df.duplicated().sum()
)
# ============================================================
# EXPORT TO EXCEL
print("\n" + "-" * 70)
print("CREATING POWER BI-READY EXCEL FILE")
print("-" * 70)


with pd.ExcelWriter(
    OUTPUT_FILE,
    engine="openpyxl"
) as writer:


    # Patient-level dataset
    df.to_excel(

        writer,

        sheet_name="Patient_Data",

        index=False
    )


    # Department-level KPI table
    department_kpis.to_excel(

        writer,

        sheet_name="Department_KPIs",

        index=False
    )


    # Overall KPI summary
    kpi_summary.to_excel(

        writer,

        sheet_name="KPI_Summary",

        index=False
    )
# ============================================================
# FINAL OUTPUT
print("\n" + "=" * 70)
print("KPI ENGINEERING COMPLETED SUCCESSFULLY!")
print("=" * 70)


print("\nFinal KPI Results:")


print(
    f"1. Total Admissions              : "
    f"{total_admissions}"
)


print(
    f"2. Admission Rate                : "
    f"{admission_rate:.2f}%"
)


print(
    f"3. Average Patient Wait Time     : "
    f"{average_wait_time:.2f} minutes"
)


print(
    f"4. Average Patient Satisfaction  : "
    f"{average_satisfaction:.2f}"
)


print(
    f"5. Patient Flow Efficiency Rate  : "
    f"{patient_flow_efficiency_rate:.2f}%"
)


print(
    f"6. Department Efficiency Score   : "
    f"{department_efficiency_score:.2f}"
)


print("\nExcel file created:")

print(OUTPUT_FILE)


print("\nSheets:")

print("1. Patient_Data")
print("2. Department_KPIs")
print("3. KPI_Summary")


print("\nReady for Power BI!")