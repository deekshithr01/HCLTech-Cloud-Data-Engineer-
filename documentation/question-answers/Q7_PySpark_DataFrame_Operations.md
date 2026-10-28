# Q7: PySpark DataFrame Operations

## Problem Statement

Create a PySpark DataFrame containing the columns EmployeeID, EmployeeName, Department, Salary, and JoiningDate. Insert at least 15 employee records and perform the required DataFrame operations.

## 1. PySpark Program

**File:** `PySpark/scripts/Q7_DataFrame_Operations.py`

The program creates a Spark session, builds a DataFrame with 15 employee records, converts `JoiningDate` into a date type, and performs all five required operations.

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count

spark = SparkSession.builder \
    .appName("Q7_DataFrame_Operations") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

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
    "EmployeeID", "EmployeeName", "Department",
    "Salary", "JoiningDate"
]

df = spark.createDataFrame(data, columns)
df = df.withColumn("JoiningDate", col("JoiningDate").cast("date"))

# (a) Display schema and first five records
df.printSchema()
df.show(5, truncate=False)

# (b) Filter employees earning more than 60000
df.filter(col("Salary") > 60000).show(truncate=False)

# (c) Add annual salary
df_annual = df.withColumn("AnnualSalary", col("Salary") * 12)
df_annual.show(truncate=False)

# (d) Department-wise average salary and employee count
df.groupBy("Department").agg(
    avg("Salary").alias("AverageSalary"),
    count("*").alias("EmployeeCount")
).orderBy("Department").show(truncate=False)

# (e) Display five highest-paid employees
df.orderBy(col("Salary").desc()).show(5, truncate=False)

spark.stop()
```

## 2. Results and Explanations

### (a) Display schema and first five records

**Method:** `printSchema()` displays column names and data types. `show(5)` displays the first five records.

**Observed columns:**

- `EmployeeID`: long
- `EmployeeName`: string
- `Department`: string
- `Salary`: long
- `JoiningDate`: date

### (b) Filter employees whose monthly salary is greater than ₹60,000

**Code:**

```python
df.filter(col("Salary") > 60000).show(truncate=False)
```

**Observed result:** 10 employees satisfy the condition.

### (c) Add an AnnualSalary column

**Code:**

```python
df_annual = df.withColumn("AnnualSalary", col("Salary") * 12)
```

**Explanation:** `withColumn()` adds a new column. Annual salary is calculated by multiplying monthly salary by 12.

Example: Rahul's monthly salary is ₹75,000, so his annual salary is ₹9,00,000.

### (d) Calculate average salary and employee count by department

**Code:**

```python
df.groupBy("Department").agg(
    avg("Salary").alias("AverageSalary"),
    count("*").alias("EmployeeCount")
).orderBy("Department").show(truncate=False)
```

**Observed results:**

| Department | Average salary | Employee count |
|---|---:|---:|
| Finance | ₹74,500.00 | 4 |
| HR | ₹48,333.33 | 3 |
| IT | ₹74,000.00 | 5 |
| Sales | ₹60,333.33 | 3 |

**Explanation:** `groupBy()` groups employees by department. `avg()` calculates average salary, and `count()` counts employees in each group.

### (e) Display the five highest-paid employees

**Code:**

```python
df.orderBy(col("Salary").desc()).show(5, truncate=False)
```

**Observed results:**

| Rank | Employee | Department | Monthly salary |
|---:|---|---|---:|
| 1 | Arjun | IT | ₹90,000 |
| 2 | Neha | Finance | ₹85,000 |
| 3 | Amit | IT | ₹82,000 |
| 4 | Manoj | Finance | ₹78,000 |
| 5 | Rahul | IT | ₹75,000 |

**Explanation:** `orderBy()` with descending salary order places the highest salaries first. `show(5)` displays the top five records.

## Result

The PySpark program executed successfully. It displayed the DataFrame schema and first five records, filtered employees earning more than ₹60,000, calculated annual salaries, aggregated department-wise salary statistics, and displayed the five highest-paid employees.