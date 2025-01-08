-- DML/DDL/DCL Part 6
-- Does the following statement use the DDL or DML component of SQL?

UPDATE things
SET material = 'plastic'
WHERE item = 'Cup';

-- Solution
-- The following code uses DML component of SQL since we try to modify the data within the schema using UPDATE statement.

-- LS Note
-- UPDATE modifies specific rows of data in a database.
-- Therefore, it is part of the DML sublanguage since it manipulates the data and not the structure of the data.
