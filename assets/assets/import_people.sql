DROP TABLE IF EXISTS people;
CREATE TABLE people (id serial PRIMARY KEY, first_name TEXT, last_name TEXT, occupation TEXT);

\copy people(first_name, last_name, occupation) FROM '/assets/people.csv' DELIMITER ',' CSV HEADER