import pandas as pd
import numpy as np
import os

INPUT_FILE = "input/Hospital Patient Management System cleaned.csv"
OUTPUT_FILE = "output/hospital_final_dataset.xlsx"

os.makedirs("output", exist_ok=True)

# ---------- LOAD ----------
df = pd.read_csv(INPUT_FILE, encoding="utf-8-sig")

# Fix files that were accidentally read as one giant column
if len(df.columns) == 1:
    with open(INPUT_FILE, "r", encoding="utf-8-sig") as f:
        lines = [line.strip() for line in f if line.strip()]
    header = lines[0].split(",")
    rows = [
        line.split(",")
        for line in lines[1:]
        if len(line.split(",")) == len(header)
    ]
    df = pd.DataFrame(rows, columns=header)

# ---------- CLEAN ----------
df.columns = (
    df.columns.astype(str).str.strip().str.lower()
    .str.replace(" ", "_", regex=False)
)

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].astype(str).str.strip()
    df[col] = df[col].replace(
        {"": np.nan, "nan": np.nan, "None": np.nan, "NULL": np.nan}
    )

for col in ["admission_date", "discharge_date", "date_of_birth", "registration_date"]:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")

for col in ["age", "total_bill", "capacity", "daily_rate", "floor", "staff_count"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# ---------- LENGTH OF STAY ----------
if "admission_date" in df.columns and "discharge_date" in df.columns:
    df["length_of_stay"] = (
        df["discharge_date"] - df["admission_date"]
    ).dt.days
    df.loc[df["length_of_stay"] < 0, "length_of_stay"] = np.nan

# ---------- READMISSION ----------
patient_col = "patient_id" if "patient_id" in df.columns else None
admission_col = "admission_id" if "admission_id" in df.columns else None

if patient_col:
    patient_admission_count = df.groupby(patient_col)[patient_col].transform("count")
    df["readmission_flag"] = (patient_admission_count > 1).astype(int)
else:
    df["readmission_flag"] = 0

# ---------- OCCUPANCY ----------
# A patient is considered occupying a bed if their admission is active
# or they have no discharge date.
status_col = next(
    (c for c in ["admission_status", "status", "patient_status"] if c in df.columns),
    None
)

if status_col:
    status = df[status_col].astype(str).str.lower()
    df["occupied_flag"] = status.str.contains(
        "admit|inpatient|occupied|active", regex=True, na=False
    ).astype(int)
elif "discharge_date" in df.columns:
    df["occupied_flag"] = df["discharge_date"].isna().astype(int)
else:
    df["occupied_flag"] = 0

# ---------- DEPARTMENT EFFICIENCY ----------
dept_col = next(
    (c for c in ["department_name", "department"] if c in df.columns),
    None
)

if dept_col:
    aggregation = {
        "admissions": (admission_col, "count")
        if admission_col else (dept_col, "size")
    }

    if "length_of_stay" in df.columns:
        aggregation["average_los"] = ("length_of_stay", "mean")

    if "total_bill" in df.columns:
        aggregation["total_bill"] = ("total_bill", "sum")

    dept = df.groupby(dept_col, dropna=False).agg(**aggregation).reset_index()

    # Higher admissions = better throughput score.
    dept["admission_score"] = (
        dept["admissions"] / dept["admissions"].max() * 100
    )

    # Lower LOS = better efficiency score.
    if "average_los" in dept.columns:
        los_range = dept["average_los"].max() - dept["average_los"].min()

        if los_range == 0:
            dept["los_score"] = 100
        else:
            dept["los_score"] = (
                1 -
                (dept["average_los"] - dept["average_los"].min()) /
                los_range
            ) * 100
    else:
        dept["los_score"] = 100

    # 50% throughput + 50% LOS efficiency
    dept["department_efficiency_score"] = (
        0.50 * dept["admission_score"] +
        0.50 * dept["los_score"]
    ).round(2)

    efficiency_map = dept.set_index(dept_col)["department_efficiency_score"]

    df["department_efficiency_score"] = df[dept_col].map(efficiency_map)

else:
    dept = pd.DataFrame()
    df["department_efficiency_score"] = np.nan

# ---------- KPI CALCULATIONS ----------
total_admissions = len(df)

unique_patients = (
    df[patient_col].nunique()
    if patient_col
    else len(df)
)

average_length_of_stay = (
    df["length_of_stay"].mean()
    if "length_of_stay" in df.columns
    else np.nan
)

readmission_rate = (
    df["readmission_flag"].mean() * 100
    if len(df)
    else 0
)

# ---------- BED UTILIZATION / OCCUPANCY ----------
if "capacity" in df.columns and df["capacity"].notna().any():

    total_bed_capacity = df["capacity"].sum()
    occupied_beds = df["occupied_flag"].sum()

    bed_utilization_rate = (
        occupied_beds / total_bed_capacity * 100
        if total_bed_capacity > 0
        else np.nan
    )

    occupancy_rate = bed_utilization_rate

else:
    # Do not invent a denominator if the dataset has no usable capacity.
    occupied_beds = df["occupied_flag"].sum()
    total_bed_capacity = np.nan
    bed_utilization_rate = np.nan
    occupancy_rate = np.nan

# ---------- KPI TABLE ----------
kpi_summary = pd.DataFrame({
    "KPI": [
        "Total Admissions",
        "Unique Patients",
        "Occupancy Rate (%)",
        "Average Length of Stay (Days)",
        "Readmission Rate (%)",
        "Bed Utilization Rate (%)",
        "Average Department Efficiency Score"
    ],
    "Value": [
        total_admissions,
        unique_patients,
        round(occupancy_rate, 2) if pd.notna(occupancy_rate) else np.nan,
        round(average_length_of_stay, 2)
        if pd.notna(average_length_of_stay) else np.nan,
        round(readmission_rate, 2),
        round(bed_utilization_rate, 2)
        if pd.notna(bed_utilization_rate) else np.nan,
        round(df["department_efficiency_score"].mean(), 2)
        if df["department_efficiency_score"].notna().any()
        else np.nan
    ]
})

# ---------- TABLEAU-FRIENDLY OUTPUT ----------
# Replace remaining categorical nulls with "Unknown".
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].fillna("Unknown")

# ---------- EXCEL ----------
with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:

    df.to_excel(
        writer,
        sheet_name="Hospital_Data",
        index=False
    )

    kpi_summary.to_excel(
        writer,
        sheet_name="Hospital_KPIs",
        index=False
    )

    if not dept.empty:
        dept.to_excel(
            writer,
            sheet_name="Department_KPIs",
            index=False
        )

print("=" * 70)
print("MODULE 3: HOSPITAL KPI ENGINEERING")
print("=" * 70)
print("\nKPI RESULTS")
print(kpi_summary.to_string(index=False))
print("\nCreated:", OUTPUT_FILE)
