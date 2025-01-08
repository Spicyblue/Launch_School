-- DML/DDL/DCL Part 2
-- Does the following statement use the Data Definition Language (DDL) 
-- or the Data Manipulation Language (DML) component of SQL?

SELECT column_name FROM my_table;

-- Solutiom
-- The statement above uses DML component of SQL since we are trying to retieve a particular data from the schema.

-- LS Note
-- SELECT merely queries (reads) the data in a database. 
-- Since it manipulates the data and not the structure of the data, 
-- SELECT is part of the DML sublanguage.