import pandas as pd
import numpy as np
from pathlib import Path


# ============================================================
# MEDTRACK_DV - MODULE 3
# HOSPITAL KPI ENGINEERING
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

INPUT_FILE = BASE_DIR / "hospital_cleaned.csv"
OUTPUT_FILE = BASE_DIR / "hospital_final_dataset.xlsx"


# ============================================================
# 1. LOAD CLEANED DATA
# ============================================================

print("=" * 70)
print("MEDTRACK_DV - MODULE 3")
print("HOSPITAL KPI ENGINEERING")
print("=" * 70)

if not INPUT_FILE.exists():
    raise FileNotFoundError(
        "hospital_cleaned.csv not found. "
        "Complete Module 2 first."
    )

df = pd.read_csv(INPUT_FILE)

print("\nCleaned dataset loaded successfully.")

print("Rows    :", len(df))
print("Columns :", len(df.columns))


# ============================================================
# 2. CONVERT DATE COLUMNS
# ============================================================

date_columns = [
    "admission_date",
    "discharge_date"
]

for column in date_columns:

    if column in df.columns:

        df[column] = pd.to_datetime(
            df[column],
            errors="coerce"
        )


# ============================================================
# 3. PREPARE LENGTH OF STAY
# ============================================================

if (
    "admission_date" in df.columns
    and "discharge_date" in df.columns
):

    df["length_of_stay_days"] = (
        df["discharge_date"]
        - df["admission_date"]
    ).dt.days


# ============================================================
# KPI 1
# TOTAL ADMISSIONS
# ============================================================

print("\nCalculating KPI 1: Total Admissions")

if "admission_id" in df.columns:

    total_admissions = df["admission_id"].nunique()

else:

    total_admissions = len(df)

print(
    "Total Admissions:",
    total_admissions
)


# ============================================================
# KPI 2
# AVERAGE LENGTH OF STAY
# ============================================================

print("\nCalculating KPI 2: Average Length of Stay")

valid_los = df[
    df["length_of_stay_days"].notna()
    & (df["length_of_stay_days"] >= 0)
]

average_length_of_stay = (
    valid_los["length_of_stay_days"]
    .mean()
)

print(
    "Average Length of Stay:",
    round(average_length_of_stay, 2),
    "days"
)


# ============================================================
# KPI 3
# READMISSION RATE
# ============================================================
#
# The HMIS dataset does not contain a direct readmission_flag.
#
# Therefore we identify readmissions using repeated
# patient admissions.
#
# If a patient has more than one admission record,
# the later admission is treated as a readmission.
# ============================================================

print("\nCalculating KPI 3: Readmission Rate")

if "patient_id" in df.columns:

    patient_admission_counts = (
        df.groupby("patient_id")
        .size()
    )

    readmitted_patients = (
        patient_admission_counts > 1
    ).sum()

    total_unique_patients = (
        df["patient_id"]
        .nunique()
    )

    if total_unique_patients > 0:

        readmission_rate = (
            readmitted_patients
            / total_unique_patients
        ) * 100

    else:

        readmission_rate = 0

else:

    readmitted_patients = 0
    total_unique_patients = 0
    readmission_rate = 0


print(
    "Readmitted Patients:",
    readmitted_patients
)

print(
    "Unique Patients:",
    total_unique_patients
)

print(
    "Readmission Rate:",
    round(readmission_rate, 2),
    "%"
)


# ============================================================
# CREATE READMISSION FLAG
# ============================================================

if "patient_id" in df.columns:

    df["readmission_flag"] = (
        df["patient_id"]
        .map(patient_admission_counts)
        .gt(1)
        .astype(int)
    )

else:

    df["readmission_flag"] = 0


# ============================================================
# KPI 4
# BED UTILIZATION RATE
# ============================================================

print("\nCalculating KPI 4: Bed Utilization Rate")

if "bed_status" in df.columns:

    occupied_statuses = [
        "occupied",
        "booked",
        "assigned"
    ]

    df["bed_occupied_flag"] = (
        df["bed_status"]
        .astype(str)
        .str.strip()
        .str.lower()
        .isin(occupied_statuses)
        .astype(int)
    )

else:

    df["bed_occupied_flag"] = 0


if "total_beds" in df.columns:

    total_beds = (
        pd.to_numeric(
            df["total_beds"],
            errors="coerce"
        )
    )

    average_beds = (
        total_beds
        .dropna()
        .mean()
    )

else:

    average_beds = 0


occupied_bed_records = (
    df["bed_occupied_flag"]
    .sum()
)


