-- HCLTech Cloud Data Engineer - Question 1
-- EnterpriseDB: Departments and Employees

CREATE DATABASE IF NOT EXISTS EnterpriseDB;
USE EnterpriseDB;

DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Departments;

CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    EmployeeName VARCHAR(100) NOT NULL,
    DepartmentID INT NOT NULL,
    Salary DECIMAL(12,2) NOT NULL CHECK (Salary > 0),
    HireDate DATE NOT NULL,
    ManagerID INT NULL,
    CONSTRAINT fk_employee_department
        FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID),
    CONSTRAINT fk_employee_manager
        FOREIGN KEY (ManagerID) REFERENCES Employees(EmployeeID)
);

INSERT INTO Departments (DepartmentID, DepartmentName) VALUES
(10, 'Engineering'),
(20, 'Human Resources'),
(30, 'Finance'),
(40, 'Marketing'),
(50, 'Research and Development');

INSERT INTO Employees
(EmployeeID, EmployeeName, DepartmentID, Salary, HireDate, ManagerID)
VALUES
(1, 'Deekshith', 10, 120000.00, '2020-01-15', NULL),
(2, 'Varshith', 20, 90000.00, '2021-03-10', NULL),
(3, 'Nanditha', 30, 110000.00, '2019-07-22', NULL),
(4, 'Darshan', 40, 100000.00, '2022-02-01', NULL);

INSERT INTO Employees
(EmployeeID, EmployeeName, DepartmentID, Salary, HireDate, ManagerID)
VALUES
(5, 'Rakshith', 10, 95000.00, '2023-05-12', 1),
(6, 'Gowtham', 10, 95000.00, '2023-08-20', 1),
(7, 'Jayanth', 10, 80000.00, '2024-01-05', 1),
(8, 'Poorvika', 20, 65000.00, '2024-04-15', 2),
(9, 'Arjun', 20, 55000.00, '2025-01-10', 2),
(10, 'Divya', 30, 85000.00, '2023-11-01', 3),
(11, 'Rohan', 30, 70000.00, '2024-06-18', 3),
(12, 'Pooja', 40, 75000.00, '2025-02-14', 4),
(13, 'Nikhil', 40, 60000.00, '2025-06-01', 4),
(14, 'Ishita', 10, 70000.00, '2025-08-11', 1),
(15, 'Aditya', 30, 70000.00, '2025-09-25', 3);

-- Verification
SELECT COUNT(*) AS total_departments FROM Departments;
SELECT COUNT(*) AS total_employees FROM Employees;

-- Employee and department details
SELECT e.EmployeeID, e.EmployeeName, d.DepartmentName, e.Salary
FROM Employees e
JOIN Departments d ON e.DepartmentID = d.DepartmentID
ORDER BY e.EmployeeID;

-- Employees earning above their department's average salary
SELECT e.EmployeeName, d.DepartmentName, e.Salary
FROM Employees e
JOIN Departments d ON e.DepartmentID = d.DepartmentID
WHERE e.Salary > (
    SELECT AVG(e2.Salary)
    FROM Employees e2
    WHERE e2.DepartmentID = e.DepartmentID
)
ORDER BY d.DepartmentName, e.Salary DESC;

-- Second-highest distinct salary
SELECT MAX(Salary) AS second_highest_salary
FROM Employees
WHERE Salary < (SELECT MAX(Salary) FROM Employees);

-- Top three employees per department, including salary ties
WITH RankedEmployees AS (
    SELECT EmployeeID, EmployeeName, DepartmentID, Salary,
           RANK() OVER (
               PARTITION BY DepartmentID
               ORDER BY Salary DESC
           ) AS salary_rank
    FROM Employees
)
SELECT r.EmployeeID, r.EmployeeName, d.DepartmentName,
       r.Salary, r.salary_rank
FROM RankedEmployees r
JOIN Departments d ON r.DepartmentID = d.DepartmentID
WHERE r.salary_rank <= 3
ORDER BY d.DepartmentID, r.salary_rank, r.EmployeeName;
