-- Exercise 8

-- Write a SQL query that finds all films whose director has the first name John.

-- Solution

SELECT * FROM films WHERE director LIKE '%John%';