-- Exercise 13

-- Add a constraint to films that requires all rows to have a value for director 
-- that is at least 3 characters long and contains at least one space character ().

-- Solution
ALTER TABLE films ADD CONSTRAINT director_name
    CHECK (length(director) >= 3 AND position(' ' in director) > 0);