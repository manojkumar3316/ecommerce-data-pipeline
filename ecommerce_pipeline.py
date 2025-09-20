from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, sum as _sum, avg

spark = SparkSession.builder.appName("EcommerceDataPipeline").getOrCreate()

# Load raw data
raw_df = spark.read.csv("sales_data.csv", header=True, inferSchema=True)
print("Raw Data:")
raw_df.show()

# Data Cleaning
clean_df = raw_df.fillna({"product": "Unknown", "price": 0})
clean_df = clean_df.withColumn("order_date", to_date(col("order_date"), "yyyy-MM-dd"))

# Transformation
transformed_df = clean_df.withColumn("total_amount", col("quantity") * col("price"))

# Aggregation
daily_sales = transformed_df.groupBy("order_date").agg(
    _sum("total_amount").alias("total_sales"),
    avg("total_amount").alias("avg_order_value")
)

print("Daily Sales:")
daily_sales.show()

# Save output
transformed_df.write.mode("overwrite").parquet("processed_sales/")
daily_sales.write.mode("overwrite").parquet("daily_sales/")
