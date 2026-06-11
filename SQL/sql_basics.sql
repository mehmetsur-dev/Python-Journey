CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    department VARCHAR(50)
);

INSERT INTO employees (name, age, department)
VALUES ('Mehmet', 28, 'Engineering'),
       ('Ali', 35, 'Marketing'),
       ('Sara', 25, 'Engineering'),
       ('Hans', 40, 'Finance');

SELECT * FROM employees;
SELECT name FROM employees;
SELECT * FROM employees WHERE department = 'Engineering';
SELECT * FROM employees WHERE age > 30;
SELECT name, age FROM employees WHERE department = 'Engineering' AND age > 30;
SELECT * FROM employees ORDER BY age DESC;
SELECT * FROM employees ORDER BY age;
SELECT AVG(age) FROM employees;