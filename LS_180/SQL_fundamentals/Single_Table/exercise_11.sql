-- Exercise 10

-- Write a SQL query to determine how profitable each item on the menu is based on the amount 
-- of time it takes to prepare one item. 
-- Assume that whoever is preparing the food is being paid $13 an hour. 
-- List the most profitable items first. 
-- Keep in mind that prep_time is represented in minutes and ingredient_cost and menu_price are both in dollars and cents:

-- Solution

SELECT item, menu_price, ingredient_cost,
       round(prep_time/60.0 * 13.0, 2) AS labor,
       menu_price - ingredient_cost - round(prep_time/60.0 * 13.0, 2) AS profit
  FROM menu_items
  ORDER BY profit DESC;