-- DML/DDL/DCL Part 10
-- Does the following statement use the DDL or DML component of SQL?

CREATE SEQUENCE part_number_sequence;

-- Solution
-- The statement uses the DDL component of SQL since we create a new data.

-- LS Note
-- CREATE SEQUENCE statements modify the characteristics and attributes of a database
-- by adding a sequence object to the database structure.
-- It does not actually manipulate any data, but instead manipulates the data definitions.
-- As such, CREATE SEQUENCE statements are part of the DDL sublanguage.
-- It could also be argued that CREATE SEQUENCE is DML; 
-- the sequence object it creates is a bit of data that is used to keep track of a sequence of automatically generated values, 
-- so it can be thought of as being part of the data instead of a characteristic of the data.
-- However, all CREATE statements (not just CREATE SEQUENCE) are generally thought of as DDL.