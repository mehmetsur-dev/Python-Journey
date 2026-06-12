CREATE TABLE people (
    id INTEGER,
	name VARCHAR (50)
);

INSERT INTO people (id, name) VALUES (3, 'Sara')
INSERT INTO people (id, name) VALUES (4, 'Yusuf')
INSERT INTO people (id, name) VALUES (5, 'Lena')

ALTER TABLE people ADD COLUMN age INT;

INSERT INTO people (id, name, age) VALUES
(7, 'Nina', 31),
(8, 'Omar', 27),
(9, 'Julia', 29);

INSERT INTO people (name, age, id) VAlUES ('Tariq', 25, 6)

SELECT * FROM people;
SELECT * FROM people WHERE age > 28;

INSERT INTO people (id, name, age) VALUES (10, 'Fatima', 33)

SELECT * FROM people ORDER BY age DESC NULLS LAST