# Q8: PySpark Data Cleaning and Aggregation

## Objective

To perform data cleaning and aggregation using PySpark DataFrames by removing duplicate records, handling missing values, converting date fields, calculating revenue, and finding total revenue by product.

## 1. Dataset

The input file is `PySpark/data/transactions.csv`. It contains transaction ID, product, quantity, unit price, and transaction date.

The dataset contains 12 records, including a duplicate transaction, a missing quantity, and an invalid date.

## 2. Schema Definition and CSV Loading

A `StructType` schema was defined with the following fields:

| Column | Data type |
|---|---|
| TransactionID | String |
| Product | String |
| Quantity | Integer |
| UnitPrice | Double |
| TransactionDate | String initially |

The CSV file was loaded using `spark.read.csv()` with `header=True` and the defined schema.

## 3. Data Cleaning

### Duplicate removal

Duplicate transactions were removed using `dropDuplicates(["TransactionID"])`.

### Missing value handling

Records with missing values in required fields were removed using `dropna()` on `TransactionID`, `Product`, `Quantity`, and `UnitPrice`.

### Date conversion

The `TransactionDate` column was converted to the date data type using `try_to_date()` with the `yyyy-MM-dd` format. Invalid dates became NULL values, and rows with NULL dates were removed.

## 4. Revenue Calculation

A new column named `Revenue` was created using:

`Revenue = Quantity × UnitPrice`

This was implemented using `withColumn()`.

## 5. Total Revenue by Product

The cleaned DataFrame was grouped by `Product`. The `sum()` aggregation calculated total revenue for each product, and `orderBy()` sorted the results in descending order.

### Output

| Product | Total Revenue |
|---|---:|
| Laptop | 275000.0 |
| Monitor | 24000.0 |
| Headphones | 9000.0 |
| Mouse | 4000.0 |
| Keyboard | 3600.0 |

## 6. Results and Observations

- Original dataset: 12 records.
- One duplicate transaction was removed.
- One record with a missing quantity was removed.
- One record with an invalid date was removed.
- Cleaned dataset: 9 records.
- The `TransactionDate` column was converted to the date data type.
- Revenue was calculated for every remaining transaction.
- Product-wise total revenue was calculated and sorted in descending order.

## 7. Conclusion

The PySpark program successfully cleaned the transaction dataset, handled duplicate and invalid records, calculated transaction revenue, and generated a product-wise revenue summary. The results demonstrate the use of DataFrame operations for data preparation and aggregation in a data engineering workflow.

## Screenshots

1. `31_PySpark_Q8_Original_Data_Schema.png`
2. `32_PySpark_Q8_Cleaned_Transactions.png`
3. `33_PySpark_Q8_Cleaned_Schema.png`
4. `34_PySpark_Q8_Revenue_By_Product.png`
