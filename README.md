# SQL Webhook App – Python Automation

This Python application automates the process of retrieving a webhook for a coding challenge, solving an SQL-based problem, and submitting the final SQL query via an authenticated request.

---

## 🚀 Features

- Automatically generates a webhook and access token from the challenge provider.
- Determines the SQL problem based on the last digit of the registration number.
- Solves the SQL problem (for even registration number - Question 2).
- Submits the final SQL query securely using the provided webhook.

---

## 🛠️ Technologies Used

- Python 3
- `requests` library for handling HTTP requests

---

## 🧠 Problem Statement

> For each employee, return the count of employees in the same department who are **younger** than them, along with their department name.  
> Output should include:
>
> - `EMP_ID`
> - `FIRST_NAME`
> - `LAST_NAME`
> - `DEPARTMENT_NAME`
> - `YOUNGER_EMPLOYEES_COUNT`

---

## 🧾 Final SQL Query

```sql
SELECT 
    e1.EMP_ID,
    e1.FIRST_NAME,
    e1.LAST_NAME,
    d.DEPARTMENT_NAME,
    COUNT(e2.EMP_ID) AS YOUNGER_EMPLOYEES_COUNT
FROM EMPLOYEE e1
JOIN DEPARTMENT d ON e1.DEPARTMENT = d.DEPARTMENT_ID
LEFT JOIN EMPLOYEE e2 
    ON e1.DEPARTMENT = e2.DEPARTMENT 
    AND e2.DOB > e1.DOB
GROUP BY 
    e1.EMP_ID, e1.FIRST_NAME, e1.LAST_NAME, d.DEPARTMENT_NAME
ORDER BY e1.EMP_ID DESC;
