-- 1. Create a Table
-- Now that we have an animals database, we can lay the groundwork needed to add some data to it.

-- Make a table called birds. It should have the following fields:

-- id (a primary key)
-- name (string with space for up to 25 characters)
-- age (integer)
-- species (a string with room for no more than 15 characters)

-- 2. Insert Data
-- For this exercise, we'll add some data to our birds table. Add five records to this database so that our data looks like:


-- id |   name   | age | species
----+----------+-----+---------
--  1 | Charlie  |   3 | Finch
--  2 | Allie    |   5 | Owl
--  3 | Jennifer |   3 | Magpie
--  4 | Jamie    |   4 | Owl
--  5 | Roy      |   8 | Crow

-- 3. Select Data
-- Write an SQL statement to query all data that is currently in our birds table.

-- 4. WHERE Clause
-- In this exercise, let's practice filtering the data we want to query. 
-- Using a WHERE clause, SELECT records for birds under the age of 5.

-- 5. Update Data
-- It seems there was a mistake when we were inserting data in the birds table. 
-- All the crows are actually ravens. 
-- Update the birds table so that the rows with a species of 'Crow' now read 'Raven'.

-- 6. Delete Data
-- Write an SQL statement that deletes the record that describes a 3 year-old finch.

-- 7. Add Constraint
-- When we initially created our birds table, we forgot to take into account a key factor: preventing certain values from being entered into the database. 
-- For instance, we would never find a bird that is negative n years old.
-- We could have included a constraint to ensure that bad data isn't entered for a database record, but we forgot to do so.
-- Write some code that ensures that only birds with a positive age may be added to the database.
-- Then write and execute an SQL statement to check that this new constraint works correctly.

-- 8. Drop Table
-- It seems we are done with our birds table, and no longer have a need for it in our animals database.
-- Write an SQL statement that will drop the birds table and all its data from the animals database.

-- 9. Drop Database
-- Let's finish things up by dropping the database animals. 
-- With no tables in it, we don't have much use for it any more.
--  Write a SQL statement or PostgreSQL command to drop the animals database.

-- Solutions

-- Create a database
CREATE DATABASE animals;

-- Notes  With PostgreSQL, the easiest way to do that is to use the Postgres wrapper function, createdb. 
-- But, if we want to stick with standard SQL, then we can use the CREATE DATABASE SQL command. 
-- Remember: to use CREATE DATABASE (and other SQL), you must use the psql console; 
-- to use createdb (and other wrapper functions) , you must use the regular terminal console.

-- Create a Table
CREATE TABLE birds(
  id serial PRIMARY KEY,
  name character varying(25),
  age integer,
  species character varying(15)
);
-- We want a primary key that auto-increments. For that last part, we'll use the pseudotype serial.
-- It auto-increments id for us as we create new bird rows in the table. 
-- This column should be a primary key, which ensures that id is NOT NULL and UNIQUE.
-- We also want name and species columns. Those will work as text. 
-- Here, we use character varying, though we could also use varchar or text.
-- The age column is last; we set it as type integer.

-- Insert Data
INSERT INTO birds (name, age, species)
VALUES ('Charlie', 3, 'Finch'),
('Allie', 5, 'Owl'),
('Jennifer', 3, 'Magpie'),
('Jamie', 4, 'Owl'),
('Roy', 8, 'Crow');
-- To add data to our birds table, we need to use the INSERT INTO SQL statement.
-- We specify a table, the column names we wish to deal with and the values we wish to insert under each of those column. 
-- Order is important here; when listing the VALUES, 
-- make sure the order of those values corresponds to the order of the column names.

-- Select Data
SELECT * FROM birds;

-- To query all the data in our table, we need to use a SELECT statement.
-- When writing our query, we may do either of two things: specify all columns in our table, 
-- or we may use the splat symbol (*).

-- WHERE Clause
SELECT * FROM birds WHERE age < 5;

-- Update Data
UPDATE birds SET species = 'Raven'
  WHERE species = 'Crow';
-- To update a row of data, we have to use the SQL statement UPDATE. 
-- We may SET one or more column values with the UPDATE statement. 
-- We don't need to specify column names that we don't need to update. 
-- The WHERE clause specifies the rows that need to be updated.

-- Delete Data
DELETE FROM birds WHERE age=3 AND species='Finch';
-- To delete a row from birds we must specify the table we wish to delete from, and we must specify some conditions that match just the rows we wish to delete. 
-- If we leave out the WHERE clause, then all rows in table birds will be deleted.
-- We use these two conditions in our WHERE clause. 
-- This differentiates between any other rows that may share some data with the one we wish to delete. 
-- To include more than one condition in a WHERE clause, recall that we may use: AND, OR.

-- Add Constraint
ALTER TABLE birds ADD CONSTRAINT check_age CHECK (age > 0);
INSERT INTO birds (age, name, species) VALUES (-2, 'Alan', 'Blue Jay');
-- After checking out the ALTER TABLE documentation, 
-- we'll notice that there are examples of how to add a constraint. 
-- We first specify ALTER TABLE followed by the table we wish to alter. 
-- Then, we specify an ADD CONSTRAINT clause, with a name of check_age (the name is your choice)
-- and an associated boolean expression as specified by the CHECK clause.

-- Drop Table
DROP TABLE IF EXISTS birds;
-- Note, We can specify multiple tables as well.
-- For instance, if there was also a reptiles table that we wanted to delete, we might write SQL like.

-- Drop Database
DROP DATABASE animals;
-- There are two ways to go about this.
-- We may explicitly write out the SQL for dropping this database with the SQL statement DROP DATABASE db_name. 
-- Note, that you will have to use the SQL statement below from another database other than animals. 
-- You cannot drop a database while you're still connected to it.

-- There is a wrapper function for dropping a database $ dropdb db_name which can be used on terminal.