-- Exercise 3
-- Write a SQL statement that returns all rows in the films table with a title shorter than 12 letters.

 SELECT * FROM films WHERE length(title) <= 12;