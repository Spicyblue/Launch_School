'''
Exercise 1
How do we create a class and an object in Python?

Write a program that defines a class and creates two objects from that class. 
The class should have at least one instance variable that gets initialized by the initializer.
What class you create doesn't matter, provided it satisfies the above requirements.
'''
# Solution
class Food:

    def __init__(self, name):
        # self. name is an instance varaible (state)
        # type_name is an instance object that returns the class name
        self.name = name
        type_name = type(self).__name__
        print(f'I am {name}, a {type_name}.')
        
    def spicy(self):
        # spicy is an instance method (behaviour)
        print(f'{self.name} is spicy!!' )

    def chilly(self):
        # spicy is an instance method (behaviour)
        print(f'{self.name} is filled with chilly!!' )

jollof_rice = Food('Jollof') # Constructor for jollof rice
akara = Food('Akara') # Constructor for akara

for foods in [jollof_rice, akara]:
    foods.spicy()

# outputs
# I am Jollof, a Food.
# I am Akara, a Food.
# Jollof is spicy!!
# Akara is spicy!!

## LS Answer ##
# class Person:

#     def __init__(self, name):
#         self.name = name

# bob = Person('Bob')
# alice = Person('Alice')
