# Question 2: Sales Analytics and Query Optimization

## Objective
Create a Sales table with at least 15 sample records, calculate product-wise revenue, calculate monthly revenue and month-over-month changes using a window function, and optimize a date-filtering query.

## Table Structure
SaleID, CustomerID, SaleDate, ProductName, Quantity, UnitPrice.

## A. Total Revenue for Each Product

```sql
SELECT ProductName,
       SUM(Quantity * UnitPrice) AS TotalRevenue
FROM Sales
GROUP BY ProductName
ORDER BY TotalRevenue DESC;
```

Expected results:

| ProductName | TotalRevenue |
|---|---:|
| Laptop | 325000.00 |
| Monitor | 60000.00 |
| Keyboard | 9000.00 |
| Mouse | 5500.00 |

## B. Monthly Revenue and Month-over-Month Change

```sql
WITH MonthlyRevenue AS (
    SELECT DATE_FORMAT(SaleDate, '%Y-%m') AS SalesMonth,
           SUM(Quantity * UnitPrice) AS Revenue
    FROM Sales
    GROUP BY DATE_FORMAT(SaleDate, '%Y-%m')
),
RevenueWithPreviousMonth AS (
    SELECT SalesMonth, Revenue,
           LAG(Revenue) OVER (ORDER BY SalesMonth) AS PreviousMonthRevenue
    FROM MonthlyRevenue
)
SELECT SalesMonth, Revenue, PreviousMonthRevenue,
       Revenue - PreviousMonthRevenue AS RevenueChange
FROM RevenueWithPreviousMonth
ORDER BY SalesMonth;
```

Expected results:

| SalesMonth | Revenue | PreviousMonthRevenue | RevenueChange |
|---|---:|---:|---:|
| 2025-01 | 67500.00 | NULL | NULL |
| 2025-02 | 90500.00 | 67500.00 | 23000.00 |
| 2025-03 | 80000.00 | 90500.00 | -10500.00 |
| 2025-04 | 91000.00 | 80000.00 | 11000.00 |
| 2025-05 | 70500.00 | 91000.00 | -20500.00 |

`LAG()` retrieves the previous month's revenue. RevenueChange is current-month revenue minus previous-month revenue.

## C. Index-Friendly Date Filtering

Original question:

```sql
SELECT *
FROM Employees
WHERE YEAR(JoiningDate) = 2025;
```

The existing Q1 database uses `HireDate` instead of `JoiningDate`, so the adapted query is:

```sql
SELECT *
FROM Employees
WHERE HireDate >= '2025-01-01'
  AND HireDate < '2026-01-01';
```

This avoids applying `YEAR()` to the date column and can allow an index range scan if an appropriate index exists.

## Screenshots
- 07_SQL_Q2_Product_Revenue.png
- 08_SQL_Q2_Monthly_Revenue_MoM.png
- 09_SQL_Q2_Index_Friendly_Date_Filter.png