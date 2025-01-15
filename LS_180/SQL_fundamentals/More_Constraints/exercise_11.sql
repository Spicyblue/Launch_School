-- Exercise 11

-- Add a constraint to the table films that ensures that all films have a year between 1900 and 2100.

-- Solution
ALTER TABLE films
ADD CONSTRAINT film_year CHECK (year BETWEEN 1900 AND 2100);
