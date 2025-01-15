-- Exercise 3

-- How does modifying a column to be NOT NULL affect how it is displayed by \d films?

-- Solution
-- not null will be included in that column's Modifiers column:

-- \d films 
--                                     Table "public.films"
--   Column  |          Type          | Collation | Nullable |             Default             
-- ----------+------------------------+-----------+----------+---------------------------------
--  title    | character varying(255) |           | not null | (NOT NULL::boolean)
--  year     | integer                |           | not null | EXTRACT(year FROM CURRENT_DATE)
--  genre    | character varying(100) |           | not null | (NOT NULL::boolean)
--  director | character varying(255) |           | not null | (NOT NULL::boolean)
--  duration | integer                |           | not null | 0

-- Note: the output of \d varies between versions of PostgreSQL. 
-- The look is basically the same, but the column names may be different, 
-- and there may be other columns present. 
-- In particular, the 'Nullable' column name may be different.