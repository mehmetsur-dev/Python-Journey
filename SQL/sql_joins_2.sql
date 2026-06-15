-- Students
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(100)
);

-- scores
CREATE TABLE scores (
  id SERIAL PRIMARY KEY,
  student_id INT REFERENCES students(id),
  subject VARCHAR(100),
  score INT
);

INSERT INTO scores (student_id, subject, score) VALUES
(1, 'Math', 88),
(1, 'Science', 72),
(2, 'Math', 95),
(4, 'Science', 60);

SELECT s.name, sc.score
FROM students AS s
INNER JOIN scores AS sc
ON s.id = sc.student_id;

SELECT s.name, sc.score
FROM students AS s
LEFT JOIN scores AS sc
ON s.id = sc.student_id

SELECT s.name, sc.score
FROM students AS s
LEFT JOIN scores AS sc
ON s.id = sc.student_id
WHERE sc.score IS NULL

SELECT s.name, sc.score
FROM students AS s
INNER JOIN scores AS sc
ON s.id = sc.student_id
WHERE sc.score > 80;

SELECT s.name, sc.score
FROM students AS s
INNER JOIN scores AS sc
ON s.id = sc.student_id
ORDER BY sc.score DESC;

SELECT s.name, ROUND(AVG (sc.score), 2)
FROM students AS s
INNER JOIN scores AS sc
ON s.id = sc.student_id
GROUP BY s.name;

SELECT s.name, ROUND(AVG(sc.score), 2)
FROM students AS s
INNER JOIN scores AS sc
ON s.id = sc.student_id
GROUP BY s.name
HAVING AVG(sc.score) > 70;

SELECT s.name, SUM(sc.score)
FROM students AS s
INNER JOIN scores AS sc
ON s.id = sc.student_id
WHERE city = 'Berlin'
GROUP BY s.name
ORDER BY SUM(sc.score) DESC;

SELECT * FROM students;
SELECT * FROM scores;