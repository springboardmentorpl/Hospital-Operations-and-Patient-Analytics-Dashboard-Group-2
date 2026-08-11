import pandas as pd

print("Loading individual datasets...")
patients = pd.read_csv('data/patient.csv')
admissions = pd.read_csv('data/admission.csv')
departments = pd.read_csv('data/department.csv')

print("Integrating data...")
merged_df = pd.merge(admissions, patients, on='Patient_ID', how='left')

final_integrated_data = pd.merge(merged_df, departments, on='DoctorLicense', how='left')

final_integrated_data = final_integrated_data.drop(columns=['Patient_ID'])

output_path = 'data/hospital_raw_data.csv'
final_integrated_data.to_csv(output_path, index=False)

print("\nHospital raw data saved successfully.")