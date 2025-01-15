-- Exercise 14

-- How does the constraint created in #13 appear in \d films?

-- Solution
-- Check constraints:
--     "director_name" CHECK (length(director::text) >= 3 AND POSITION((' '::text) IN (director)) > 0)