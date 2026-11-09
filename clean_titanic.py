import pandas as pd

# Load the public Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print("ORIGINAL DATA")
print("Rows and columns:", df.shape)
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())
print("\nOriginal data types:\n", df.dtypes)

# 1. Remove exact duplicate records
df = df.drop_duplicates()

# 2. Fix data types
numeric_columns = ["PassengerId", "Survived", "Pclass", "Age",
                   "SibSp", "Parch", "Fare"]
for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# 3. Standardize text values (remove extra spaces and standardize case)
text_columns = ["Name", "Sex", "Ticket", "Cabin", "Embarked"]
for column in text_columns:
    df[column] = df[column].astype("string").str.strip()

df["Sex"] = df["Sex"].str.lower()
df["Sex"] = df["Sex"].replace({"male": "Male", "female": "Female"})
df["Embarked"] = df["Embarked"].str.upper()

# 4. Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Cabin has many missing values, so keep the useful information as a flag
df["Cabin_Known"] = df["Cabin"].notna().astype("int64")
df = df.drop(columns=["Cabin"])

# Save cleaned dataset
df.to_csv("titanic_cleaned.csv", index=False)

print("\nCLEANED DATA")
print("Rows and columns:", df.shape)
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())
print("\nFinal data types:\n", df.dtypes)
print("\nCleaned file saved as titanic_cleaned.csv")
