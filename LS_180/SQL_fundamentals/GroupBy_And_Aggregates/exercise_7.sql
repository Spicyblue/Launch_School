-- Exercise 7

-- Write a SQL query that determines the average duration of movies for each decade represented in the films table, 
-- rounded to the nearest minute and listed in chronological order.

-- Solution

SELECT year / 10 * 10 as decade, ROUND(AVG(duration)) as average_duration
  FROM films GROUP BY decade ORDER BY decade;

