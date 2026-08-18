import pandas as pd
import numpy as np

# ============================================================
# FILES
# ============================================================

INPUT_FILE = "hospital_cleaned.csv"
OUTPUT_FILE = "hospital_final_dataset.xlsx"

# ============================================================
# LOAD DATASET
# ============================================================

df = pd.read_csv(INPUT_FILE)

# Clean column names
df.columns = [
    str(c).strip().lower().replace(" ", "_").replace("-", "_")
    for c in df.columns
]

# ============================================================
# FIND REQUIRED COLUMNS
# ============================================================

def find_col(names):
    for name in names:
        if name in df.columns:
            return name
    return None


admission_id_col = find_col([
    "admission_id",
    "admissionid",
    "admission_no",
    "admission_number"
])

patient_id_col = find_col([
    "patient_id",
    "patientid",
    "patient_no",
    "patient_number"
])

department_col = find_col([
    "department",
    "department_name",
    "dept",
    "unit"
])

los_col = find_col([
    "length_of_stay",
    "los",
    "lengthofstay",
    "stay_days"
])

readmission_col = find_col([
    "readmission",
    "readmitted",
    "readmission_flag",
    "readmission_status"
])

occupied_beds_col = find_col([
    "occupied_beds",
    "occupied_bed",
    "occupied"
])

available_beds_col = find_col([
    "available_beds",
    "available_bed",
    "beds_available"
])

# ============================================================
# CHECK REQUIRED COLUMNS
# ============================================================

print("Detected Columns:")
print("Admission ID       :", admission_id_col)
print("Patient ID         :", patient_id_col)
print("Department         :", department_col)
print("Length of Stay     :", los_col)
print("Readmission        :", readmission_col)
print("Occupied Beds      :", occupied_beds_col)
print("Available Beds     :", available_beds_col)

# ============================================================
# 1. TOTAL ADMISSIONS
# Formula:
# COUNT(UNIQUE Admission ID)
# ============================================================

if admission_id_col:
    total_admissions = df[admission_id_col].nunique()
else:
    # Fallback if Admission ID is unavailable
    total_admissions = len(df)

# ============================================================
# 2. OCCUPANCY RATE
# Formula:
# (Occupied Beds / Available Beds) × 100
# ============================================================

if occupied_beds_col and available_beds_col:

    occupied_beds = pd.to_numeric(
        df[occupied_beds_col],
        errors="coerce"
    ).sum()

    available_beds = pd.to_numeric(
        df[available_beds_col],
        errors="coerce"
    ).sum()

    if available_beds > 0:
        occupancy_rate = (
            occupied_beds / available_beds
        ) * 100
    else:
        occupancy_rate = np.nan

else:
    occupancy_rate = np.nan

# ============================================================
# 3. AVERAGE LENGTH OF STAY
# Formula:
# Total Days Spent / Total Unique Admissions
# ============================================================

if los_col:

    df[los_col] = pd.to_numeric(
        df[los_col],
        errors="coerce"
    )

    total_days_spent = df[los_col].sum()

    if total_admissions > 0:
        average_los = (
            total_days_spent / total_admissions
        )
    else:
        average_los = np.nan

else:
    total_days_spent = np.nan
    average_los = np.nan

# ============================================================
# 4. READMISSION RATE
# Formula:
# (Total Readmitted Patients / Total Unique Patients) × 100
# ============================================================

if readmission_col and patient_id_col:

    # Convert readmission values into True / False
    df["_readmitted"] = (
        df[readmission_col]
        .astype(str)
        .str.strip()
        .str.lower()
        .isin([
            "yes",
            "y",
            "true",
            "1",
            "readmitted"
        ])
    )

    # Find unique patients who were readmitted
    readmitted_patients = df.loc[
        df["_readmitted"],
        patient_id_col
    ].nunique()

    # Find total unique patients
    total_unique_patients = df[patient_id_col].nunique()

    if total_unique_patients > 0:

        readmission_rate = (
            readmitted_patients /
            total_unique_patients
        ) * 100

    else:
        readmission_rate = np.nan

else:
    readmitted_patients = np.nan
    total_unique_patients = np.nan
    readmission_rate = np.nan

# ============================================================
# 5. BED UTILIZATION RATE
# Formula:
# Bed Utilization Rate = Occupancy Rate
# ============================================================

bed_utilization_rate = occupancy_rate

# ============================================================
# 6. DEPARTMENT KPIs
# ============================================================

