-- Select Data
-- Write an SQL statement to query all data that is currently in our birds table.

-- Solution

SELECT * from birds

-- LS Solution

SELECT * FROM birds;

-- or we can specify all the columns we wish to query

SELECT id, name, age, species FROM birds;

-- Whether you use parentheses around the columns you wish to query is important. 
-- Leave the parentheses off and we get 4 individual columns returned in a table. 
-- Include parentheses, and all our data gets grouped together into one column, like so:

SELECT (id,name,age,species) FROM birds;
-----------------------
--  (1,Charlie,3,Finch)
--  (2,Allie,5,Owl)
--  (3,Jennifer,3,Magpie)
--  (4,Jamie,4,Owl)
--  (5,Roy,8,Crow)
-- (5 rows)
