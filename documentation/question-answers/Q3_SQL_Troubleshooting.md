# Question 3: SQL Troubleshooting

## (a) Explain how an execution plan helps identify expensive operations in a query. (2 Marks)

An execution plan shows how MySQL plans to execute a query. It helps us understand which operations may take more time and resources. It shows whether the database uses an index or scans a table, along with the estimated number of rows examined. This information helps us identify slow operations and improve query performance.

## (b) Recommend an appropriate index strategy for queries filtering employees by DepartmentID and Salary. Explain your reasoning. (2 Marks)

A composite index on `DepartmentID` and `Salary` can improve queries that filter employees using these two columns.

```sql
CREATE INDEX idx_employee_department_salary
ON Employees (DepartmentID, Salary);
```

This index helps MySQL filter employees by department and salary more efficiently. In our execution plan, the estimated rows examined decreased from 5 to 3, and MySQL used the composite index with a range scan. Actual performance improvement depends on the data and query.

## (c) Write a query to identify duplicate customer email addresses and display only addresses occurring more than once. (2 Marks)

```sql
SELECT Email, COUNT(*) AS DuplicateCount
FROM Customers
GROUP BY Email
HAVING COUNT(*) > 1;
```

The `GROUP BY` clause groups customers with the same email address. `COUNT(*)` counts how often each address appears, and `HAVING COUNT(*) > 1` displays only addresses that occur more than once.

## Screenshots

- `10_SQL_Q3_Execution_Plan.png`
- `11_SQL_Q3_Composite_Index_Comparison.png`
- `12_SQL_Q3_Duplicate_Customer_Emails.png`