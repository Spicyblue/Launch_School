-- DML/DDL/DCL Part 3
-- Does the following statement use the DDL or DML component of SQL?

CREATE TABLE things (
  id serial PRIMARY KEY,
  item text NOT NULL UNIQUE,
  material text NOT NULL
);

-- Solution
-- The code above uses DDL component of SQL since we are create a new schema within the database.

-- LS Notes
-- CREATE TABLE defines the type of information stored in a database table by describing the data and its attributes. 
-- It does not actually manipulate any data, but instead manipulates the data definitions. 
-- As such, CREATE TABLE statements are part of the DDL sublanguage.