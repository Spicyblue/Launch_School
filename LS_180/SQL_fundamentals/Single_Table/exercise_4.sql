-- Exercise 4
-- Write a SQL statement that will create a table named birds that can hold the following values:

--  name	            length	        wingspan	    family	        extinct
-- Spotted Towhee	    21.6	        26.7	        Emberizidae	    f
-- American Robin	    25.5	        36.0	        Turdidae	    f
-- Greater Koa Finch	19.0	        24.0	        Fringillidae	t
-- Carolina Parakeet	33.0	        55.8	        Psittacidae	    t
-- Common Kestrel	    35.5	        73.5	        Falconidae	    f


-- Solution
CREATE TABLE birds(
    id serial,
    name varchar(50),
    length numeric(4, 1),
    wingspan numeric(4, 1),
    family varchar(50),
    extinct boolean
);
