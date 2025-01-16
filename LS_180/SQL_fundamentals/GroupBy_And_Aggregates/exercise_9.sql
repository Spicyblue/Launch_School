-- Exercise 9

-- Write a SQL query that will return the following data:

--    genre   | count
-- -----------+-------
--  scifi     |     5
--  comedy    |     4
--  drama     |     2
--  espionage |     2
--  crime     |     1
--  thriller  |     1
--  horror    |     1
--  action    |     1
-- (8 rows)

-- Solution

SELECT genre, COUNT(genre) as count FROM films GROUP by genre ORDER BY count DESC;