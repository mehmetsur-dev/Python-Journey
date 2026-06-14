CREATE TABLE base(
   base_id SERIAL PRIMARY KEY,
   base_name VARCHAR(100)
);

CREATE TABLE martian(
   martian_id SERIAL PRIMARY KEY,
   name VARCHAR(100),
   base_id INT REFERENCES base(base_id)
);

INSERT INTO base (base_name) VALUES
('Tharsisland'),
('Valles Marineris 2.0'),
('Gale Cratertown'),
('New New New York');

INSERT INTO martian (name, base_id) VALUES
('Alice', 1),
('Bob', 4),
('Carol', 4),
('Dave', 1),
('Eve', 2),
('Frank', 3),
('Grace', 3),
('Hank', 2);

SELECT m.name, b.base_name
FROM martian AS m
INNER JOIN base AS b
ON m.base_id = b.base_id;

INSERT INTO martian
(name, base_id) VALUES ('Zara', NULL);

SELECT m.name, b.base_name
FROM martian AS m
LEFT JOIN base AS b
ON m.base_id = b.base_id;

SELECT m.name
FROM martian AS m
LEFT JOIN base AS b
ON m.base_id = b.base_id
WHERE b.base_id IS NULL;

SELECT b.base_name, COUNT(m.name) 
FROM martian AS m
RIGHT JOIN base AS b
ON m.base_id = b.base_id
GROUP BY b.base_name
ORDER BY COUNT(m.name) DESC;

SELECT * FROM base;
SELECT * FROM martian;
