import pandas as pd
import os

raw_file = "data_collection/hospital_raw_data.csv"

if os.path.exists(raw_file):
    print("Raw dataset found successfully.")

    df = pd.read_csv(raw_file)

    print("\nDataset Shape:")
    print(df.shape)

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

else:
    print("Raw dataset not found. Please check the file path.")