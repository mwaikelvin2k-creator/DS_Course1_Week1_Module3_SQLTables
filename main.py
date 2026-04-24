# CodeGrade step0
# Run this cell without changes

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# CodeGrade step1
# Replace None with your code
df_boston = pd.read_sql(""" 
        SELECT 
            firstName,
            lastName 
        FROM employees e
        JOIN offices o ON e.officeCode = o.officecode
        WHERE city = 'Boston'
 """, conn)

# CodeGrade step2
# Replace None with your code
df_zero_emp = pd.read_sql(""" 
        SELECT COUNT(e.employeeNumber) AS Total_employees,
                o.officecode
        FROM employees e
        JOIN offices o ON e.officeCode = o.officecode
        GROUP BY e.officeCode
        HAVING Total_employees = 0
       
 """, conn)

# CodeGrade step3
# Replace None with your code
df_employee = pd.read_sql("""
        SELECT 
                e.firstName,
                e.lastName,
                o.city,
                o.state
        FROM employees e
        JOIN offices o 
        ON e.officecode = o.officecode
        GROUP BY e.employeeNumber
        ORDER BY e.firstName, e.lastName 
""",conn)


# CodeGrade step4
# Replace None with your code
df_contacts = pd.read_sql("""
        SELECT
                c.contactLastName,
                c.contactFirstName,
                c.phone,
                c.salesRepEmployeeNumber
        FROM customers c
        LEFT JOIN orders o
        ON c.customerNumber = o.customerNumber
        GROUP BY c.customerNumber
        HAVING   COUNT(orderNumber) = 0
        ORDER BY c.contactLastName
""", conn)

# CodeGrade step5
# Replace None with your code
df_payment = pd.read_sql("""
        SELECT
                c.contactFirstName,
                c.contactLastName,
                p.paymentDate,
                CAST(p.amount AS REAL)
        FROM customers c
        FULL OUTER JOIN payments p
        ON c.customerNumber = p.customerNumber
        ORDER BY CAST(p.amount AS REAL) DESC
""", conn)
df_payment

# CodeGrade step6
# Replace None with your code
df_credit = pd.read_sql("""
        SELECT
                e.employeeNumber,
                e.firstName,
                e.lastName,
        COUNT(c.customerNumber) AS Number_of_customers
        FROM employees e
        JOIN customers c
        ON e.employeeNumber = c.salesRepEmployeeNumber
        GROUP BY e.employeeNumber
        HAVING AVG(c.creditLimit) > 90000
        ORDER BY Number_of_customers  DESC
""", conn)

# CodeGrade step7
# Replace None with your code
df_product_sold = pd.read_sql("""
        SELECT
                p.productName,
                COUNT(o.orderNumber) AS numorders,
                SUM(o.quantityOrdered) AS totalunits
        FROM products p
        JOIN orderdetails o ON p.productCode = o.productCode
        GROUP BY p.productCode
        ORDER BY totalunits DESC
""", conn)

# CodeGrade step8
# Replace None with your code
df_total_customers = pd.read_sql("""
        SELECT
                p.productName,
                p.productCode,
                COUNT(DISTINCT c.customerNumber) AS numpurchasers
        FROM customers c
        JOIN orders o ON c.customerNumber = o.customerNumber
        JOIN orderdetails od ON o.orderNumber = od.orderNumber
        JOIN products p ON od.productCode = p.productCode
        GROUP BY p.productCode
        ORDER BY numpurchasers DESC
""", conn)          


# CodeGrade step9
# Replace None with your code
df_customers = pd.read_sql("""
        SELECT 
                COUNT(c.customerNumber) AS n_customers,
                o.officeCode,
                o.city
        FROM customers c
        JOIN employees e ON  e.employeeNumber = c.salesRepEmployeeNumber
        JOIN offices o ON o.officeCode = e.officecode
        GROUP BY o.officecode
""", conn)


# CodeGrade step10
# Replace None with your code
df_under_20 = pd.read_sql("""
    SELECT DISTINCT
                e.employeeNumber,
                e.firstName,
                e.lastName,
                o.officeCode,
                o.city
        FROM employees e
        JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
        JOIN orders ord ON c.customerNumber = ord.customerNumber
        JOIN orderdetails od ON ord.orderNumber = od.orderNumber
        JOIN offices o ON e.officeCode = o.officeCode
        WHERE od.productCode IN (
                SELECT productCode
                FROM customers
                JOIN orders ON customers.customerNumber = orders.customerNumber
                JOIN orderdetails ON orders.orderNumber = orderdetails.orderNumber
                GROUP BY productCode
                HAVING COUNT(DISTINCT customers.customerNumber) < 20
        )
""", conn)

# Run this cell without changes

conn.close()