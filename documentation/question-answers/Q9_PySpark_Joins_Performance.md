# Q9: PySpark Joins and Performance

## Objective

To load customer and order datasets into PySpark DataFrames, join them, identify customers without orders, calculate city-wise order values, and understand broadcast joins, transformations, and actions.

## 1. Input Datasets

- `PySpark/data/customers.csv`: CustomerID, CustomerName, City
- `PySpark/data/orders.csv`: OrderID, CustomerID, OrderAmount, OrderDate

Both datasets were loaded using `spark.read.csv()` with `header=True` and `inferSchema=True`.

## 2. Join Orders with Customer Details

An inner join was performed using `CustomerID`.

```python
joined = orders.join(customers, "CustomerID", "inner")
joined.show(truncate=False)
```

The result contains eight orders with their corresponding customer names and cities.

## 3. Customers Who Never Placed an Order

A left anti join identifies customers whose IDs do not appear in the orders dataset.

```python
customers.join(
    orders.select("CustomerID").distinct(),
    "CustomerID",
    "left_anti"
).show(truncate=False)
```

**Result:** C006 — Meera, Hubballi.

## 4. Total Order Value by City

```python
joined.groupBy("City").agg(
    spark_sum("OrderAmount").alias("TotalOrderValue")
).orderBy(col("TotalOrderValue").desc()).show()
```

### Results

| City | Total Order Value |
|---|---:|
| Bengaluru | 8400 |
| Hassan | 4500 |
| Mysuru | 4500 |
| Mangaluru | 3500 |

## 5. Broadcast Join

A broadcast join is useful when one dataset is sufficiently small to fit in executor memory. It distributes the smaller dataset to worker nodes and can reduce shuffle during the join.

The program uses `broadcast(customers)` and calls `explain()` to display the physical execution plan. The output shows `BroadcastHashJoin`.

## 6. Transformations and Actions

- **Transformation:** `filter()` creates a transformed DataFrame. Transformations are evaluated lazily.
- **Action:** `show()` triggers execution and displays DataFrame records.

## 7. Conclusion

The PySpark program successfully loaded and joined the datasets, identified customers without orders, calculated city-wise order values, demonstrated a broadcast join, and explained transformations and actions.

## Screenshots

Capture and save screenshots of the customer and order DataFrames, joined results, customers without orders, city-wise aggregation, and broadcast join execution plan in `documentation/screenshots/`.
