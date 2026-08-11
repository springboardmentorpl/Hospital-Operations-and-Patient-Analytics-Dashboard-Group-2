# Hospital Operations & Patient Analytics Dashboard

## Project Overview

This project focuses on analyzing hospital operations and patient data to generate useful insights related to patient flow, department performance, and healthcare resource utilization.

The project uses Python for data collection, cleaning, and transformation. The cleaned dataset will be used for further healthcare analytics and Tableau dashboard development.

---

## Project Workflow

The overall workflow of the project is:

Data Collection  
↓  
Data Cleaning & Transformation  
↓  
Healthcare KPI Engineering  
↓  
Dashboard Development  
↓  
Dashboard Integration  
↓  
Testing & Validation  
↓  
Documentation & Delivery

---

# Module 1: Hospital Data Collection

### Objective

The objective of Module 1 is to collect and prepare the raw hospital patient dataset for further processing.

### Tasks Performed

- Loaded the hospital patient dataset using Python and Pandas.
- Checked the dataset structure.
- Checked the number of rows and columns.
- Checked missing values.
- Checked duplicate records.
- Saved the raw dataset in the required format.

### Deliverables

- `hospital_raw_data.csv`
- `data_collection.py`

---

# Module 2: Data Cleaning & Transformation

### Objective

The objective of Module 2 is to clean and transform the hospital patient dataset into a Tableau-ready dataset.

### Data Cleaning

The following cleaning tasks were performed:

- Checked and removed duplicate records.
- Checked missing values.
- Standardized text/categorical values.
- Converted the arrival date and time into proper datetime format.

### Data Transformation

The following new analytical columns were created:

- `total_wait_time_min`
- `stay_category`
- `billing_category`
- `wait_time_category`

### Data Normalization

The `total_wait_time_min` healthcare indicator was normalized using Min-Max normalization and stored in:

- `wait_time_normalized`

The normalized values are scaled between 0 and 1.

### Data Validation

The final dataset was validated by checking:

- Total rows
- Total columns
- Missing values
- Duplicate records
- Normalized value range

### Deliverables

- `hospital_cleaning.ipynb`
- `hospital_cleaned.csv`

---

# Files Description

| File | Description |
|---|---|
| `hospital_raw_data.csv` | Original raw hospital dataset |
| `data_collection.py` | Python script used to load and prepare the raw dataset |
| `hospital_cleaning.ipynb` | Jupyter Notebook containing data cleaning and transformation |
| `hospital_cleaned.csv` | Final cleaned, transformed and normalized dataset |

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook
- Tableau

---

# Module 2 Output

The final `hospital_cleaned.csv` dataset is prepared for further healthcare analytics and Tableau dashboard development.

---

## Project Structure

```text
Hospital-Operations-and-Patient-Analytics-Dashboard
│
├── hospital_raw_data.csv
├── data_collection.py
├── hospital_cleaning.ipynb
├── hospital_cleaned.csv
└── README.md
