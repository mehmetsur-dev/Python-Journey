CREATE TABLE martian_confidential(
   martian_id SERIAL PRIMARY KEY,
   first_name VARCHAR(100),
   last_name VARCHAR(100),
   base_id INT,
   super_id INT,
   salary INT,
   dna_id VARCHAR(200)
);

CREATE TABLE visitor(
   visitor_id SERIAL PRIMARY KEY,
   host_id INT,
   first_name VARCHAR(100),
   last_name VARCHAR(100)
);

INSERT INTO visitor (host_id, first_name, last_name) VALUES
(1, 'SiSU', 'Doe'),
(2, 'John', 'Johns'),
(3, 'Alex', 'Perry'),
(4, 'Sera', 'Clay');

INSERT INTO martian_confidential (first_name, last_name, base_id, super_id, salary, dna_id)
VALUES
('Ray', 'Bradbury', 1, NULL, 155900, 'gctaggaatgtagaatctcctgttg'),
('John', 'Black', 4, 10, 120100, 'cagttaatggttgaagctggggatt'),
('Samuel', 'Hinkston', 4, 2, 110000, 'cgaagcgctagatgctgtgttgtag'),
('Jeff', 'Spender', 1, 9, 10000, 'gactaatgtcttcgtggattgcaga'),
('Sam', 'Parkhill', 2, 12, 125000, 'gttactttgcgaaagccgtggctac'),
('Elma', 'Parkhill', 3, 8, 137000, 'gcaggaatggaagcaactgccatat'),
('Melissa', 'Lewis', 1, 1, 145250, 'cttcgatcgtcaatggagtccggac'),
('Mark', 'Watney', 3, NULL, 121100, 'gacacgaggcgaactatgtcgcggc'),
('Beth', 'Johanssen', 1, 1, 130000, 'cttagactaggtgtgaaacccgtta'),
('Chris', 'Beck', 4, NULL, 125000, 'gggggggttacgacgaggaatccat'),
('Nathaniel', 'York', 4, 2, 105000, 'ggctccctgggcgggatattggatg'),
('Elon', 'Musk', 2, NULL, 155800, 'atctgcttggatcaatagcgctgcg'),
('John', 'Carter', NULL, 8, 129500, 'ccaatcgtgcgagtcgcgatagtct');

CREATE VIEW martian_public AS
SELECT martian_id, first_name, last_name, base_id, super_id
FROM martian_confidential;

CREATE VIEW people_on_mars AS
SELECT CONCAT('m', martian_id) AS id, first_name, last_name, 'martian' AS status
FROM martian_public
    UNION
SELECT CONCAT('v', visitor_id) AS id, first_name, last_name, 'visitor' AS status
FROM visitor;

SELECT * FROM people_on_mars
WHERE status = 'visitor'
ORDER BY last_name;

SELECT status, COUNT(*)
FROM people_on_mars
GROUP BY status
HAVING COUNT(*) > 4;

SELECT super_id, AVG(salary)
FROM martian_confidential
WHERE super_id IS NOT NULL
GROUP BY super_id
HAVING COUNT(*) > 1;