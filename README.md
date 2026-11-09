# Titanic-Data-Cleaning-Project

## Objective
To identify and clean missing values, duplicate records, incorrect data types, and inconsistent text values in a public dataset.

## Dataset
- **Name:** Titanic passenger dataset
- **Source:** [DataScienceDojo public Titanic CSV](https://github.com/datasciencedojo/datasets/blob/master/titanic.csv)
- **Direct CSV:** https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
- **Original size:** 891 rows and 12 columns
- Each row represents one Titanic passenger.

## Data quality issues checked
1. **Missing values:** The standard dataset contains missing values in `Age`, `Cabin`, and `Embarked` (commonly 177, 687, and 2 respectively).
2. **Duplicate records:** Exact duplicate rows are checked and removed if present. The standard 891-row file has 0 exact duplicate rows.
3. **Data types:** Numeric columns are converted using `pandas.to_numeric()` so they can be used correctly in calculations.
4. **Inconsistent values:** Text values are stripped of extra spaces; `Sex` is standardized to `Male` / `Female`, and `Embarked` is standardized to uppercase.

## Cleaning performed
- Removed exact duplicate rows.
- Filled missing `Age` values with the median age.
- Filled missing `Embarked` values with the most common value (mode).
- Created `Cabin_Known` (1 = cabin recorded, 0 = cabin missing), then removed `Cabin` because it has a large number of missing values.
- Standardized text columns and converted numeric columns to numeric data types.
- Exported the cleaned file as `titanic_cleaned.csv`.

## Tools
Python 3, pandas

## How to run
1. Install Python and pandas:
   ```bash
   pip install -r requirements.txt
   ```
2. Run:
   ```bash
   python clean_titanic.py
   ```
3. The script reads the public CSV directly and creates `titanic_cleaned.csv` in the same folder. Internet access is required to load the source CSV.

## Repository files
- `clean_titanic.py` – data inspection and cleaning code
- `README.md` – project explanation
- `requirements.txt` – required Python library
- `titanic_cleaned.csv` – generated after running the script

## Result
The script prints the original and cleaned data size, missing-value counts, duplicate counts, and data types. The cleaned CSV is the final dataset to submit.
