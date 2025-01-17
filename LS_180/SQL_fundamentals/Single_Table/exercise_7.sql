-- Exercise 7
-- Use SQL to determine the average, minimum, and maximum wingspan for the birds shown in the table.

--  name	            length	        wingspan	    family	        extinct
-- Spotted Towhee	    21.6	        26.7	        Emberizidae	    f
-- American Robin	    25.5	        36.0	        Turdidae	    f
-- Greater Koa Finch	19.0	        24.0	        Fringillidae	t
-- Carolina Parakeet	33.0	        55.8	        Psittacidae	    t
-- Common Kestrel	    35.5	        73.5	        Falconidae	    f


-- Solution
SELECT round(avg(wingspan), 1) , min(wingspan), max(wingspan) from birds;
