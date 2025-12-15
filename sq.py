1] Create Database
create database database_name;                                                                                                   

create database practice;                                                                                           
use practice;                                                                                                                     show tables;


2] Create Table

    CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender CHAR(1),
    department_id INT,
    hire_date DATE,
    salary DECIMAL(10,2)
);

3] Insert

INSERT INTO employees (emp_id, first_name, last_name, gender, department_id, hire_date, salary)
VALUES
(101, 'Amit', 'Sharma', 'M', 1, '2018-03-12', 60000.00),
(102, 'Priya', 'Singh', 'F', 2, '2019-07-23', 75000.00),
(103, 'Ravi', 'Patel', 'M', 1, '2020-01-15', 55000.00),
(104, 'Sneha', 'Mehta', 'F', 3, '2017-10-30', 80000.00),
(105, 'Vikas', 'Yadav', 'M', 2, '2021-05-20', 45000.00),
(106, 'Anjali', 'Nair', 'F', 3, '2016-02-14', 90000.00);

Or

insert into employee values (107, 'Prabhat', 'Mahajan', 'M', 2, '2019-08-15', 370000);
4] Alter:

A] Add New Column

ALTER TABLE table_name ADD column_name datatype;

ALTER TABLE employees
ADD email VARCHAR(100);


B] Rename column

ALTER TABLE table_name RENAME COLUMN old_name TO new_name;

alter table employee rename column first_name to fname;

ALTER TABLE employees
RENAME TO employee_info;


C] Modify Datatype or size

ALTER TABLE emp MODIFY sal DECIMAL(12,2);

ALTER TABLE employees
MODIFY first_name VARCHAR(100);


D] Drop Column

ALTER TABLE table_name DROP COLUMN column_name;

ALTER TABLE employee DROP COLUMN email;


F] Add and drop constraint 

ALTER TABLE table_name
ADD CONSTRAINT constraint_name constraint_type (column_name);
ALTER TABLE table_name DROP CONSTRAINT constraint_name;
5] Drop & Truncate

A] Drop Database database_name
B] Drop table table_name
C] Truncate table table_name


6] Update

update emp SET sal = 2000 where empno = 7369;

UPDATE employee SET email = REPLACE(email, '@company.com', '@practice.com') WHERE email LIKE '%@company.com';

7] Delete

Delete from table_name where condition;

DELETE FROM employee
WHERE hire_date < '2017-01-01';

8] Select

    Select * from table name;

9] where

Select * from emp where id = 1;

10] Distinct

SELECT DISTINCT column_name FROM table_name;

Select distinct email from employee






11] Order by

SELECT * FROM table_name ORDER BY col_name ASC; 

SELECT fname, salary FROM employee
ORDER BY salary DESC;

13] Limit

SELECT * FROM table_name LIMIT 5;

SELECT * FROM employee
ORDER BY salary DESC
LIMIT 3;


14] Grant and Revoke

GRANT SELECT, INSERT ON dept TO 'user1'@'localhost';
REVOKE INSERT ON dept FROM 'user1'@'localhost';


15] AND OR NOT

SELECT * FROM employee
WHERE gender = 'M' AND department_id = 2;

SELECT * FROM employee
WHERE gender = 'F' OR salary > 80000;

SELECT * FROM employee
WHERE NOT department_id = 3;


16] Between

SELECT fname, salary FROM employee
WHERE salary BETWEEN 50000 AND 90000;


17] IN / NOT IN

SELECT fname, department_id FROM employee
WHERE department_id IN (1, 3);

SELECT * FROM employee
WHERE department_id NOT IN (2);


18] Like

SELECT * FROM employee
WHERE fname LIKE 'A%';

SELECT * FROM employee
WHERE email LIKE '%gmail.com';


19] IS NULL / IS NOT NULL

SELECT * FROM employee
WHERE email IS NULL;


20] Count Sum Avg Min Max

SELECT COUNT(*) AS total_employees FROM employee;
SELECT COUNT(*) AS total_females FROM employee
WHERE gender = 'F';

SELECT SUM(salary) AS total_salary FROM employee;
SELECT department_id, SUM(salary) AS total_dept_salary
FROM employee
GROUP BY department_id;

SELECT AVG(salary) AS average_salary FROM employee;
SELECT department_id, AVG(salary) AS avg_salary
FROM employee
GROUP BY department_id;

SELECT MIN(salary) AS lowest_salary,
MAX(salary) AS highest_salary
FROM employee;

SELECT department_id,
       COUNT(*) AS total_employees,
       AVG(salary) AS avg_salary,
       MAX(salary) AS highest,
       MIN(salary) AS lowest
FROM employee
GROUP BY department_id;


21] Upper Lower Length / SUBSTRING / CONCAT / TRIM / REPLACE

SELECT UPPER(fname) AS upper_name,
LOWER(last_name) AS lower_name
FROM employee;

SELECT fname, LENGTH(email) FROM employee;

SELECT TRIM('   Prabhat   ') AS cleaned_name;

