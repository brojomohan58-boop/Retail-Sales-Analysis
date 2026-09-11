# Retail-Sales-Analysis
Sales data analysis and visualization project using Python, Power BI, and Git/GitHub.

# Retail Sales Performance Analysis — Data Analytics Capstone

## Project Overview
End-to-end data analytics project analyzing 60 retail sales transactions
(June-September 2024) using Python for cleaning/EDA and Power BI for
interactive business intelligence reporting.

## Problem Statement
The business observed fluctuating monthly performance and needed a
data-driven view of revenue trends, regional and category performance,
payment channel behavior, and profitability to guide Q4 decision-making.

## Dataset Description
- sales_fact.csv: 61 raw transaction records (sale_id, order_date,
  product_id, region, payment_method, quantity, unit_price, sales_amount)
- products.csv: 10 products (product_id, product_name, category, unit_cost)
- Final cleaned dataset (sales_data_cleaned.csv): 60 transactions,
  13 columns, 0 missing values, 0 duplicates

## Tools Used
- Git & GitHub - version control
- Python (Pandas, NumPy) - data cleaning and EDA
- Matplotlib & Seaborn - visualization
- Power BI - interactive dashboard and DAX measures

## Data Cleaning Process
- Removed unnecessary columns, fixed data types
- Standardized inconsistent text values (region casing)
- Imputed missing values (quantity, unit_price)
- Corrected negative quantity error
- Recalculated sales_amount, merged with product dimension table
- Calculated total_cost and profit, removed duplicates

## Exploratory Data Analysis (EDA)
- Descriptive statistics, correlation analysis, IQR-based outlier detection
- 8 visualizations covering trend, regional, category, payment, and
  distribution analysis

## Power BI Dashboard
- 4 KPIs with Month-over-Month trend indicators
- 5 interactive visualizations
- 3 slicers (Month, Region, Category)

## Key Insights
[See Task 7 above - 5 insights covering revenue decline, regional/category
performance, payment method gaps, and price-vs-volume drivers]

## Business Recommendations
[See Task 7 above - 2 recommendations on Q3 slump investigation and
Storage/South-East inventory concentration]

## Conclusion
This project demonstrates a complete data analytics workflow from raw
data to business-ready insights, using consistent, cross-validated
figures across both the Python and Power BI phases.

## Repository Contents
- /data - raw and cleaned datasets
- /notebooks - Dataset_Selection_Data_Preparation.ipynb, EDA_Visualizations.ipynb
- /dashboard - Power BI .pbix file and screenshots
- README.md - this file



## Key Insights

- Total sales reached approximately ₹1.50 million across 60 transactions.
- Monthly sales declined from approximately ₹643K in June to ₹185K in September, indicating a significant downward trend.
- South generated the highest regional sales at approximately ₹415K.
- Storage was the highest-performing category with approximately ₹510K in sales.
- UPI generated the highest sales among the payment methods at approximately ₹405K.

## Business Recommendations

- Investigate the decline in monthly sales after June by reviewing demand, product availability, pricing, and regional performance.
- Review inventory and sales concentration in the Storage category and South/East regions to identify opportunities for better inventory planning and targeted promotions.

## Conclusion

This project demonstrates a complete data analytics workflow from raw data to business-ready insights, using Python for data cleaning and exploratory analysis and Power BI for interactive reporting.

## Repository Contents

- `01_datasets` – Raw and cleaned datasets
- `02_python_cleaning` – Data cleaning and preparation notebooks/scripts
- `03_python_eda&visualization` – EDA notebook, Python scripts, and visualization images
- `04_power_bi` – Power BI dashboard file and dashboard screenshot
- `05_documentation` – Project report and presentation
- `README.md` – Project documentation
- `LICENSE` – Repository license

## Key Findings

- Total sales were approximately ₹1.50 million across 60 transactions.
- Total profit was approximately ₹606.18K, resulting in a profit margin of 40.36%.
- June recorded the highest monthly sales at approximately ₹643K.
- South recorded the highest regional sales at approximately ₹415K.
- Storage was the highest-performing category with approximately ₹510K in sales.
- UPI generated the highest sales among the payment methods at approximately ₹405K.
- Two high-value Gaming Chair transactions were identified as genuine bulk orders.
