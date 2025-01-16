-- Exercise 8

-- What error do you receive if you attempt to add another primary key column to the films table?

-- Solution
ALTER TABLE films 
ADD PRIMARY KEY (director);
-- ERROR:  multiple primary keys for table "films" are not allowed