SELECT CONCAT(fname, ' ', last_name) AS full_name FROM employee;
SELECT CONCAT(fname, ' (', email, ')') AS employee_contact FROM employee;

SELECT fname,
SUBSTRING(email, 1, 5) AS first_five_chars
FROM employee;

SELECT fname,
 REPLACE(email, '@gmail.com', '@practice.com') AS updated_email
FROM employee;

24] Date
 
 
 
 

25] Cast Convert

SELECT CAST('2025-06-12' AS DATE);
SELECT CONVERT('2025-06-12', DATE);


26] ROUND / CEIL / FLOOR / ABS

SELECT fname, salary, ROUND(salary / 12, 2) AS monthly_salary
FROM employee;

SELECT fname, CEIL(salary / 12) AS rounded_up_monthly
FROM employee;

SELECT fname, FLOOR(salary / 12) AS rounded_down_monthly
FROM employee;

SELECT fname, ABS(salary - 80000) AS difference_from_80k
FROM employee;



27] Group By

SELECT department_id, SUM(salary) AS total_salary
FROM employee
GROUP BY department_id;

SELECT gender, AVG(salary) AS avg_salary
FROM employee
GROUP BY gender;

28] Having 

SELECT department_id, SUM(salary) AS total_salary
FROM employee
GROUP BY department_id
HAVING SUM(salary) > 150000;


SELECT department_id, AVG(salary) AS avg_salary
FROM employee
WHERE hire_date > '2018-01-01'
GROUP BY department_id
HAVING AVG(salary) > 60000;

SELECT department_id, SUM(salary) AS total_salary
FROM employee
GROUP BY department_id WITH ROLLUP;



29]  Joins (Need atleast 1 same column)

Inner Join 
SELECT e.emp_id, e.fname, e.department_id, d.dept_name
FROM employee e
INNER JOIN department d
ON e.department_id = d.department_id;

Left Join 
SELECT e.emp_id, e.fname, d.dept_name
FROM employee e
LEFT JOIN department d
ON e.department_id = d.department_id;

Right Join
SELECT e.emp_id, e.fname, d.dept_name
FROM employee e
RIGHT JOIN department d
ON e.department_id = d.department_id;

Full outer join
SELECT e.emp_id, e.fname, d.dept_name
FROM employee e
LEFT JOIN department d ON e.department_id = d.department_id
UNION
SELECT e.emp_id, e.fname, d.dept_name
FROM employee e
RIGHT JOIN department d ON e.department_id = d.department_id;

Cross join
SELECT e.fname, d.dept_name
FROM employee e
CROSS JOIN department d;

Self join
SELECT e.fname AS Employee, m.fname AS Manager
FROM employee e
LEFT JOIN employee m ON e.manager_id = m.emp_id;

30] Subqueries / Nested queries

SELECT fname, salary
FROM employee
WHERE salary > (SELECT AVG(salary) FROM employee);

SELECT fname, department_id
FROM employee
WHERE department_id = (SELECT department_id FROM department WHERE dept_name = 'HR');

SELECT e.fname, e.salary, e.department_id
FROM employee e
WHERE e.salary > (
    SELECT AVG(salary)
    FROM employee
    WHERE department_id = e.department_id
);

SELECT 
    e.fname,
    e.department_id,
    e.salary,
    (SELECT AVG(salary) FROM employee WHERE department_id = e.department_id) AS dept_avg
FROM employee e;



31] Union / Union All / Intersect

SELECT fname, last_name FROM employee
UNION
SELECT fname, last_name FROM ex_employee;

SELECT email FROM employee
UNION
SELECT email FROM ex_employee;

SELECT fname, last_name FROM employee
UNION ALL
SELECT fname, last_name FROM ex_employee;

SELECT fname, last_name FROM employee
UNION ALL
SELECT fname, last_name FROM ex_employee;

SELECT fname, last_name
FROM employee
WHERE (fname, last_name) IN (
    SELECT fname, last_name FROM ex_employee
);


32] Primary key / Foreign Key / Unique / Not Null / Default / Check

ALTER TABLE employee
ADD CONSTRAINT pk_employee PRIMARY KEY (emp_id);

ALTER TABLE employee
ADD CONSTRAINT fk_department
FOREIGN KEY (department_id)
REFERENCES department(department_id);

ALTER TABLE employee
ADD CONSTRAINT unique_email UNIQUE (email);

ALTER TABLE employee
MODIFY fname VARCHAR(30) NOT NULL;
ALTER TABLE employee
ALTER salary SET DEFAULT 30000;

ALTER TABLE employee
ADD CONSTRAINT check_salary CHECK (salary >= 30000);

33] Indexes

CREATE INDEX idx_employee_department
ON employee (department_id);

CREATE UNIQUE INDEX idx_employee_email
ON employee (email);

CREATE INDEX idx_employee_name
ON employee (fname, last_name);

CREATE INDEX idx_emp_covering
ON employee (fname, last_name, email);

DROP INDEX idx_employee_department ON employee;

SHOW INDEXES FROM employee;

34] Views

CREATE VIEW view_name AS
SELECT columns
FROM table_name
WHERE condition;

