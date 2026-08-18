import pandas as pd
import numpy as np

INPUT_FILE = "hospital_cleaned.csv"
OUTPUT_FILE = "hospital_final_dataset.xlsx"

df = pd.read_csv(INPUT_FILE)
df.columns = [
    str(c).strip().lower().replace(" ", "_").replace("-", "_")
    for c in df.columns
]

def find_col(names):
    for name in names:
        if name in df.columns:
            return name
    return None

department_col = find_col(["department", "department_name", "dept", "unit"])
los_col = find_col(["length_of_stay", "los", "lengthofstay", "stay_days"])
readmission_col = find_col([
    "readmission", "readmitted", "readmission_flag", "readmission_status"
])
occupancy_col = find_col([
    "occupancy_rate", "occupancy", "bed_occupancy_rate"
])
bed_col = find_col([
    "beds", "bed_count", "available_beds", "total_beds", "number_of_beds"
])

total_admissions = len(df)

if los_col:
    df[los_col] = pd.to_numeric(df[los_col], errors="coerce")
    average_los = df[los_col].mean()
else:
    average_los = np.nan

if readmission_col:
    readmitted = (
        df[readmission_col].astype(str).str.strip().str.lower()
        .isin(["yes", "y", "true", "1", "readmitted"])
    )
    readmission_rate = readmitted.mean() * 100
else:
    readmission_rate = np.nan

if occupancy_col:
    occupancy_rate = pd.to_numeric(
        df[occupancy_col], errors="coerce"
    ).mean()
else:
    occupancy_rate = np.nan

if bed_col and los_col:
    beds = pd.to_numeric(df[bed_col], errors="coerce")
    bed_utilization_rate = (
        df[los_col].sum() / (beds.sum() * max(1, len(df))) * 100
        if beds.sum() > 0 else np.nan
    )
else:
    bed_utilization_rate = occupancy_rate

if department_col:
    department_kpis = df.groupby(department_col).size().reset_index(
        name="Total Admissions"
    )
    department_kpis = department_kpis.rename(
        columns={department_col: "Department"}
    )

    if los_col:
        avg_los = df.groupby(department_col)[los_col].mean().reset_index()
        avg_los.columns = ["Department", "Average Length of Stay"]
        department_kpis = department_kpis.merge(
            avg_los, on="Department", how="left"
        )
    else:
        department_kpis["Average Length of Stay"] = np.nan

    if readmission_col:
        temp = df.copy()
        temp["_readmitted"] = (
            temp[readmission_col].astype(str).str.strip().str.lower()
            .isin(["yes", "y", "true", "1", "readmitted"])
        )
        rr = temp.groupby(department_col)["_readmitted"].mean().mul(100).reset_index()
        rr.columns = ["Department", "Readmission Rate"]
        department_kpis = department_kpis.merge(
            rr, on="Department", how="left"
        )
    else:
        department_kpis["Readmission Rate"] = np.nan

    los = department_kpis["Average Length of Stay"].fillna(
        department_kpis["Average Length of Stay"].median()
    )
    rr = department_kpis["Readmission Rate"].fillna(
        department_kpis["Readmission Rate"].median()
    )

    if los.max() != los.min():
        los_score = (los.max() - los) / (los.max() - los.min()) * 100
    else:
        los_score = pd.Series(100.0, index=department_kpis.index)

    if rr.max() != rr.min():
        rr_score = (rr.max() - rr) / (rr.max() - rr.min()) * 100
    else:
        rr_score = pd.Series(100.0, index=department_kpis.index)

    if occupancy_col:
        occ = df.groupby(department_col)[occupancy_col].mean().reindex(
            department_kpis["Department"]
        )
        if occ.max() != occ.min():
            occ_score = (occ - occ.min()) / (occ.max() - occ.min()) * 100
        else:
            occ_score = pd.Series(100.0, index=department_kpis.index)
    else:
        occ_score = pd.Series(100.0, index=department_kpis.index)

    department_kpis["Department Efficiency Score"] = (
        0.40 * np.asarray(los_score) +
        0.30 * np.asarray(rr_score) +
        0.30 * np.asarray(occ_score)
    ).round(2)
else:
    department_kpis = pd.DataFrame({
        "Department": ["All Departments"],
        "Total Admissions": [total_admissions],
        "Average Length of Stay": [average_los],
        "Readmission Rate": [readmission_rate],
        "Department Efficiency Score": [np.nan]
    })

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
        occupancy_rate,
        average_los,
        readmission_rate,
        bed_utilization_rate
    ],
    "Unit": ["Admissions", "%", "Days", "%", "%"]
})

with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Hospital Data", index=False)
    kpi_summary.to_excel(writer, sheet_name="Hospital KPIs", index=False)
    department_kpis.to_excel(writer, sheet_name="Department KPIs", index=False)

print("Created:", OUTPUT_FILE)