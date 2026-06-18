CREATE TABLE base2(
   base_id SERIAL PRIMARY KEY,
   base_name VARCHAR(50),
   founded DATE
);

CREATE TABLE supply(
   supply_id SERIAL PRIMARY KEY,
   name VARCHAR(50),
   description VARCHAR(200),
   quantity INT
);

CREATE TABLE inventory(
   base_id INT REFERENCES base2(base_id),
   supply_id INT REFERENCES supply(supply_id),
   quantity INT
);

SELECT * FROM base2;
SELECT * FROM supply;
SELECT * FROM inventory;

INSERT INTO base2 (base_id, base_name, founded) VALUES
(1, 'Tharsisland', '2037-06-03'),
(2, 'Valles Marineris 2.0', '2040-12-01'),
(3, 'Gale Cratertown', '2041-08-15'),
(4, 'New New New York', '2042-02-10'),
(5, 'Olympus Mons Spa & Casino', NULL);

INSERT INTO supply (supply_id, name, description, quantity) VALUES
(1, 'Solar Panel', 'Standard 1x1 meter cell', 912),
(2, 'Water Filter', 'This takes things out of your water so it''s drinkable.', 6),
(3, 'Duct Tape', 'A 10 meter roll of duct tape for ALL your repairs.', 951),
(4, 'Ketchup', 'It''s ketchup...', 206),
(5, 'Battery Cell', 'Standard 1000 kAh battery cell for power grid (heavy item).', 17),
(6, 'USB 6.0 Cable', 'Carbon fiber coated / 15 TBps spool', 42),
(7, 'Fuzzy Duster', 'It gets dusty around here.  Be prepared!', 19),
(8, 'Mars Bars', 'The ORIGINAL nutrient bar made with the finest bioengineered ingredients.', 3801),
(9, 'Air Filter', 'Removes 99% of all Martian dust from your ventilation unit.', 23),
(10, 'Famous Ray''s Frozen Pizza', 'This Martian favorite is covered in all your favorite toppings.  1 flavor only.', 823);

INSERT INTO inventory (base_id, supply_id, quantity) VALUES
(1, 1, 8),
(1, 3, 5),
(1, 5, 1),
(1, 6, 2),
(1, 8, 12),
(1, 9, 1),
(2, 4, 5),
(2, 8, 62),
(2, 10, 37),
(3, 2, 11),
(3, 7, 2),
(4, 10, 91);

SELECT * FROM base2;
SELECT * FROM supply;
SELECT * FROM inventory;

CREATE VIEW base_storage AS
SELECT b.base_id, s.supply_id, s.name,
       COALESCE(
	   (SELECT quantity FROM inventory
	    WHERE base_id = b.base_id AND supply_id = s.supply_id), 0)
		AS quantity
FROM base2 AS b
CROSS JOIN supply AS s;

SELECT * FROM base_storage;