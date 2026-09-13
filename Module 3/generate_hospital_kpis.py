from pathlib import Path
import pandas as pd
import numpy as np



INPUT_FILE = "cleaned_healthcare_patient_flow_data (7).csv"
OUTPUT_CSV = INPUT_FILE
OUTPUT_EXCEL = "hospital_final_dataset.xlsx"


rng = np.random.default_rng(42)


if not Path(INPUT_FILE).exists():
    raise FileNotFoundError(
        f"Cannot find '{INPUT_FILE}'. Keep the CSV and Python file in the same folder."
    )

df = pd.read_csv(INPUT_FILE)

df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_", regex=False)
    .str.replace(r"[^a-z0-9_]", "", regex=True)
)

df["patient_admission_date"] = pd.to_datetime(
    df["patient_admission_date"],
    errors="coerce",
)

df["patient_admission_date"] = df["patient_admission_date"].fillna(
    df["patient_admission_date"].mode()[0]
)

df["patient_admission_flag"] = (
    df["patient_admission_flag"]
    .astype(str)
    .str.strip()
    .str.lower()
)

df["department_referral"] = (
    df["department_referral"]
    .astype(str)
    .str.strip()
    .str.title()
)

df["patient_waittime"] = pd.to_numeric(
    df["patient_waittime"],
    errors="coerce",
).fillna(df["patient_waittime"].median())

df["patient_satisfaction_score"] = pd.to_numeric(
    df["patient_satisfaction_score"],
    errors="coerce",
).fillna(df["patient_satisfaction_score"].median())


old_kpi_columns = [
    "synthetic_length_of_stay_days",
    "length_of_stay_days",
    "patient_discharge_date",
    "total_beds",
    "occupied_beds",
    "is_readmitted",
    "department_efficiency_score",
    "kpi_data_note",
]

df = df.drop(
    columns=[column for column in old_kpi_columns if column in df.columns],
    errors="ignore",
)


admission_mask = df["patient_admission_flag"] == "admission"

if admission_mask.sum() == 0:
    raise ValueError(
        "No admission records found. Check patient_admission_flag values."
    )


df["length_of_stay_days"] = 0

df.loc[admission_mask, "length_of_stay_days"] = rng.integers(
    low=1,
    high=11,
    size=admission_mask.sum(),
)

df["length_of_stay_days"] = df["length_of_stay_days"].astype(int)


df["patient_discharge_date"] = (
    df["patient_admission_date"]
    + pd.to_timedelta(df["length_of_stay_days"], unit="D")
)


df["total_beds"] = 200


daily_bed_data = pd.DataFrame(
    {
        "patient_admission_date": (
            df["patient_admission_date"]
            .drop_duplicates()
            .sort_values()
        )
    }
)

daily_bed_data["occupied_beds"] = rng.integers(
    low=130,
    high=181,
    size=len(daily_bed_data),
)

df = df.merge(
    daily_bed_data,
    on="patient_admission_date",
    how="left",
)

df["occupied_beds"] = df["occupied_beds"].fillna(150).astype(int)


df["is_readmitted"] = 0

df.loc[admission_mask, "is_readmitted"] = (
    rng.random(admission_mask.sum()) < 0.08
).astype(int)


total_admissions = int(admission_mask.sum())


occupancy_rate = round(
    (
        daily_bed_data["occupied_beds"].sum()
        / (len(daily_bed_data) * 200)
    )
    * 100,
    2,
)


average_length_of_stay = round(
    df.loc[admission_mask, "length_of_stay_days"].mean(),
    2,
)


readmission_rate = round(
    df.loc[admission_mask, "is_readmitted"].mean() * 100,
    2,
)


bed_utilization_rate = occupancy_rate


department_summary = (
    df.groupby("department_referral")
    .agg(
        Patient_Volume=("patient_id", "count"),
        Average_Wait_Time=("patient_waittime", "mean"),
        Average_Satisfaction=("patient_satisfaction_score", "mean"),
    )
    .reset_index()
)

