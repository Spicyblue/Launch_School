-- Exercise 3
-- Write 3 SQL queries that can be used to retrieve the second row of the table shown in #1 and #2.
-- name	        age	    occupation
-- Abby	        34	    biologist
-- Mu'nisah	    26	    NULL       <--- This row
-- Mirabelle	40	    contractor

-- Solution
SELECT * from people 
    where age = 26;

SELECT * from people 
    ORDER BY age ASC
    LIMIT = 1;

SELECT * from people 
    where occupation IS NULL;