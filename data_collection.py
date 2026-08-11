import pandas as pd
from pathlib import Path


# ==========================================
# Hospital Data Collection
# ==========================================

# Project paths
RAW_DATA_PATH = Path("Hospital ER_Raw_Data.csv")


def load_hospital_data(file_path):

    df = pd.read_csv(file_path)

    print("Hospital dataset loaded successfully!")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])

    return df

def inspect_dataset(df):
    """
    Perform basic validation of the collected dataset.
    """
    print("\n--- Dataset Information ---")
    print("Shape:", df.shape)

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nFirst 5 Records:")
    print(df.head())


def calculate_completeness(df):
    """
    Calculate dataset completeness percentage.
    """
    total_cells = df.size
    missing_cells = df.isnull().sum().sum()

    completeness = (
        (total_cells - missing_cells) / total_cells
    ) * 100

    print(f"\nDataset Completeness: {completeness:.2f}%")

    return completeness


# ==========================================
# Main Program
# ==========================================

if __name__ == "__main__":

    df = load_hospital_data(RAW_DATA_PATH)

    inspect_dataset(df)

    calculate_completeness(df)