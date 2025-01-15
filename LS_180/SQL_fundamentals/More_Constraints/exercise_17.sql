-- Exercise 16

-- Is it possible to define a default value for a column that will be considered invalid by a constraint? 
-- Create a table that tests this.

-- Solution
CREATE TABLE shoes (
    name text,
    size numeric(3,1) DEFAULT 0
    );
ALTER TABLE shoes ADD CONSTRAINT shoe_size CHECK (size BETWEEN 1 AND 15);
INSERT INTO shoes (name) VALUES ('blue sneakers');
-- ERROR:  new row for relation "shoes" violates check constraint "shoe_size"
-- DETAIL:  Failing row contains (blue sneakers, 0.0).