-- Exercise 5
-- Using the table created in #4, write the SQL statements to insert the data as shown in the listing.

--  name	            length	        wingspan	    family	        extinct
-- Spotted Towhee	    21.6	        26.7	        Emberizidae	    f
-- American Robin	    25.5	        36.0	        Turdidae	    f
-- Greater Koa Finch	19.0	        24.0	        Fringillidae	t
-- Carolina Parakeet	33.0	        55.8	        Psittacidae	    t
-- Common Kestrel	    35.5	        73.5	        Falconidae	    f

-- Solution
INSERT INTO birds (name, length, wingspan, family, extinct)
            VALUES ('Spotted Towhee', 21.6, 26.7, 'Emberizidae', false);

INSERT INTO birds (name, length, wingspan, family, extinct)
            VALUES ('American Robin', 25.5, 36.0, 'Turdidae', false);

INSERT INTO birds (name, length, wingspan, family, extinct)
            VALUES ('Greater Koa Finch', 19.0, 24.0, 'Fringillidae', true);

INSERT INTO birds (name, length, wingspan, family, extinct)
            VALUES ('Carolina Parakeet', 33.0, 55.8, 'Psittacidae', true);

INSERT INTO birds (name, length, wingspan, family, extinct)
            VALUES ('Common Kestrel', 35.5, 73.5, 'Falconidae', false);