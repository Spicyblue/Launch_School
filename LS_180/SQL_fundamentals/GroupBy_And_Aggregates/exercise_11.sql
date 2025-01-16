-- Exercise 11

-- Write a SQL query that will return the following data:

-- Write a SQL query that will return the following data:

--    genre   | total_duration
-- -----------+----------------
--  horror    |            113
--  thriller  |            113
--  action    |            132
--  crime     |            175
--  drama     |            198
--  espionage |            245
--  comedy    |            407
--  scifi     |            632
-- (8 rows)

-- Solution

SELECT genre, SUM(duration) as total_duration from films GROUP by genre ORDER BY total_duration ASC;