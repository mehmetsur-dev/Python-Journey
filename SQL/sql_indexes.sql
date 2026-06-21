CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    signup_date DATE
);

INSERT INTO customers (first_name, last_name, email, signup_date)
SELECT
    'First' || i,
    'Last' || i,
    'user' || i || '@example.com',
    DATE '2020-01-01' + (random() * 2000)::int
FROM generate_series(1, 100000) AS i;

SELECT COUNT(*) FROM customers;

EXPLAIN ANALYZE
SELECT * FROM customers WHERE email = 'user99999@example.com';

CREATE INDEX idx_customers_email
ON customers(email);

EXPLAIN ANALYZE
SELECT * FROM customers WHERE email = 'user99999@example.com';

INSERT INTO customers (first_name, last_name, email, signup_date)
SELECT
    'First' || i,
    'Last' || i,
    'user' || i || '@example.com',
    DATE '2020-01-01' + (random() * 2000)::int
FROM generate_series(100001, 110000) AS i;

SELECT * FROM customers;