'''
Example 10.

Consider the following code:

class Bird:
    def __init__(self, species):
        self.species = species

class Sparrow(Bird):
    def __init__(self, species, color):
        self.color = color

birdie = Sparrow("sparrow", "brown")
print(birdie.species)               # What will this output?
Without running the above code, what will it output? If it raises an error, explain why and how to fix it.

'''

# Solution

class Bird:
    def __init__(self, species):
        self.species = species

class Sparrow(Bird):
    def __init__(self, species, color):
        super().__init__(species)
        self.color = color

birdie = Sparrow("sparrow", "brown")
print(birdie.species)

# This will raise an AttributeError: 'Sparrow' object has no attribute 'species' because we dont have any instance variable for species defined in the class Sparrow. Although we have an __init__ method in the parent class with an instance variable for species, this however never get instantiated. To fix this problem, we must call Bird.__init__ from inside Sparrow.__init__ using super().__init__(species) statement.

## LS Solution ##   
# This code will raise an AttributeError since the Sparrow class doesn't initialize the species instance variable. To fix this problem, we must call Bird.__init__ from inside Sparrow.__init__:

# class Bird:
#     def __init__(self, species):
#         self.species = species

# class Sparrow(Bird):
#     def __init__(self, species, color):
#         super().__init__(species)
#         self.color = color

# birdie = Sparrow("sparrow", "brown")
# print(birdie.species)               # sparrow
