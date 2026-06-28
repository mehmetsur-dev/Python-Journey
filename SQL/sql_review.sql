CREATE TABLE py_students(
   id INT,
   first_name VARCHAR(100),
   last_name VARCHAR(100),
   age INT,
   grade INT
);

INSERT INTO py_students(id, first_name, last_name, age, grade) VALUES
(1, 'Sera', 'Clay', 21, 88),
(2, 'Mehmet', 'Sur', 21, 68);

SELECT *
FROM py_students
WHERE grade > 70
ORDER BY grade DESC;