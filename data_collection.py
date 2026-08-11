from pathlib import Path
import pandas as pd

# Original dataset downloaded manually from the public source.
SOURCE_FILE = "healthcare_analytics_patient_flow_data.csv"
OUTPUT_FILE = "hospital_raw_data.csv"

source_path = Path(SOURCE_FILE)

if not source_path.exists():
    raise FileNotFoundError(
        f"{SOURCE_FILE} not found. Place the originally downloaded dataset "
        "in this folder before running this script."
    )

df = pd.read_csv(source_path)

# Save a consistent raw-data copy for the project
df.to_csv(OUTPUT_FILE, index=False)

print("Raw data collection completed.")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")
print(f"Saved as: {OUTPUT_FILE}")