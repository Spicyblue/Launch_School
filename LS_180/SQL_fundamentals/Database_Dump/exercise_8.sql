-- Exercise 8
-- Write a SQL statement that will return the title and duration of each movie longer than two hours,
-- with the longest movies first.

-- Solution
SELECT title, duration FROM films WHERE duration > 120 ORDER BY duration DESC;