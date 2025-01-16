-- Exercise 6

-- Write a SQL query that determines the average duration 
-- for each genre in the films table, rounded to the nearest minute.

-- Solution

SELECT genre, ROUND(avg(duration)) as avg_duraion FROM films GROUP BY genre;
