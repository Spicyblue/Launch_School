'''
Example 5.

Which of the following classes would create objects that have an instance variable.
How do you know?

class Fruit:
    def __init__(self, name):
        my_name = name

class Pizza:
    def __init__(self, name):
        self.my_name = name

'''

# Solution
# The Pizza class alone would create an object that has an 
# instance variable `name` because this class has a defined `__init__` (a dunder init) 
# method which takes in one parameter for `name` and 
# assigns the value of `name` to the instance varaibe `my_name`.


## LS Solution ##

# Pizza class instances will have instance variables by virtue of 
# assigning a value to self.my_name in the Pizza.__init__ method. 
# Fruit class instances don't have instance variables since none are defined. 
# my_name is a local variable only defined inside Fruit.__init__.

# You can verify this by using the vars function
# to see what instance variables exist in Pizza and Fruit objects:

# print(vars(Fruit('orange')))     # {}
# print(vars(Pizza('pepperoni')))  # {'my_name': 'pepperoni'}

# In this example, we can see that the Fruit object has no instance variables,
# while the Pizza object has a my_name instance variable whose value is 'pepperoni'.