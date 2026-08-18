import pandas as pd
import numpy as np
import re
import json

# ============================================================
# FILE NAMES
# ============================================================

INPUT_FILE = "hospital_raw_dataset.csv"
OUTPUT_CSV = "hospital_cleaned.csv"
OUTPUT_NOTEBOOK = "hospital_cleaning.ipynb"


# ============================================================
# 1. LOAD RAW DATASET
# ============================================================

df = pd.read_csv(INPUT_FILE)

print("Raw dataset shape:", df.shape)


# ============================================================
# 2. CLEAN COLUMN NAMES
# ============================================================

df.columns = [
    re.sub(r"[^a-z0-9]+", "_", str(col).strip().lower()).strip("_")
    for col in df.columns
]


# ============================================================
# 3. HANDLE COMMON MISSING VALUES
# ============================================================

missing_values = {
    "",
    " ",
    "na",
    "n/a",
    "nan",
    "null",
    "none",
    "unknown",
    "-",
    "--",
    "not available",
    "not_applicable"
}

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].apply(
        lambda x:
        np.nan
        if pd.isna(x) or str(x).strip().lower() in missing_values
        else str(x).strip()
    )


# ============================================================
# 4. REMOVE DUPLICATE RECORDS
# ============================================================

duplicates = df.duplicated().sum()

df = df.drop_duplicates().reset_index(drop=True)

print("Duplicate records removed:", duplicates)


# ============================================================
# 5. STANDARDIZE DEPARTMENT NAMES
# ============================================================

department_columns = [
    col for col in df.columns
    if "department" in col or col in ["dept", "unit"]
]

department_mapping = {
    "cardio": "Cardiology",
    "cardiology dept": "Cardiology",
    "cardiology department": "Cardiology",
    "cardiology": "Cardiology",

    "ortho": "Orthopedics",
    "orthopaedics": "Orthopedics",
    "orthopedics": "Orthopedics",
    "orthopedic": "Orthopedics",

    "ent": "ENT",
    "ear nose throat": "ENT",

    "emergency": "Emergency",
    "emergency dept": "Emergency",
    "emergency department": "Emergency",

    "general medicine": "General Medicine",
    "general med": "General Medicine",

    "general surgery": "General Surgery",

    "gastro": "Gastroenterology",
    "gastroenterology": "Gastroenterology",

    "neurology": "Neurology",
    "neuro": "Neurology",

    "oncology": "Oncology",

    "pediatrics": "Pediatrics",
    "paediatrics": "Pediatrics",
    "pediatric": "Pediatrics",

    "psychiatry": "Psychiatry",

    "radiology": "Radiology",

    "dermatology": "Dermatology",

    "gynecology": "Gynecology",
    "gynaecology": "Gynecology",

    "obgyn": "Obstetrics & Gynecology",
    "obstetrics & gynecology": "Obstetrics & Gynecology",

    "icu": "ICU"
}


def standardize_department(value):

    if pd.isna(value):
        return value

    value = re.sub(
        r"\s+",
        " ",
        str(value).strip().lower()
    )

    return department_mapping.get(
        value,
        value.title()
    )


for col in department_columns:
    df[col] = df[col].apply(standardize_department)


# ============================================================
# 6. NORMALIZE HEALTHCARE INDICATORS
# ============================================================

indicator_keywords = [
    "age",
    "bmi",
    "heart_rate",
    "pulse",
    "systolic",
    "diastolic",
    "blood_pressure",
    "temperature",
    "respiratory",
    "oxygen",
    "spo2",
    "glucose",
    "sugar",
    "cholesterol",
    "hemoglobin",
    "hba1c",
    "length_of_stay",
    "los",
    "wait_time",
    "readmission",
    "mortality",
    "satisfaction",
    "score",
    "rate",
    "count",
    "cost",
    "charge",
    "amount"
]


# Convert numeric healthcare indicators
for col in df.columns:

    if any(keyword in col for keyword in indicator_keywords):

        converted = pd.to_numeric(
            df[col]
            .astype(str)
            .str.replace(",", "", regex=False)
            .str.replace("%", "", regex=False),
            errors="coerce"
        )

        if converted.notna().sum() >= max(
            1,
            int(0.5 * df[col].notna().sum())
        ):
            df[col] = converted


# Normalize categorical indicators
indicator_mapping = {

    "yes": "Yes",
    "y": "Yes",
    "true": "Yes",
    "1": "Yes",

    "no": "No",
    "n": "No",
    "false": "No",
    "0": "No",

    "male": "Male",
    "m": "Male",

    "female": "Female",
    "f": "Female",

    "positive": "Positive",
    "pos": "Positive",

    "negative": "Negative",
    "neg": "Negative",

    "stable": "Stable",
    "critical": "Critical",

    "normal": "Normal",
    "abnormal": "Abnormal"
}


for col in df.select_dtypes(include="object").columns:

    values = (
        df[col]
        .dropna()
        .astype(str)
        .str.strip()
        .str.lower()
    )

    if len(values) > 0:

        matching_percentage = values.isin(
            indicator_mapping.keys()
        ).mean()

        if matching_percentage >= 0.5:

            df[col] = df[col].apply(
                lambda x:
                indicator_mapping.get(
                    str(x).strip().lower(),
                    x
                )
                if pd.notna(x)
                else x
            )


# ============================================================
# 7. HANDLE MISSING PATIENT DATA
# ============================================================

