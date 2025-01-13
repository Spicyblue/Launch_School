-- Exercise 9
-- Write a SQL statement that returns the title of the longest film.

-- Solution
SELECT title FROM films ORDER BY duration DESC LIMIT 1;