CREATE TABLE test(
   id INTEGER,
   name VARCHAR(50),
   location VARCHAR(100)
);

INSERT INTO test (id, name, location) VALUES
(1, 'test1', NULL),
(2, 'test2', NULL),
(3, 'test3', NULL),
(4, 'test4', NULL),
(5, 'test5', NULL),
(6, 'test6', NULL),
(7, 'test7', NULL),
(8, 'test8', NULL);

SELECT * FROM test; 

UPDATE test
SET location = 'Berlin'
WHERE name = 'test1'

UPDATE test
SET Location = 'Unknown'
WHERE location IS NULL

UPDATE test
SET name = 'Mehmet',
location = 'Germany'
WHERE name = 'test5'

DELETE FROM test
WHERE name = 'test8'

DELETE FROM test
WHERE location = 'Unknown'