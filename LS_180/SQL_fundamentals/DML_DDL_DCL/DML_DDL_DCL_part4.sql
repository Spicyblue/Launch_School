-- DML/DDL/DCL Part 4
-- Does the following statement use the DDL or DML component of SQL?

ALTER TABLE things
DROP CONSTRAINT things_item_key;

-- Solution
-- The code uses DDL components of SQL since we alter the data within the schema.

-- Solution
-- ALTER TABLE modifies the characteristics and attributes of a table. 
-- It does not actually manipulate any data, but instead manipulates the data definitions. 
-- As such, ALTER TABLE statements are part of the DDL sublanguage.