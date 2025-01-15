-- Exercise 9

-- How is the constraint added in #7 displayed by \d films?

-- Solution

-- Check constraints:
--    "title_length" CHECK (length(title::text) >= 1)