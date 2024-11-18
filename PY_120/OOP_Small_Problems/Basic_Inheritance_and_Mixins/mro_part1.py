'''
Method Resolution Path (Part 1).
Using the code below, determine the method resolution order (MRO) used when accessing cat1.color.
Only list the classes that are checked by Python when searching for the color attribute. 
Do not use the mro method.

Copy Code
class Animal:
    def __init__(self, color):
        self.color = color

class Cat(Animal):
    pass

class Bird(Animal):
    pass

cat1 = Cat('Black')
print(cat1.color)

'''

# Solution

class Animal:
    def __init__(self, color):
        self.color = color

class Cat(Animal):
    pass

class Bird(Animal):
    pass

cat1 = Cat('Black')
print(cat1.color)

# Cat then Animal

## LS Solution ##

# Cat
# Animal
