import pandas as pd
import os

# --------------------------------------------------
# 1. Load cleaned hospital dataset
# --------------------------------------------------

input_file = "data/hospital_cleaned.csv"
output_file = "data/hospital_final_dataset.xlsx"

df = pd.read_csv(input_file)

print("Cleaned dataset loaded successfully.")
print("Shape:", df.shape)


# --------------------------------------------------
# 2. Calculate Hospital KPIs
# --------------------------------------------------

# Total Admissions
# In this dataset, IP represents inpatient admissions.
total_admissions = (df["Case type"] == "IP").sum()


# Average Length of Stay
average_los = df["LOS"].mean()


# Total Cases
total_cases = len(df)


# Total Revenue
total_revenue = df["Revenue"].sum()


# Average Revenue
average_revenue = df["Revenue"].mean()


# Discharge Before 12 PM Rate
discharge_before_12pm_rate = (
    (df["Discharge Before 12PM"] == "Yes").mean() * 100
)


# --------------------------------------------------
# 3. KPI Summary
# --------------------------------------------------

kpi_summary = pd.DataFrame({
    "KPI": [
        "Total Cases",
        "Total Admissions",
        "Average Length of Stay",
        "Total Revenue",
        "Average Revenue",
        "Discharge Before 12PM Rate",
        "Occupancy Rate",
        "Readmission Rate",
        "Bed Utilization Rate",
        "Department Efficiency Score"
    ],

    "Value": [
        total_cases,
        total_admissions,
        round(average_los, 2),
        round(total_revenue, 2),
        round(average_revenue, 2),
        round(discharge_before_12pm_rate, 2),
        "Not Available",
        "Not Available",
        "Not Available",
        "Not Available"
    ],

    "Status": [
        "Calculated",
        "Calculated",
        "Calculated",
        "Calculated",
        "Calculated",
        "Calculated",
        "Requires bed/capacity data",
        "Requires patient readmission data",
        "Requires bed data",
        "Requires department-specific capacity/efficiency data"
    ]
})


# --------------------------------------------------
# 4. Monthly KPI Summary
# --------------------------------------------------

df["Month"] = pd.to_datetime(df["Month"], errors="coerce")

monthly_kpis = (
    df.groupby(df["Month"].dt.to_period("M"))
    .agg(
        Total_Cases=("Case_No", "count"),
        Admissions=("Case type", lambda x: (x == "IP").sum()),
        Average_LOS=("LOS", "mean"),
        Total_Revenue=("Revenue", "sum")
    )
    .reset_index()
)

monthly_kpis["Month"] = monthly_kpis["Month"].astype(str)

monthly_kpis["Average_LOS"] = monthly_kpis["Average_LOS"].round(2)
monthly_kpis["Total_Revenue"] = monthly_kpis["Total_Revenue"].round(2)


# --------------------------------------------------
# 5. Specialty KPI Summary
# --------------------------------------------------

specialty_kpis = (
    df.groupby("Specialty")
    .agg(
        Total_Cases=("Case_No", "count"),
        Total_Revenue=("Revenue", "sum"),
        Average_LOS=("LOS", "mean"),
        Average_CMI=("CMI Value", "mean")
    )
    .reset_index()
)

specialty_kpis["Total_Revenue"] = specialty_kpis["Total_Revenue"].round(2)
specialty_kpis["Average_LOS"] = specialty_kpis["Average_LOS"].round(2)
specialty_kpis["Average_CMI"] = specialty_kpis["Average_CMI"].round(3)


# --------------------------------------------------
# 6. Case Type KPI Summary
# --------------------------------------------------

case_type_kpis = (
    df.groupby("Case type")
    .agg(
        Total_Cases=("Case_No", "count"),
        Average_LOS=("LOS", "mean"),
        Total_Revenue=("Revenue", "sum")
    )
    .reset_index()
)

case_type_kpis["Average_LOS"] = case_type_kpis["Average_LOS"].round(2)
case_type_kpis["Total_Revenue"] = case_type_kpis["Total_Revenue"].round(2)


# --------------------------------------------------
# 7. Save final Excel workbook
# --------------------------------------------------

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:

    # Complete cleaned dataset
    df.to_excel(
        writer,
        sheet_name="Final Dataset",
        index=False
    )

    # Main KPI summary
    kpi_summary.to_excel(
        writer,
        sheet_name="KPI Summary",
        index=False
    )

    # Monthly KPIs
    monthly_kpis.to_excel(
        writer,
        sheet_name="Monthly KPIs",
        index=False
    )

    # Specialty KPIs
    specialty_kpis.to_excel(
        writer,
        sheet_name="Specialty KPIs",
        index=False
    )

    # Case Type KPIs
    case_type_kpis.to_excel(
        writer,
        sheet_name="Case Type KPIs",
        index=False
    )


print("\nKPI calculation completed successfully.")
print("Total Cases:", total_cases)
print("Total Admissions:", total_admissions)
print("Average LOS:", round(average_los, 2))
print("Total Revenue:", round(total_revenue, 2))
print("Average Revenue:", round(average_revenue, 2))
print("Discharge Before 12PM Rate:", round(discharge_before_12pm_rate, 2), "%")

print("\nFinal file created:")
print(output_file)