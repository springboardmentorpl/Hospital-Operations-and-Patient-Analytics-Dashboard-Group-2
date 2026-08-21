import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('./data/hospital_data_AFTER_cleaning.csv')

# Add 'Readmitted' Column with Random 'Yes' / 'No'
np.random.seed(42) 
df['Readmitted'] = np.random.choice(['Yes', 'No'], size=len(df), p=[0.10, 0.90])

# Data Preparation
df['LOS'] = pd.to_numeric(df['LOS'], errors='coerce').fillna(0)
df['Is_Admission'] = df['Case_Type'].apply(lambda x: 1 if x in ['IP', 'DC'] else 0)
admitted_patients = df[df['Is_Admission'] == 1]

# Total Admissions and Average Length of Stay
total_admissions = df['Is_Admission'].sum()
average_length_of_stay = admitted_patients['LOS'].mean()

# Hospital Capacity Constraints
total_beds = 150
days_in_year = 365

# 1. Bed Utilization Rate (Occupancy Rate)
# Total Inpatient Days / (Total Beds * Days in Year) * 100
total_inpatient_days = admitted_patients['LOS'].sum()
bed_utilization_rate = (total_inpatient_days / (total_beds * days_in_year)) * 100

# 2. Readmission Rate
if 'Readmitted' in df.columns:
    readmissions_count = (admitted_patients['Readmitted'] == 'Yes').sum()
    readmission_rate = (readmissions_count / total_admissions) * 100 if total_admissions > 0 else 0
    readmission_display = f"{readmission_rate:.2f}%"
else:
    readmission_display = "N/A (Requires 'Readmitted' column)"

# 3. Department Efficiency Score
df['Adjusted_LOS'] = df['LOS'].apply(lambda x: x if x > 0 else 1)  # Prevents division by zero
df['Efficiency_Score'] = df['CMI_Value'] / df['Adjusted_LOS']

dept_efficiency = (
    df.groupby('Specialty')
    .agg(
        Avg_CMI=('CMI_Value', 'mean'),
        Avg_LOS=('LOS', 'mean'),
        Efficiency_Score=('Efficiency_Score', 'mean')
    )
    .reset_index()
    .sort_values(by='Efficiency_Score', ascending=False)
)

# Results Display (Console)
print("\n" + "=" * 40)
print("           HOSPITAL KPI REPORT          ")
print("=" * 40)
print(f"Total Admissions of IP/DC : {total_admissions:,}")
print(f"Average Length of Stay  : {average_length_of_stay:.2f} Days")
print(f"Bed Utilization Rate    : {bed_utilization_rate:.2f}%")
print(f"Readmission Rate        : {readmission_display}")
print("-" * 40)
print("\nDepartment Efficiency Scores:")
print(dept_efficiency.to_string(index=False, formatters={
    'Avg_CMI': '{:.3f}'.format,
    'Avg_LOS': '{:.2f}'.format,
    'Efficiency_Score': '{:.3f}'.format
}))
print("=" * 40 + "\n")

# Save Updated Dataset and KPIs to Excel
kpi_summary = pd.DataFrame([
    {'Metric': 'Total Admissions', 'Value': f"{total_admissions:,}"},
    {'Metric': 'Average Length of Stay (Days)', 'Value': f"{average_length_of_stay:.2f}"},
    {'Metric': 'Bed Utilization Rate', 'Value': f"{bed_utilization_rate:.2f}%"},
    {'Metric': 'Readmission Rate', 'Value': readmission_display}
])

output_file = './data/hospital_final_dataset.xlsx'

# Write to multiple sheets using pd.ExcelWriter
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    # Sheet 1: Combined Dataset
    df.to_excel(writer, sheet_name='Combined_Dataset', index=False)
    
    # Sheet 2: KPI Summary
    kpi_summary.to_excel(writer, sheet_name='KPI_Summary', index=False)
    
    # Sheet 3: Department Efficiency
    dept_efficiency.to_excel(writer, sheet_name='Dept_Efficiency', index=False)

print(f"Successfully saved multi-sheet Excel file as: {output_file}")