-- Exercise 8

-- What error is shown if the constraint created in #7 is violated?
-- Write a SQL INSERT statement that demonstrates this.

-- Solution

INSERT INTO films   (title , year, genre, director, duration) 
            VALUES  ('', 2020, 'Horror', 'Kage Mushin', 60);
-- ERROR:  new row for relation "films" violates check constraint "title_length"
-- DETAIL:  Failing row contains (, 2020, Horror, Kage Mushin, 60).