if department_col:

    # --------------------------------------------------------
    # Total Admissions by Department
    # --------------------------------------------------------

    if admission_id_col:

        department_kpis = (
            df.groupby(department_col)[admission_id_col]
            .nunique()
            .reset_index(name="Total Admissions")
        )

    else:

        department_kpis = (
            df.groupby(department_col)
            .size()
            .reset_index(name="Total Admissions")
        )

    department_kpis = department_kpis.rename(
        columns={
            department_col: "Department"
        }
    )

    # --------------------------------------------------------
    # Average Length of Stay by Department
    # --------------------------------------------------------

    if los_col:

        department_los = (
            df.groupby(department_col)[los_col]
            .sum()
            .reset_index(name="Total Days Spent")
        )

        if admission_id_col:

            department_admissions = (
                df.groupby(department_col)[admission_id_col]
                .nunique()
                .reset_index(name="Department Admissions")
            )

            department_los = department_los.merge(
                department_admissions,
                on=department_col,
                how="left"
            )

            department_los["Average Length of Stay"] = (
                department_los["Total Days Spent"] /
                department_los["Department Admissions"]
            )

        else:

            department_los["Average Length of Stay"] = (
                department_los["Total Days Spent"] /
                department_kpis["Total Admissions"]
            )

        department_los = department_los.rename(
            columns={
                department_col: "Department"
            }
        )

        department_kpis = department_kpis.merge(
            department_los[
                ["Department", "Average Length of Stay"]
            ],
            on="Department",
            how="left"
        )

    else:

        department_kpis["Average Length of Stay"] = np.nan

    # --------------------------------------------------------
    # Readmission Rate by Department
    # --------------------------------------------------------

    if readmission_col and patient_id_col:

        temp = df.copy()

        temp["_readmitted"] = (
            temp[readmission_col]
            .astype(str)
            .str.strip()
            .str.lower()
            .isin([
                "yes",
                "y",
                "true",
                "1",
                "readmitted"
            ])
        )

        # Unique patients in each department
        department_patients = (
            temp.groupby(department_col)[patient_id_col]
            .nunique()
            .reset_index(
                name="Unique Patients"
            )
        )

        # Unique readmitted patients in each department
        department_readmitted = (
            temp[temp["_readmitted"]]
            .groupby(department_col)[patient_id_col]
            .nunique()
            .reset_index(
                name="Readmitted Patients"
            )
        )

        department_readmission = department_patients.merge(
            department_readmitted,
            on=department_col,
            how="left"
        )

        department_readmission["Readmitted Patients"] = (
            department_readmission["Readmitted Patients"]
            .fillna(0)
        )

        department_readmission["Readmission Rate"] = (
            department_readmission["Readmitted Patients"] /
            department_readmission["Unique Patients"]
        ) * 100

        department_readmission = department_readmission.rename(
            columns={
                department_col: "Department"
            }
        )

        department_kpis = department_kpis.merge(
            department_readmission[
                ["Department", "Readmission Rate"]
            ],
            on="Department",
            how="left"
        )

    else:

        department_kpis["Readmission Rate"] = np.nan

    # ========================================================
    # DEPARTMENT EFFICIENCY SCORE
    #
    # Lower Readmission Rate = Higher Efficiency
    # Higher Readmission Rate = Lower Efficiency
    #
    # Score:
    # Lowest Readmission Rate -> 100
    # Highest Readmission Rate -> 0
    # ========================================================

    rr = department_kpis[
        "Readmission Rate"
    ].copy()

    if rr.notna().any():

        min_rr = rr.min()
        max_rr = rr.max()

        if max_rr != min_rr:

            department_efficiency_score = (
                (max_rr - rr) /
                (max_rr - min_rr)
            ) * 100

        else:

            # If all departments have the same
            # readmission rate
            department_efficiency_score = pd.Series(
                100.0,
                index=department_kpis.index
            )

        department_kpis[
            "Department Efficiency Score"
        ] = department_efficiency_score.round(2)

    else:

        department_kpis[
            "Department Efficiency Score"
        ] = np.nan

else:

    department_kpis = pd.DataFrame({
        "Department": ["All Departments"],
        "Total Admissions": [total_admissions],
        "Average Length of Stay": [average_los],
        "Readmission Rate": [readmission_rate],
        "Department Efficiency Score": [np.nan]
    })

# ============================================================
# 7. KPI SUMMARY
# ============================================================

kpi_summary = pd.DataFrame({

    "KPI": [
        "Total Admissions",
        "Occupancy Rate",
        "Average Length of Stay",
        "Readmission Rate",
        "Bed Utilization Rate"
    ],

    "Value": [
        total_admissions,
        round(occupancy_rate, 2)
        if not pd.isna(occupancy_rate)
        else np.nan,

        round(average_los, 2)
        if not pd.isna(average_los)
        else np.nan,

        round(readmission_rate, 2)
        if not pd.isna(readmission_rate)
        else np.nan,

        round(bed_utilization_rate, 2)
        if not pd.isna(bed_utilization_rate)
        else np.nan
    ],

    "Unit": [
        "Admissions",
        "%",
        "Days",
        "%",
        "%"
    ]
})

# ============================================================
# 8. SAVE FINAL EXCEL FILE
# ============================================================

# Remove temporary column before saving
if "_readmitted" in df.columns:
    df = df.drop(columns=["_readmitted"])

with pd.ExcelWriter(
    OUTPUT_FILE,
    engine="openpyxl"
) as writer:

    df.to_excel(
        writer,
        sheet_name="Hospital Data",
        index=False
    )

    kpi_summary.to_excel(
        writer,
        sheet_name="Hospital KPIs",
        index=False
    )

    department_kpis.to_excel(
        writer,
        sheet_name="Department KPIs",
        index=False
    )

# ============================================================
# 9. DISPLAY RESULTS
# ============================================================

print("\n========================================")
print("HOSPITAL KPI RESULTS")
print("========================================")

print("Total Admissions       :", total_admissions)
print("Occupancy Rate         :", occupancy_rate, "%")
print("Average Length of Stay :", average_los, "days")
print("Readmission Rate       :", readmission_rate, "%")
print("Bed Utilization Rate   :", bed_utilization_rate, "%")

print("\nCreated:", OUTPUT_FILE)