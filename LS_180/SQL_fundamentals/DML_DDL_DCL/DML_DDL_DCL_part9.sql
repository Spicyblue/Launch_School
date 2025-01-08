-- DML/DDL/DCL Part 9

-- Does the following statement use the DDL or DML component of SQL?
DROP DATABASE xyzzy;

-- Solution
-- The solutions uses the DDL component of SQL since we try to DROP a database.

-- LS Solution
-- This one is a bit ambiguous. Depending on how you look at DROP DATABASE, 
-- you might think it is part of the DML, part of the DDL, or both.
-- DROP DATABASE removes all data from the database, including any and all tables in the database. 
-- In this respect, it manipulates data, so some people think of it as part of DML. 
-- However, DROP DATABASE also deletes everything about the structure of the database and its tables.
-- Furthermore, all variants of the DROP statement are generally treated as DDL.
-- In these respects, DROP DATABASE manipulates how the data is structured,
-- so it is considered part of the DDL sublanguage.