for col in df.columns:

    if df[col].isna().sum() == 0:
        continue

    # Numeric columns → median
    if pd.api.types.is_numeric_dtype(df[col]):

        median_value = df[col].median()

        if pd.notna(median_value):
            df[col] = df[col].fillna(median_value)
        else:
            df[col] = df[col].fillna(0)

    # Text columns
    else:

        # Patient ID / other ID columns
        if "id" in col.lower():

            df[col] = df[col].fillna("Unknown")

        # Other categorical columns → mode
        else:

            mode_value = df[col].mode(dropna=True)

            if len(mode_value) > 0:
                df[col] = df[col].fillna(
                    mode_value.iloc[0]
                )
            else:
                df[col] = df[col].fillna("Unknown")


# ============================================================
# 8. STANDARDIZE DATE COLUMNS
# ============================================================

for col in df.columns:

    if any(
        keyword in col
        for keyword in [
            "date",
            "admission",
            "discharge"
        ]
    ):

        parsed_date = pd.to_datetime(
            df[col],
            errors="coerce",
            dayfirst=True
        )

        if parsed_date.notna().sum() >= max(
            1,
            int(0.7 * len(df))
        ):

            df[col] = parsed_date.dt.strftime(
                "%Y-%m-%d"
            )


# ============================================================
# 9. REMOVE UNNECESSARY INDEX COLUMNS
# ============================================================

df = df.loc[
    :,
    ~df.columns.str.match(r"^unnamed")
]


# ============================================================
# 10. SAVE CLEANED CSV
# ============================================================

df.to_csv(
    OUTPUT_CSV,
    index=False
)

print("Cleaned CSV created:", OUTPUT_CSV)
print("Final dataset shape:", df.shape)
print(
    "Remaining missing values:",
    df.isna().sum().sum()
)


# ============================================================
# 11. CREATE JUPYTER NOTEBOOK
# ============================================================

notebook_cells = [

    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# Hospital Dataset Cleaning\n",
            "\n",
            "This notebook cleans the hospital raw dataset and "
            "creates a Tableau-ready dataset.\n",
            "\n",
            "### Cleaning Operations\n",
            "1. Remove duplicate records\n",
            "2. Handle missing patient data\n",
            "3. Standardize department names\n",
            "4. Normalize healthcare indicators\n",
            "5. Standardize date fields\n",
            "6. Export Tableau-ready CSV\n"
        ]
    },

    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "import pandas as pd\n",
            "import numpy as np\n",
            "import re\n",
            "\n",
            "df = pd.read_csv('hospital_raw_dataset.csv')\n",
            "print('Raw dataset shape:', df.shape)\n",
            "df.head()\n"
        ]
    },

    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Remove duplicate records\n",
            "duplicates = df.duplicated().sum()\n",
            "df = df.drop_duplicates().reset_index(drop=True)\n",
            "print('Duplicates removed:', duplicates)\n"
        ]
    },

    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Handle missing values\n",
            "for col in df.columns:\n",
            "    if df[col].isna().sum() > 0:\n",
            "        if pd.api.types.is_numeric_dtype(df[col]):\n",
            "            df[col] = df[col].fillna(df[col].median())\n",
            "        else:\n",
            "            mode = df[col].mode()\n",
            "            df[col] = df[col].fillna(\n",
            "                mode.iloc[0] if len(mode) else 'Unknown'\n",
            "            )\n"
        ]
    },

    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Standardize department names\n",
            "department_mapping = {\n",
            "    'cardio': 'Cardiology',\n",
            "    'cardiology dept': 'Cardiology',\n",
            "    'ortho': 'Orthopedics',\n",
            "    'orthopaedics': 'Orthopedics',\n",
            "    'ent': 'ENT',\n",
            "    'emergency dept': 'Emergency',\n",
            "    'general med': 'General Medicine',\n",
            "    'neuro': 'Neurology',\n",
            "    'gastro': 'Gastroenterology',\n",
            "    'paediatrics': 'Pediatrics'\n",
            "}\n",
            "\n",
            "for col in df.columns:\n",
            "    if 'department' in col or col in ['dept', 'unit']:\n",
            "        df[col] = df[col].apply(\n",
            "            lambda x: department_mapping.get(\n",
            "                str(x).strip().lower(),\n",
            "                x\n",
            "            ) if pd.notna(x) else x\n",
            "        )\n"
        ]
    },

    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Normalize healthcare indicators\n",
            "indicator_mapping = {\n",
            "    'yes': 'Yes', 'y': 'Yes', 'true': 'Yes',\n",
            "    'no': 'No', 'n': 'No', 'false': 'No',\n",
            "    'male': 'Male', 'm': 'Male',\n",
            "    'female': 'Female', 'f': 'Female',\n",
            "    'positive': 'Positive', 'pos': 'Positive',\n",
            "    'negative': 'Negative', 'neg': 'Negative'\n",
            "}\n",
            "\n",
            "for col in df.select_dtypes(include='object').columns:\n",
            "    df[col] = df[col].apply(\n",
            "        lambda x: indicator_mapping.get(\n",
            "            str(x).strip().lower(), x\n",
            "        ) if pd.notna(x) else x\n",
            "    )\n"
        ]
    },

    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Save Tableau-ready dataset\n",
            "df.to_csv('hospital_cleaned.csv', index=False)\n",
            "\n",
            "print('hospital_cleaned.csv created successfully!')\n",
            "print('Final shape:', df.shape)\n",
            "print('Missing values:', df.isna().sum().sum())\n"
        ]
    }
]


notebook = {
    "cells": notebook_cells,
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 5
}


# ============================================================
# 12. SAVE NOTEBOOK
# ============================================================

with open(
    OUTPUT_NOTEBOOK,
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        notebook,
        file,
        indent=4
    )


print("Jupyter notebook created:", OUTPUT_NOTEBOOK)
print("\nAll files created successfully!")