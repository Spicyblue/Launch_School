-- Exercise 9

-- Write SQL statements to insert the data shown in #8 into the table.
-- item	        prep_time	    ingredient_cost	    sales	    menu_price
-- omelette	    10	            1.50	            182	        7.99
-- tacos	    5	            2.00	            254	        8.99
-- oatmeal	    1	            0.50	            79	        5.99

-- Solution

INSERT INTO menu_items (item, prep_time, ingredient_cost, sales, menu_price)
            VALUES('omelette', 10, 1.50, 182, 7.99);

INSERT INTO menu_items (item, prep_time, ingredient_cost, sales, menu_price)
            VALUES('tacos', 5, 2.00, 254, 8.99);

INSERT INTO menu_items (item, prep_time, ingredient_cost, sales, menu_price)
            VALUES('oatmeal', 1, 0.50, 79, 5.99);
