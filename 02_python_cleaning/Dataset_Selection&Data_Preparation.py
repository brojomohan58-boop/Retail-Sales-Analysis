# InternNova — Data Analytics Internship
## Week 6 Assignment: Dataset Selection & Data Preparation 
**Dataset:** `sales_fact.csv` & `product.csv`  \
**Prepared by:** Brojo Mohan Dutta\
**Environment:** Anaconda / Jupyter Notebook 7.4.5 / Python 3.x / Pandas

# Setup & Load
import pandas as pd
import numpy as np

sales = pd.read_csv("sales_fact.csv")
products = pd.read_csv("products.csv")

sales.head()

# Inspect
print("Shape:", sales.shape)
print("Columns:", sales.columns.tolist())
print("Data Types:\n", sales.dtypes)
print("Missing values:\n", sales.isnull().sum())
print("Duplicate rows:", sales.duplicated().sum())
print("Unique region values:", sales["region"].unique())

# Clean
df_clean = df.copy()

# 1. Remove unnecessary column
df = df.drop(columns=["notes"])

# 2. Fix data types
df["order_date"] = pd.to_datetime(df["order_date"])

# 3. Standardize inconsistent text in 'region'
df["region"] = df["region"].str.strip().str.title()

# 4. Handle missing values
df["quantity"] = df["quantity"].fillna(5)
df["unit_price"] = df["unit_price"].fillna(1999)

# 5. Fix incorrect value (negative quantity -> positive)
df.loc[df["quantity"] < 0, "quantity"] = df.loc[df["quantity"] < 0, "quantity"].abs()
df["quantity"] = df["quantity"].astype(int)

# 6. Recompute sales_amount cleanly
df["sales_amount"] = df["quantity"] * df["unit_price"]

# 7. Remove duplicate records
df = df.drop_duplicates()

print("Shape after cleaning:", df.shape)
print("Missing values after cleaning:\n", df.isnull().sum())
print("Duplicate rows after cleaning:", df.duplicated().sum())
