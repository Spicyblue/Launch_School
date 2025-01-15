-- Exercise 4

-- Add a constraint to the table films that ensures that all films have a unique title.

-- Solution
ALTER TABLE films ADD CONSTRAINT title_unique UNIQUE (title);