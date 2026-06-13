CREATE TABLE students(
    id INTEGER,
	first_name VARCHAR(20),
	last_name VARCHAR(20),
	age INT,
	occupation VARCHAR(20)
);

INSERT INTO students (id, first_name, last_name, age, occupation) VALUES
(1, 'Alice', 'Johnson', 22, 'Student'),
(2, 'Michael', 'Smith', 28, 'Engineer'),
(3, 'Elena', 'Rodriguez', 35, 'Designer'),
(4, 'David', 'Chen', 24, 'Data Analyst'),
(5, 'Sarah', 'Williams', 29, 'Marketing'),
(6, 'James', 'Brown', 31, 'Teacher'),
(7, 'Olivia', 'Taylor', 26, 'Developer'),
(8, 'Daniel', 'Miller', 40, 'Manager'),
(9, 'Sophia', 'Davis', 23, 'Intern'),
(10, 'Liam', 'Wilson', 27, 'Architect');

SELECT * FROM students;

SELECT * FROM students 
WHERE occupation = 'Student';

SELECT * FROM students
WHERE age > 25
AND (occupation = 'Developer'
OR occupation = 'Engineer'
OR occupation = 'Architect');

SELECT * FROM students ORDER BY age ASC;

SELECT * FROM students ORDER BY last_name DESC;

SELECT first_name, age, occupation FROM students
WHERE age > 25
ORDER BY age DESC
