
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count

# Create Spark session
spark = SparkSession.builder \
    .appName("Q7_DataFrame_Operations") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# Create employee records: EmployeeID, EmployeeName,
# Department, Salary, JoiningDate
data = [
    (1, "Rahul", "IT", 75000, "2024-01-15"),
    (2, "Priya", "HR", 45000, "2023-03-10"),
    (3, "Amit", "IT", 82000, "2022-06-20"),
    (4, "Sneha", "Finance", 65000, "2024-02-12"),
    (5, "Kiran", "HR", 52000, "2021-11-05"),
    (6, "Arjun", "IT", 90000, "2020-07-18"),
    (7, "Meera", "Finance", 70000, "2022-09-25"),
    (8, "Vikram", "Sales", 58000, "2023-05-14"),
    (9, "Ananya", "Sales", 62000, "2021-08-30"),
    (10, "Rohit", "IT", 68000, "2023-12-01"),
    (11, "Pooja", "HR", 48000, "2024-04-22"),
    (12, "Manoj", "Finance", 78000, "2020-10-11"),
    (13, "Divya", "Sales", 61000, "2022-01-19"),
    (14, "Sanjay", "IT", 55000, "2024-06-03"),
    (15, "Neha", "Finance", 85000, "2021-02-16")
]

columns = [
    "EmployeeID",
    "EmployeeName",
    "Department",
    "Salary",
    "JoiningDate"
]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Convert JoiningDate from string to date
df = df.withColumn("JoiningDate", col("JoiningDate").cast("date"))

# (a) Display schema and first five records
print("\n--- (a) EMPLOYEE DATAFRAME SCHEMA ---")
df.printSchema()

print("\n--- FIRST FIVE EMPLOYEES ---")
df.show(5, truncate=False)

# (b) Filter employees earning more than 60000
print("\n--- (b) EMPLOYEES WITH SALARY > 60000 ---")
df.filter(col("Salary") > 60000).show(truncate=False)

# (c) Add AnnualSalary column
print("\n--- (c) EMPLOYEES WITH ANNUAL SALARY ---")
df_annual = df.withColumn("AnnualSalary", col("Salary") * 12)
df_annual.show(truncate=False)

# (d) Average salary and employee count by department
print("\n--- (d) DEPARTMENT-WISE SALARY AND EMPLOYEE COUNT ---")
df.groupBy("Department").agg(
    avg("Salary").alias("AverageSalary"),
    count("*").alias("EmployeeCount")
).orderBy("Department").show(truncate=False)

# (e) Display five highest-paid employees
print("\n--- (e) TOP FIVE HIGHEST-PAID EMPLOYEES ---")
df.orderBy(col("Salary").desc()).show(5, truncate=False)

# Stop Spark session
spark.stop()
