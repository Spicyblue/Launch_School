'''
Example 9.

Create a Bird class that has a species attribute.
Create a Sparrow class that inherits from the Bird class.
Create a Sparrow instance object, then print its species.
The expected output is sparrow.

'''

# Solution

class Bird:
    def __init__(self, species):
        self.species = species

class Sparrow(Bird):
    pass

birdie = Sparrow('sparrow')
print(birdie.species)              # sparrow

## LS Solution ##   
# class Bird:
#     def __init__(self, species):
#         self.species = species

# class Sparrow(Bird):
#     pass

# sparrow = Sparrow('sparrow')
# print(sparrow.species)              # sparrow