DROP VIEW view_name;

CREATE VIEW vw_employee_basic AS
SELECT emp_id, fname, last_name, gender, department_id, email
FROM employee;




CREATE VIEW vw_employee_department AS
SELECT 
    e.emp_id,
    CONCAT(e.fname, ' ', e.last_name) AS full_name,
    e.gender,
    d.department_name,
    e.salary,
    e.hire_date
FROM employee e
JOIN department d ON e.department_id = d.department_id;

CREATE VIEW vw_salary_update AS
SELECT emp_id, salary
FROM employee
WHERE department_id = 2;

CREATE TABLE mv_department_salary AS
SELECT department_id, SUM(salary) AS total_salary
FROM employee
GROUP BY department_id;


30] Except
Returns rows from the first query that are not in the second query.SELECT deptno FROM emp EXCEPT SELECT deptno FROM dept;



40] User Grant Revoke 

Create user ‘user_name’@’localhost’ identified by ‘1223’;
Grant select on sample.* to ‘user_name’@’localhost’;	
REVOKE SELECT ON emp FROM user1;







41] Being Commit Rollback Savepoint

BEGIN;   -- or START TRANSACTION

START TRANSACTION;

UPDATE emp SET sal = sal + 500 WHERE deptno = 10;
SAVEPOINT sp1;

UPDATE emp SET sal = sal + 1000 WHERE deptno = 20;
ROLLBACK TO sp1;   -- undo dept 20 update, keep dept 10 update

COMMIT;   -- save dept 10 changes permanently 




WINDOW FUNCTION

1] ROW_NUMBER()

SELECT
    emp_id,
    fname,
    salary,
    ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num
FROM employee;

2] RANK()

SELECT
    emp_id,
    fname,
    salary,
    RANK() OVER (ORDER BY salary DESC) AS rank_no
FROM employee;

3] DENSE_RANK()

SELECT
    emp_id,
    fname,
    salary,
    DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rank_no
FROM employee;

4] LAG() — looks at the previous row’s value

SELECT
    emp_id,
    fname,
    salary,
    LAG(salary, 1) OVER (ORDER BY salary DESC) AS prev_salary
FROM employee;



5] LEAD() — looks at the next row’s value

SELECT
    emp_id,
    fname,
    salary,
    LEAD(salary, 1) OVER (ORDER BY salary DESC) AS next_salary
FROM employee;

6]  FIRST_VALUE() and LAST_VALUE()

SELECT
    emp_id,
    fname,
    department_id,
    salary,
    FIRST_VALUE(fname) OVER (PARTITION BY department_id ORDER BY salary DESC) AS top_earner
FROM employee;

SELECT
    emp_id,
    fname,
    department_id,
    salary,
    LAST_VALUE(fname) OVER (PARTITION BY department_id ORDER BY salary DESC
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS lowest_earner
FROM employee;


NTILE

SELECT
    emp_id,
    fname,
    salary,
    NTILE(4) OVER (ORDER BY salary DESC) AS quartile
FROM employee;
Aggregate Functions with OVER()

SUM() OVER()
Cumulative total of salary in order.
SELECT
    emp_id,
    fname,
    salary,
    SUM(salary) OVER (ORDER BY emp_id) AS running_total
FROM employee;


AVG() OVER()
Average salary per department (keeps all rows):
SELECT
    emp_id,
    fname,
    department_id,
    salary,
    AVG(salary) OVER (PARTITION BY department_id) AS avg_salary_dept
FROM employee;


COUNT() OVER()
Count employees per department.
SELECT
    emp_id,
    fname,
    department_id,
    COUNT(*) OVER (PARTITION BY department_id) AS dept_count
FROM employee;









SELECT
    emp_id,
    fname,
    department_id,
    salary,
    AVG(salary) OVER (PARTITION BY department_id) AS avg_dept_salary,
    RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS dept_rank,
    LAG(salary) OVER (PARTITION BY department_id ORDER BY salary DESC) AS prev_emp_salary
FROM employee;





























CTE

WITH cte_name AS (
    SELECT ... FROM ...
)
SELECT * FROM cte_name;

Simple Example — Basic CTE
🎯 Goal: Display employees whose salary > ₹80,000.
WITH high_salary AS (
    SELECT emp_id, fname, last_name, salary
    FROM employee
    WHERE salary > 80000
)
SELECT * FROM high_salary;








Checking constraints

CREATE TABLE details (
    name VARCHAR(30),
    address VARCHAR(40),
    age INT,
    mobile_num BIGINT PRIMARY KEY,
    CONSTRAINT chk_mobile CHECK (mobile_num BETWEEN 1000000000 AND 9999999999)
);
CONSTRAINT chk_name CHECK (CHAR_LENGTH(name) = 4)
CONSTRAINT chk_email CHECK (email LIKE '%@gmail.com')


WHERE salary NOT BETWEEN 80000 AND 400000;

WHERE hire_date BETWEEN '2018-01-01' AND '2020-12-31';

List employees whose first name has ‘i’ as the second character
SELECT * FROM employee WHERE fname LIKE '_i%';


