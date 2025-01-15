-- Exercise 15

-- Write an UPDATE statement that attempts to change the director for "Die Hard" to "Johnny". 
-- Show the error that occurs when this statement is executed.

-- Solution
UPDATE films SET director = 'Johnny' WHERE title = 'Die Hard';
-- ERROR:  new row for relation "films" violates check constraint "director_name"
-- DETAIL:  Failing row contains (Die Hard, 1988, action, Johnny, 132).