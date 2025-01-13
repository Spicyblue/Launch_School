-- Exercise 2
-- Write SQL statements to insert the data shown iin the table.

-- name	        age	    occupation
-- Abby	        34	    biologist
-- Mu'nisah	    26	    NULL
-- Mirabelle	40	    contractor

-- Solution

INSERT INTO people (name, age, occupation) 
            VALUES ('Abby', 34 , 'biologist');
INSERT INTO people (id, name, age, occupation) 
            VALUES (DEFAULT, 'Mu''nisah', 26 , NULL);
INSERT INTO people (id, name, age, occupation) 
            VALUES (DEFAULT, 'Mirabelle', 40 , 'contractor');