if len(df) > 0:

    bed_utilization_rate = (
        occupied_bed_records
        / len(df)
    ) * 100

else:

    bed_utilization_rate = 0


print(
    "Bed Utilization Rate:",
    round(bed_utilization_rate, 2),
    "%"
)


# ============================================================
# KPI 5
# OCCUPANCY RATE
# ============================================================
#
# For this admission-level dataset, occupancy is represented
# using occupied bed records against available bed records.
#
# This is a dashboard-level operational indicator.
# ============================================================

print("\nCalculating KPI 5: Occupancy Rate")


if "bed_occupied_flag" in df.columns:

    occupied_records = (
        df["bed_occupied_flag"]
        .sum()
    )

    total_bed_records = len(df)

    if total_bed_records > 0:

        occupancy_rate = (
            occupied_records
            / total_bed_records
        ) * 100

    else:

        occupancy_rate = 0

else:

    occupancy_rate = 0


print(
    "Occupancy Rate:",
    round(occupancy_rate, 2),
    "%"
)


# ============================================================
# KPI 6
# DEPARTMENT EFFICIENCY SCORE
# ============================================================
#
# The project specification requires this KPI but does not
# provide a fixed mathematical formula.
#
# We define a transparent score using:
#
# 40% Patient Volume Efficiency
# 30% Bed Utilization
# 30% Length-of-Stay Efficiency
#
# Higher score = better relative departmental efficiency.
# ============================================================

print(
    "\nCalculating KPI 6: Department Efficiency Score"
)


if "department_name" in df.columns:

    department_summary = (
        df.groupby("department_name")
        .agg(
            Total_Admissions=(
                "admission_id",
                "nunique"
            )
            if "admission_id" in df.columns
            else (
                "patient_id",
                "count"
            ),

            Average_Length_of_Stay=(
                "length_of_stay_days",
                "mean"
            ),

            Bed_Utilization=(
                "bed_occupied_flag",
                "mean"
            ),

            Readmission_Rate=(
                "readmission_flag",
                "mean"
            )
        )
        .reset_index()
    )


    # --------------------------------------------------------
    # Normalize admissions
    # --------------------------------------------------------

    max_admissions = (
        department_summary["Total_Admissions"]
        .max()
    )

    if max_admissions > 0:

        department_summary[
            "Admission_Efficiency"
        ] = (
            department_summary[
                "Total_Admissions"
            ]
            / max_admissions
        )

    else:

        department_summary[
            "Admission_Efficiency"
        ] = 0


    # --------------------------------------------------------
    # Normalize bed utilization
    # --------------------------------------------------------

    department_summary[
        "Bed_Utilization_Score"
    ] = (
        department_summary[
            "Bed_Utilization"
        ]
        .clip(0, 1)
    )


    # --------------------------------------------------------
    # Length-of-stay efficiency
    #
    # Lower LOS is treated as better efficiency.
    # --------------------------------------------------------

    max_los = (
        department_summary[
            "Average_Length_of_Stay"
        ]
        .max()
    )

    if max_los > 0:

        department_summary[
            "LOS_Efficiency"
        ] = 1 - (
            department_summary[
                "Average_Length_of_Stay"
            ]
            / max_los
        )

    else:

        department_summary[
            "LOS_Efficiency"
        ] = 0


    # --------------------------------------------------------
    # Final efficiency score
    # --------------------------------------------------------

    department_summary[
        "Department_Efficiency_Score"
    ] = (

        0.40
        * department_summary[
            "Admission_Efficiency"
        ]

        +

        0.30
        * department_summary[
            "Bed_Utilization_Score"
        ]

        +

        0.30
        * department_summary[
            "LOS_Efficiency"
        ]

    ) * 100


    department_summary[
        "Department_Efficiency_Score"
    ] = (
        department_summary[
            "Department_Efficiency_Score"
        ]
        .round(2)
    )

else:

    department_summary = pd.DataFrame()


# ============================================================
# HOSPITAL KPI SUMMARY
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

        round(
            occupancy_rate,
            2
        ),

        round(
            average_length_of_stay,
            2
        ),

        round(
            readmission_rate,
            2
        ),

        round(
            bed_utilization_rate,
            2
        ),

        round(
            department_summary[
                "Department_Efficiency_Score"
            ].mean(),
            2
        )
        if not department_summary.empty
        else 0

    ],

    "Unit": [

        "Admissions",

        "%",

        "Days",

        "%",

        "%",

        "Score / 100"

    ]

})


# ============================================================
# KPI DEFINITIONS
# ============================================================

