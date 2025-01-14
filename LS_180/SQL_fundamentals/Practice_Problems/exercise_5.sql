-- Exercise 5
-- Write a SQL statement to determine the average (mean) temperature
-- (divide the sum of the high and low temperatures by two) for each day from
-- March 2, 2016 through March 8, 2016. Make sure to round each average value to one decimal place.

-- Solution
SELECT date, ROUND((high + low) / 2.0, 1) as average
  FROM temperatures
 WHERE date BETWEEN '2016-03-02' AND '2016-03-08';

--  A combination of BETWEEN/AND is the same as using date >= '2016-03-02' AND date <='2016-03-08'. 
--  The use of a SQL comparison predicate such as BETWEEN allows us to simplify our comparison a bit.