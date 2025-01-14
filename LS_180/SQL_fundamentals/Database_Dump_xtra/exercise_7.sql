-- Exercise 7
-- Write a SQL statement that will update the given_name values to be all uppercase 
-- for all users with an email address that contains teleworm.us.

-- Solution
UPDATE people SET given_name = UPPER(given_name) WHERE email LIKE '%teleworm.us';