-- Exercise 7

-- What error do you receive if you attempt to update a row to have a value for id that is used by another row?

-- Solution

INSERT INTO films   (title , year, genre, director, duration, id)
            VALUES  ('wahaha', '2039', 'unknwon', 'Mc Fluffy fluff', 15, 2);
-- ERROR:  duplicate key value violates unique constraint "films_pkey"
-- DETAIL:  Key (id)=(2) already exists.