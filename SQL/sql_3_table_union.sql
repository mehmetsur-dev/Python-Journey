CREATE TABLE fingerprint_evidence(
   evidence_id SERIAL PRIMARY KEY,
   location_found VARCHAR(250),
   match_name VARCHAR(100),
   date_collected DATE
);

CREATE TABLE witness_statements(
   statement_id SERIAL PRIMARY KEY,
   location_given VARCHAR(250),
   person_name VARCHAR(100),
   date_collected DATE
);

CREATE TABLE security_footage(
   footage_id SERIAL PRIMARY KEY,
   location_captured VARCHAR(250),
   person_identified VARCHAR(100),
   date_collected DATE
);

INSERT INTO fingerprint_evidence
   (location_found, match_name, date_collected)
VALUES
   ('Kitchen window', 'John Carter', '2026-06-10'),
   ('Front door handle', 'Unknown', '2026-06-11');

INSERT INTO security_footage
   (location_captured, person_identified, date_collected)
VALUES
   ('Garden', '6''1 Tall White male', '2026-5-22'),
   ('Park', '5''5 Tall Female', '2026-5-26');

INSERT INTO witness_statements
   (location_given, person_name, date_collected)
VALUES
   ('Street 10s', 'Alex John', '2026-6-10'),
   ('Target', 'Sera Doe', '2026-5-28');


SELECT CONCAT('f', evidence_id) AS id, location_found, match_name, date_collected
FROM fingerprint_evidence
   UNION
SELECT CONCAT('w', statement_id) AS id, location_given, person_name, date_collected
FROM witness_statements
   UNION
SELECT CONCAT('s', footage_id) AS id, location_captured, person_identified, date_collected
FROM security_footage;

SELECT * FROM fingerprint_evidence;
SELECT * FROM witness_statements;
SELECT * FROM security_footage;