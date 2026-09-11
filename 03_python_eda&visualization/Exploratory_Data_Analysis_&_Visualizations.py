# InternNova — Data Analytics Internship
## Week 6 Assignment: Exploratory Data Analysis & Visualizations 
**Dataset:** `sales_data_cleaned.csv` \
**Prepared by:** Brojo Mohan Dutta\
**Environment:** Anaconda / Jupyter Notebook 7.4.5 / Python 3.x / Pandas

# Install Libraries & Load Data 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sales_data_cleaned.csv")
df.head()

# Inspect
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Data Types:\n", df.dtypes)
print("Missing values:\n", df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())
print("Unique region values:", df["region"].unique())

# Descriptive statistics
# Convert order_date from text to datetime
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

# Create month abbreviation for analysis
df["month"] = df["order_date"].dt.strftime("%b")

# Display descriptive statistics for key numerical variables
print("Descriptive Statistics:")
print(df[["quantity", "unit_price", "sales_amount", "profit"]].describe())

# Correlation analysis
correlation_matrix = df[["quantity", "unit_price", "sales_amount", "profit"]].corr()
print(correlation_matrix)

# Outlier detection (IQR method)
Q1 = df["sales_amount"].quantile(0.25)
Q3 = df["sales_amount"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df["sales_amount"] < lower_bound) | (df["sales_amount"] > upper_bound)]
print("Upper bound:", upper_bound)
print(outliers[["sale_id", "product_name", "quantity", "sales_amount"]])

# Patterns & Trends Summery
month_order = ["Jun", "Jul", "Aug", "Sep"]

print("Sales by month:\n", df.groupby("month")["sales_amount"].sum().reindex(month_order))
print("Sales by region:\n", df.groupby("region")["sales_amount"].sum().sort_values(ascending=False))
print("Sales by payment method:\n", df.groupby("payment_method")["sales_amount"].sum().sort_values(ascending=False))
print("Sales by category:\n", df.groupby("category")["sales_amount"].sum().sort_values(ascending=False))



import matplotlib.pyplot as plt
import seaborn as sns

df["order_date"] = pd.to_datetime(df["order_date"])

# 1. Line Chart — Monthly Sales Trend
monthly_sales = df.groupby("month")["sales_amount"].sum().reindex(month_order)

plt.figure(figsize=(8,5))
plt.plot(monthly_sales.index, monthly_sales.values, marker="o", color="teal")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales (₹)")
plt.tight_layout()
plt.show()

# 2. Bar Chart — Total Sales by Region
region_sales = df.groupby("region")["sales_amount"].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
plt.bar(region_sales.index, region_sales.values, color="steelblue")
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales (₹)")
plt.tight_layout()
plt.show()

# 3. Pie Chart — Sales Share by Category
category_sales = df.groupby("category")["sales_amount"].sum().sort_values(ascending=False)

plt.figure(figsize=(6,6))
wedges, texts, autotexts = plt.pie(
    category_sales.values,
    labels=category_sales.index,
    autopct="%1.1f%%",
    startangle=90,
    wedgeprops={"edgecolor": "white", "linewidth": 2}
)
for autotext in autotexts:
    autotext.set_color("white")
    autotext.set_fontweight("bold")
plt.title("Sales Share by Category")
plt.tight_layout()
plt.show()

# 4. Histogram — Distribution of Sales Amount
plt.figure(figsize=(9, 5))
plt.hist(df["sales_amount"], bins=10, edgecolor="white")
plt.title("Distribution of Sales Amount")
plt.xlabel("Sales Amount (₹)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 5. Box Plot — Sales Amount Distribution by Category
plt.figure(figsize=(9, 5))
sns.boxplot(data=df, x="category", y="sales_amount")
plt.title("Sales Amount Distribution by Category")
plt.xlabel(" ")
plt.ylabel("Sales Amount (₹)")
plt.tight_layout()
plt.show()

# 6. Count Plot — Transactions by Payment Method
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="payment_method", order=df["payment_method"].value_counts().index)
plt.title("Transaction Count by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Number of Transactions")
plt.tight_layout()
plt.show()

# 7. Scatter Plot — Unit Price vs Sales Amount
plt.figure(figsize=(9, 5))
plt.scatter(df["unit_price"], df["sales_amount"], alpha=0.7)
plt.title("Unit Price vs Sales Amount")
plt.xlabel("Unit Price (₹)")
plt.ylabel("Sales Amount (₹)")
plt.tight_layout()
plt.show()

# 8. Heatmap — Correlation Between Numeric Variables
plt.figure(figsize=(6,5))
sns.heatmap(df[["quantity", "unit_price", "sales_amount", "profit"]].corr(),
            annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

