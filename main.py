# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect('data.sqlite')

# STEP 2
# Columns: employeeNumber, lastName
df_first_five = pd.read_sql_query("SELECT employeeNumber, lastName FROM employees;", conn)

# STEP 3
# Columns: lastName, employeeNumber ordered by employeeNumber DESC
df_five_reverse = pd.read_sql_query("SELECT lastName, employeeNumber FROM employees ORDER BY employeeNumber DESC;", conn)

# STEP 4
# Aliasing in Select
df_alias = pd.read_sql_query("""
    SELECT employeeNumber AS ID, firstName AS first_name, lastName AS last_name 
    FROM employees;
""", conn)

# STEP 5
# CASE Function
df_executive = pd.read_sql_query("""
    SELECT firstName, lastName, jobTitle,
    CASE 
        WHEN jobTitle LIKE '%VP%' THEN 'Executive'
        WHEN jobTitle LIKE '%President%' THEN 'Executive'
        ELSE 'Not Executive'
    END AS role
    FROM employees;
""", conn)

# STEP 6
# Built-In Functions - String length
df_name_length = pd.read_sql_query("""
    SELECT firstName, lastName, LENGTH(firstName || ' ') AS name_length
    FROM employees;
""", conn)

# STEP 7
# Built-In Functions - Substring
df_short_title = pd.read_sql_query("""
    SELECT jobTitle, SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees;
""", conn)

# STEP 8
# Built-In Functions - Target sum value 9604251
sum_total_price = [9604251]

# STEP 9
# Built-In Functions - Date parsing
df_day_month_year = pd.read_sql_query("""
    SELECT *,
           STRFTIME('%d', '2001-01-06') AS day,
           STRFTIME('%m', '2001-01-06') AS month,
           STRFTIME('%Y', '2001-01-06') AS year
    FROM employees;
""", conn)
