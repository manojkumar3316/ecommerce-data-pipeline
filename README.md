# E-commerce Data Pipeline using PySpark & Databricks

## 📌 Objective
This project builds a real-time inspired ETL pipeline for e-commerce sales data using **PySpark** and **Databricks**.

## ⚙️ Tech Stack
- Python
- PySpark
- Databricks / Jupyter Notebook
- Delta Lake / Parquet

## 📊 Dataset
`sales_data.csv` contains sample raw e-commerce transactions.

## 🚀 Steps
1. Clone this repo:
   ```bash
   git clone https://github.com/manojkumar3316/ecommerce-data-pipeline.git
   ```
2. Open `ecommerce_pipeline.py` in Databricks or Jupyter.
3. Run the pipeline to:
   - Load raw data
   - Clean missing values
   - Transform & calculate sales amount
   - Aggregate daily sales
   - Save results as Parquet

## ✅ Example Output
### Cleaned + Transformed Data
| order_id | customer_id | order_date | product   | quantity | price | total_amount |
|----------|-------------|------------|-----------|----------|-------|--------------|
| 1001     | C001        | 2025-09-10 | Laptop    | 1        | 75000 | 75000        |
| 1002     | C002        | 2025-09-11 | Headphones| 2        | 2000  | 4000         |

### Daily Sales
| order_date | total_sales | avg_order_value |
|------------|-------------|-----------------|
| 2025-09-10 | 75000       | 75000.0         |
| 2025-09-11 | 34000       | 17000.0         |
