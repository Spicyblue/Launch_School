-- Exercise 7
-- Write a SQL statement that will return the title and age in years of each movie, 
-- with newest movies listed first:

-- Solution
SELECT title, extract("year" from current_date) - "year" AS age
  FROM films
  ORDER BY age ASC;

