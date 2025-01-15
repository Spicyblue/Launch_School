-- Exercise 12

-- How is the constraint added in #11 displayed by \d films?.

-- Solution
-- Check constraints:
--    "film_year" CHECK (year >= 1900 AND year <= 2100)