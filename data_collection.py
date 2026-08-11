"""
Hospital Operations & Patient Analytics Dashboard
Module 1: Hospital Data Collection

This script collects/loads the raw hospital patient dataset and saves it
with the project-required filename: hospital_raw_data.csv.
"""

import pandas as pd
from pathlib import Path

# Input dataset
input_file = Path("ed_patient_data.csv")

# Output dataset required by the project
output_file = Path("hospital_raw_data.csv")

# Load the hospital patient dataset
df = pd.read_csv(input_file)

# Basic collection/integrity checks
print("Dataset loaded successfully.")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("Missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())

# Save the raw dataset without cleaning or transformation
df.to_csv(output_file, index=False)

print(f"Raw dataset saved as: {output_file}")
