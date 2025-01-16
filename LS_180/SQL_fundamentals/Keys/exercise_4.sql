-- Exercise 4

-- Is it possible to create a sequence that returns only even numbers? 
-- The documentation for sequence might be useful.

-- Solution

CREATE SEQUENCE even_numbers_seq
    INCREMENT BY 2
    START WITH 2
    MINVALUE 2
    NO MAXVALUE
    CACHE 1;

SELECT nextval('even_numbers_seq')