import pandas as pd
import numpy as np
import os

# Ensure the data folder exists
os.makedirs('data', exist_ok=True)

# 1. patient.csv (Scaled to 10,000 patients)
num_patients = 10000
patients = pd.DataFrame({
    'Patient_ID': [f'P{str(i).zfill(5)}' for i in range(1, num_patients + 1)],
    'DOB': np.random.randint(1950, 2010, num_patients),
    'Nationality': np.random.choice(['India', 'USA', 'UK', 'UAE', 'Pakistan'], num_patients, p=[0.5, 0.1, 0.1, 0.2, 0.1]),
    'Gender': np.random.choice(['M', 'F'], num_patients)
})
patients.to_csv('data/patient.csv', index=False)

# 2. department.csv (Scaled to 50 doctors to handle 10k patients)
num_doctors = 50
departments = pd.DataFrame({
    'DoctorLicense': [f'DOC{str(i).zfill(3)}' for i in range(1, num_doctors + 1)],
    'DoctorName': [f'Doctor_{i}' for i in range(1, num_doctors + 1)],
    'Specialty': np.random.choice(['Cardiology', 'Emergency', 'Orthopaedics', 'General Surgery', 'Internal Medicine'], num_doctors),
    'Doctor_Type': np.random.choice(['Consultant', 'Specialist', 'GP'], num_doctors),
    'Doctor_Status': np.random.choice(['Active', 'Inactive'], num_doctors, p=[0.9, 0.1]),
    'CMI_Value': np.round(np.random.uniform(0.8, 1.5, num_doctors), 3)
})
departments.to_csv('data/department.csv', index=False)

# 3. ward.csv & bed.csv (Scaled capacity for a larger hospital)
wards = pd.DataFrame({
    'Ward_ID': [f'W{str(i).zfill(2)}' for i in range(1, 6)],
    'Specialty': ['Cardiology', 'Emergency', 'Orthopaedics', 'General Surgery', 'Internal Medicine'],
    'Capacity': [100, 150, 80, 120, 50]  # Total of 500 beds
})
wards.to_csv('data/ward.csv', index=False)

beds_data = []
for _, row in wards.iterrows():
    for b in range(1, row['Capacity'] + 1):
        beds_data.append({
            'Bed_ID': f"{row['Ward_ID']}-B{str(b).zfill(3)}", 
            'Ward_ID': row['Ward_ID'], 
            'Status': np.random.choice(['Occupied', 'Available'])
        })
beds = pd.DataFrame(beds_data)
beds.to_csv('data/bed.csv', index=False)

# 4. admission.csv (Scaled to 10,000 admissions)
num_admissions = 10000
admissions = pd.DataFrame({
    'Case_No': [f'123{str(i).zfill(5)}' for i in range(1, num_admissions + 1)],
    'Patient_ID': np.random.choice(patients['Patient_ID'], num_admissions), # Reusing patients to simulate return visits
    'DoctorLicense': np.random.choice(departments['DoctorLicense'], num_admissions),
    'Month': pd.date_range(start='2025-01-01', end='2025-12-31', periods=num_admissions).strftime('%Y-%m-%d'),
    'Insurance_Payer': np.random.choice(['PureWin Insurance', 'Nextcare Insurance', 'Self-Pay'], num_admissions),
    'Case_Type': np.random.choice(['IP', 'OP', 'DC'], num_admissions, p=[0.4, 0.5, 0.1]),
    'LOS': np.random.randint(0, 15, num_admissions),
    'Severity': np.random.randint(1, 4, num_admissions),
    'Revenue': np.round(np.random.uniform(500, 50000, num_admissions), 2)
})

# Set Length of Stay (LOS) to 0 for Outpatients (OP)
admissions.loc[admissions['Case_Type'] == 'OP', 'LOS'] = 0 
admissions.to_csv('data/admission.csv', index=False)

print(f"Success! Generated {num_patients} patients and {num_admissions} admissions.")