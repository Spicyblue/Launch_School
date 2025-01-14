-- Exercise 4
-- Write a SQL query that lists each domain used in an email address in the people table and 
-- how many people in the database have an email address containing that domain.
-- Domains should be listed with the most popular first.
-- Output should look like this
--      domain     | count
-- ----------------+-------
--  cuvox.de       |  1036
--  gustr.com      |  1029
--  rhyta.com      |  1024
--  superrito.com  |  1018
--  armyspy.com    |  1006
--  jourrapide.com |  1000
--  teleworm.us    |   998
--  dayrep.com     |   966
--  einrot.com     |   965
--  fleckens.hu    |   958
-- (10 rows)

-- Solution
SELECT substr(email, strpos(email, '@') + 1) as domain,
         COUNT(id)
  FROM people
  GROUP BY domain
  ORDER BY count DESC;