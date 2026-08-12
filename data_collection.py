import pandas as pd

# Load the raw hospital dataset
raw_data = pd.read_csv("hospital_raw_data.csv")

print("Raw hospital dataset loaded successfully!")

print("\nDataset Shape:")
print(raw_data.shape)

print("\nFirst 5 Records:")
print(raw_data.head())

print("\nData Types:")
print(raw_data.dtypes)

print("\nMissing Values:")
print(raw_data.isnull().sum())

print("\nDuplicate Rows:")
print(raw_data.duplicated().sum())