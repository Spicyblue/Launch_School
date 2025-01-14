-- Exercise 8
-- A decision has been made to store rainfall data in inches. 
-- Write the SQL statements required to modify the rainfall column to reflect these new requirements.
-- A decision has been made to store rainfall data in inches.
-- Write the SQL statements required to modify the rainfall column to reflect these new requirements.

-- Solution
ALTER TABLE temperatures ALTER COLUMN rainfall TYPE numeric(6,3);
UPDATE temperatures SET rainfall = rainfall * 0.039;