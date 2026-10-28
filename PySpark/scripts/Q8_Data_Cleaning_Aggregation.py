from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType, StructField, StringType,
    IntegerType, DoubleType
)
from pyspark.sql.functions import (
    col, try_to_date, sum as spark_sum
)

# Create Spark session
spark = SparkSession.builder \
    .appName("Q8_Data_Cleaning_Aggregation") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# Define schema
schema = StructType([
    StructField("TransactionID", StringType(), True),
    StructField("Product", StringType(), True),
    StructField("Quantity", IntegerType(), True),
    StructField("UnitPrice", DoubleType(), True),
    StructField("TransactionDate", StringType(), True)
])

# Read CSV file
df = spark.read.csv(
    "PySpark/data/transactions.csv",
    header=True,
    schema=schema
)

print("\n--- (1) ORIGINAL TRANSACTIONS ---")
df.show(truncate=False)

print("\n--- (2) ORIGINAL SCHEMA ---")
df.printSchema()

# Remove duplicate transactions using TransactionID
df_clean = df.dropDuplicates(["TransactionID"])

# Remove rows with missing required values
df_clean = df_clean.dropna(
    subset=["TransactionID", "Product", "Quantity", "UnitPrice"]
)

# Convert dates safely; invalid dates become NULL
df_clean = df_clean.withColumn(
    "TransactionDate",
    try_to_date(col("TransactionDate"), "yyyy-MM-dd")
)

# Remove rows with invalid or missing dates
df_clean = df_clean.filter(
    col("TransactionDate").isNotNull()
)

# Calculate revenue
df_clean = df_clean.withColumn(
    "Revenue",
    col("Quantity") * col("UnitPrice")
)

print("\n--- (3) CLEANED TRANSACTIONS ---")
df_clean.show(truncate=False)

print("\n--- (4) CLEANED DATA SCHEMA ---")
df_clean.printSchema()

# Calculate total revenue by product
print("\n--- (5) TOTAL REVENUE BY PRODUCT ---")
df_clean.groupBy("Product").agg(
    spark_sum("Revenue").alias("TotalRevenue")
).orderBy(
    col("TotalRevenue").desc()
).show(truncate=False)

spark.stop()