-- Exercise 1
-- Write a SQL statement that will create the following table, people:

-- name	        age	    occupation
-- Abby	        34	    biologist
-- Mu'nisah	    26	    NULL
-- Mirabelle	40	    contractor

-- Solution
CREATE TABLE people(
    id serial,
    name varchar(30),
    age integer,
    occupation varchar(50),
);