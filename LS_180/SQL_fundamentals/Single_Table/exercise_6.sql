-- Exercise 6
-- Write a SQL statement that finds the names and families for all birds that are not extinct, 
-- in order from longest to shortest (based on the length column's value).

-- Output 
--       name      |   family
-- ----------------+-------------
--  Common Kestrel | Falconidae
--  American Robin | Turdidae
--  Spotted Towhee | Emberizidae
-- (3 rows)


-- Solution
SELECT name, family from birds
    WHERE extinct = false
    ORDER BY length DESC;