def min_max_score(series, higher_is_better=True):
    if series.max() == series.min():
        return pd.Series(100.0, index=series.index)

    score = (
        (series - series.min())
        / (series.max() - series.min())
        * 100
    )

    return score if higher_is_better else 100 - score


department_summary["Volume_Score"] = min_max_score(
    department_summary["Patient_Volume"],
    higher_is_better=True,
)

department_summary["Wait_Time_Score"] = min_max_score(
    department_summary["Average_Wait_Time"],
    higher_is_better=False,
)

department_summary["Satisfaction_Score"] = min_max_score(
    department_summary["Average_Satisfaction"],
    higher_is_better=True,
)

department_summary["Department_Efficiency_Score"] = (
    department_summary["Volume_Score"] * 0.30
    + department_summary["Wait_Time_Score"] * 0.30
    + department_summary["Satisfaction_Score"] * 0.40
).round(2)


df = df.merge(
    department_summary[
        ["department_referral", "Department_Efficiency_Score"]
    ],
    on="department_referral",
    how="left",
)

df = df.rename(
    columns={
        "Department_Efficiency_Score": "department_efficiency_score"
    }
)


kpi_summary = pd.DataFrame(
    {
        "KPI": [
            "Total Admissions",
            "Occupancy Rate (%)",
            "Average Length of Stay (Days)",
            "Readmission Rate (%)",
            "Bed Utilization Rate (%)",
        ],
        "Value": [
            total_admissions,
            occupancy_rate,
            average_length_of_stay,
            readmission_rate,
            bed_utilization_rate,
        ],
        "Formula / Method": [
            "Count of records where patient_admission_flag = admission",
            "Average daily occupied beds / total beds x 100",
            "Average of patient_discharge_date - patient_admission_date",
            "Readmitted admitted patients / total admitted patients x 100",
            "Average daily occupied beds / total beds x 100",
        ],
    }
)


assumptions = pd.DataFrame(
    {
        "Field / KPI": [
            "patient_discharge_date",
            "length_of_stay_days",
            "total_beds",
            "occupied_beds",
            "is_readmitted",
            "department_efficiency_score",
        ],
        "Description": [
            "Generated by adding length_of_stay_days to patient_admission_date.",
            "Generated from 1 to 10 days for admitted patients.",
            "Assumed hospital capacity of 200 beds for KPI demonstration.",
            "Generated once per admission date from 130 to 180 beds.",
            "Generated at an 8% rate for admitted patients.",
            "40% satisfaction + 30% lower wait time + 30% patient volume.",
        ],
    }
)


df["patient_discharge_date"] = pd.to_datetime(
    df["patient_discharge_date"]
).dt.strftime("%Y-%m-%d")

df["department_efficiency_score"] = (
    df["department_efficiency_score"]
    .fillna(0)
    .round(2)
)


df.to_csv(OUTPUT_CSV, index=False)


with pd.ExcelWriter(OUTPUT_EXCEL, engine="openpyxl") as writer:
    kpi_summary.to_excel(writer, sheet_name="KPI Summary", index=False)
    department_summary.to_excel(
        writer,
        sheet_name="Department Efficiency",
        index=False,
    )
    df.to_excel(
        writer,
        sheet_name="Final Patient Dataset",
        index=False,
    )
    daily_bed_data.to_excel(
        writer,
        sheet_name="Daily Bed Capacity",
        index=False,
    )
    assumptions.to_excel(
        writer,
        sheet_name="Data Dictionary",
        index=False,
    )

print("Module 3 KPI engineering completed successfully.")
print(f"Updated merged dataset: {OUTPUT_CSV}")
print(f"Excel deliverable created: {OUTPUT_EXCEL}")
print("\nKPI Summary:")
print(kpi_summary.to_string(index=False))