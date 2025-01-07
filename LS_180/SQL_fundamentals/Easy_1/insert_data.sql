-- Insert Data
-- For this exercise, we'll add some data to our birds table. Add five records to this database so that our data looks like:


-- id |   name   | age | species
----+----------+-----+---------
--  1 | Charlie  |   3 | Finch
--  2 | Allie    |   5 | Owl
--  3 | Jennifer |   3 | Magpie
--  4 | Jamie    |   4 | Owl
--  5 | Roy      |   8 | Crow

-- Solutions

Insert into birds   (id, name, age, species)
            values  (1, Charlie, 3, Finch),
                    (2, Allie, 3, Owl),
                    (3, Jennifer, 3, Magpie),
                    (4, Jamie, Owl), 
                    (5, Roy, 8, Crow);