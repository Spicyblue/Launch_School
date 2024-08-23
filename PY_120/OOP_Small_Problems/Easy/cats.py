'''
Complete the Program - Cats!
Consider the following program.

class Pet:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

class Cat(Pet):
    pass

cocoa = Cat('Cocoa', 3, 'black')
cheddar = Cat('Cheddar', 4, 'yellow and white')

print(cocoa.info)
print(cheddar.info)

# Update this code so you see the following output when you run the code:

# My cat Cocoa is 3 years old and has black fur.
# My cat Cheddar is 4 years old and has yellow and white fur.

'''

# Solution

class Pet:
    def __init__(self, name, age, color):
        self._name = name
        self._age = age
        self._color = color

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def color(self):
        return self._color 
    
    @property
    def info(self):
        return F" My cat {self._name} is {self._age} years old and has {self._color} fur."
    
class Cat(Pet):
    pass 

cocoa = Cat('Cocoa', 3, 'black')
cheddar = Cat('Cheddar', 4, 'yellow and white')

print(cocoa.info)
print(cheddar.info)

# Update this code so you see the following output when you run the code:

# My cat Cocoa is 3 years old and has black fur.
# My cat Cheddar is 4 years old and has yellow and white fur.


# A rectangle's area is given by its width times its height.

## LS Solution ##

# class Pet:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     @property
#     def name(self):
#         return self._name

#     @property
#     def age(self):
#         return self._age

# class Cat(Pet):
#     def __init__(self, name, age, colors):
#         super().__init__(name, age)
#         self._colors = colors

#     @property
#     def colors(self):
#         return self._colors

#     @property
#     def info(self):
#         return (f"My cat {self.name} is {self.age} "
#                 f"years old and has {self.colors} fur.")