import pandas as pd


# =====================================================
# Load Cleaned Dataset
# =====================================================

df = pd.read_excel(
    r"C:\Users\Shakshi\OneDrive\Desktop\Hospital_Analytics\hospital_cleaned.xlsx"
)


# =====================================================
# 1. Total Admissions
# =====================================================

total_admissions = df['Patient_ID'].nunique()

print("Total Admissions:", total_admissions)


# =====================================================
# 2. Occupancy Rate
# =====================================================

total_patient_days = df['Length_of_Stay'].sum()

available_bed_days = 100 * 365

occupancy_rate = (
    total_patient_days / available_bed_days
) * 100

print("Occupancy Rate (%):", occupancy_rate)


# =====================================================
# 3. Average Length of Stay
# =====================================================

avg_los = df['Length_of_Stay'].mean()

print("Average Length of Stay:", avg_los)


# =====================================================
# 4. Department Efficiency Score
# =====================================================

dept_efficiency = df.groupby('Department').apply(
    lambda x: (
        x['Patient_Satisfaction_Score'].mean()
        / x['Length_of_Stay'].mean()
    ) * x['Bill_Amount_INR'].mean()
)

print("\nDepartment Efficiency Score:")
print(dept_efficiency)


# =====================================================
# Create KPI DataFrame
# =====================================================

kpi_df = pd.DataFrame({
    'KPI': [
        'Total Admissions',
        'Occupancy Rate (%)',
        'Average Length of Stay'
    ],

    'Value': [
        total_admissions,
        occupancy_rate,
        avg_los
    ]
})


# =====================================================
# Save KPI Report
# =====================================================

kpi_path = (
    r"C:\Users\Shakshi\OneDrive\Desktop"
    r"\Hospital_Analytics\Hospital_KPI_Report.xlsx"
)

kpi_df.to_excel(
    kpi_path,
    index=False
)


# =====================================================
# Save Department Efficiency
# =====================================================

department_path = (
    r"C:\Users\Shakshi\OneDrive\Desktop"
    r"\Hospital_Analytics\Department_Efficiency.xlsx"
)

dept_efficiency.to_excel(
    department_path,
    header=['Efficiency Score']
)


print("\nKPI Report saved successfully!")
print("Department Efficiency Report saved successfully!")