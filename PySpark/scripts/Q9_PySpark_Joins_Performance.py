from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum, broadcast

spark = SparkSession.builder.appName("Q9_Joins_Performance").master("local[*]").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

customers = spark.read.csv("PySpark/data/customers.csv", header=True, inferSchema=True)
orders = spark.read.csv("PySpark/data/orders.csv", header=True, inferSchema=True)

print("\\n--- (a) CUSTOMERS ---")
customers.show(truncate=False)

print("\\n--- (a) ORDERS ---")
orders.show(truncate=False)

print("\\n--- (b) ORDERS WITH CUSTOMER DETAILS ---")
joined = orders.join(customers, "CustomerID", "inner")
joined.show(truncate=False)

print("\\n--- (c) CUSTOMERS WHO NEVER PLACED AN ORDER ---")
customers.join(orders.select("CustomerID").distinct(), "CustomerID", "left_anti").show(truncate=False)

print("\\n--- (d) TOTAL ORDER VALUE BY CITY ---")
joined.groupBy("City").agg(spark_sum("OrderAmount").alias("TotalOrderValue")).orderBy(col("TotalOrderValue").desc()).show(truncate=False)

print("\\n--- (e) BROADCAST JOIN ---")
print("Broadcast joins are useful when one dataset is small enough to fit in executor memory. They can reduce shuffle.")
broadcast(customers).join(orders, "CustomerID", "inner").explain()

print("\\n--- (f) TRANSFORMATIONS AND ACTIONS ---")
print("Transformation example: filter() creates a new DataFrame lazily.")
print("Action example: show() triggers execution and displays results.")

spark.stop()