kpi_definitions = pd.DataFrame({

    "KPI": [

        "Total Admissions",

        "Occupancy Rate",

        "Average Length of Stay",

        "Readmission Rate",

        "Bed Utilization Rate",

        "Department Efficiency Score"

    ],

    "Definition": [

        "Number of unique admission records.",

        "Percentage of admission records associated with occupied beds.",

        "Average number of days patients stay in the hospital.",

        "Percentage of unique patients who have more than one admission.",

        "Percentage of admission records associated with occupied beds.",

        "Department score based on admission efficiency, bed utilization and length-of-stay efficiency."

    ],

    "Calculation": [

        "COUNT(DISTINCT admission_id)",

        "Occupied bed records / total admission records × 100",

        "Average(discharge_date - admission_date)",

        "Patients with more than one admission / unique patients × 100",

        "Occupied bed records / total admission records × 100",

        "40% Admission Efficiency + 30% Bed Utilization + 30% LOS Efficiency"

    ]

})


# ============================================================
# MONTHLY KPI SUMMARY
# ============================================================

if (
    "admission_date" in df.columns
    and "length_of_stay_days" in df.columns
):

    monthly_kpi = (
        df.groupby(
            df["admission_date"]
            .dt.to_period("M")
        )
        .agg(
            Total_Admissions=(
                "admission_id",
                "nunique"
            ),

            Average_Length_of_Stay=(
                "length_of_stay_days",
                "mean"
            ),

            Readmission_Rate=(
                "readmission_flag",
                "mean"
            ),

            Bed_Utilization_Rate=(
                "bed_occupied_flag",
                "mean"
            )
        )
        .reset_index()
    )

    monthly_kpi["Admission_Month"] = (
        monthly_kpi[
            "admission_date"
        ]
        .astype(str)
    )

    monthly_kpi.drop(
        columns=["admission_date"],
        inplace=True
    )

    monthly_kpi[
        "Readmission_Rate"
    ] *= 100

    monthly_kpi[
        "Bed_Utilization_Rate"
    ] *= 100

    monthly_kpi[
        "Average_Length_of_Stay"
    ] = monthly_kpi[
        "Average_Length_of_Stay"
    ].round(2)

    monthly_kpi[
        "Readmission_Rate"
    ] = monthly_kpi[
        "Readmission_Rate"
    ].round(2)

    monthly_kpi[
        "Bed_Utilization_Rate"
    ] = monthly_kpi[
        "Bed_Utilization_Rate"
    ].round(2)

else:

    monthly_kpi = pd.DataFrame()


# ============================================================
# DEPARTMENT SUMMARY
# ============================================================

if not department_summary.empty:

    department_summary = (
        department_summary
        .sort_values(
            "Department_Efficiency_Score",
            ascending=False
        )
    )


# ============================================================
# SAVE FINAL EXCEL WORKBOOK
# ============================================================

print("\n" + "=" * 70)
print("CREATING FINAL KPI WORKBOOK")
print("=" * 70)


with pd.ExcelWriter(
    OUTPUT_FILE,
    engine="openpyxl"
) as writer:

    # Main cleaned + KPI fields
    df.to_excel(
        writer,
        sheet_name="Final_Dataset",
        index=False
    )

    # Six KPIs
    kpi_summary.to_excel(
        writer,
        sheet_name="KPI_Summary",
        index=False
    )

    # KPI definitions
    kpi_definitions.to_excel(
        writer,
        sheet_name="KPI_Definitions",
        index=False
    )

    # Department performance
    department_summary.to_excel(
        writer,
        sheet_name="Department_Analytics",
        index=False
    )

    # Monthly trends
    monthly_kpi.to_excel(
        writer,
        sheet_name="Monthly_KPIs",
        index=False
    )


# ============================================================
# FINAL OUTPUT
# ============================================================

print("\n" + "=" * 70)
print("MODULE 3 COMPLETED")
print("=" * 70)

print(
    f"Total Admissions           : {total_admissions:,}"
)

print(
    f"Occupancy Rate             : "
    f"{occupancy_rate:.2f}%"
)

print(
    f"Average Length of Stay     : "
    f"{average_length_of_stay:.2f} days"
)

print(
    f"Readmission Rate           : "
    f"{readmission_rate:.2f}%"
)

print(
    f"Bed Utilization Rate       : "
    f"{bed_utilization_rate:.2f}%"
)

if not department_summary.empty:

    print(
        "Department Efficiency Score: "
        f"{department_summary['Department_Efficiency_Score'].mean():.2f}"
    )

print("\nCreated:")
print(OUTPUT_FILE)

print("=" * 70)