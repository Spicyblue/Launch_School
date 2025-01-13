-- Exercise 6

-- Write SQL statements to insert the following data into the films table:

-- title	                        year    genre	    director	            duration
-- 1984	                            1956	scifi	    Michael Anderson	    90
-- Tinker Tailor Soldier Spy	    2011	espionage	Tomas Alfredson	        127
-- The Birdcage	                    1996	comedy	    Mike Nichols	        118

-- Solution
INSERT INTO films(title, "year", genre, director, duration)
            VALUES ('1984', 1956, 'scifi', 'Michael Anderson', 90);

INSERT INTO films(title, "year", genre, director, duration)
            VALUES ('Tinker Tailor Soldier Spy', 2011, 'espionage', 'Tomas Alfredson', 127);

INSERT INTO films(title, "year", genre, director, duration)
            VALUES ('The Birdcage', 1996, 'comedy', 'Mike Nichols', 118);
