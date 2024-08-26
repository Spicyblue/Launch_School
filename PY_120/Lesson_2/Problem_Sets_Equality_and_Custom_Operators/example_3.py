'''
Example 2

Consider the following class:

class Cat:
    def __init__(self, name):
        self.name = name

Create the methods needed so you can compare Cat objects for equality and inequality by their name value.
The comparisons should ignore case and should work for the == and !=operators.
If the right-hand operand is not a Cat object, the methods should return NotImplemented.

Be sure to write test cases to demonstrate that your methods work as intended.

'''

# Solution

class Cat:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name == other.name

    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name != other.name

class Dog:

    def __init__(self, name):
        self.name = name

pillow = Cat('Pillow')
harry = Cat('Harry')
new_pillow = Cat('Pillow')
is_pillow = Dog('Pillow')

print(pillow == new_pillow)     # outputs True
print(pillow == harry)          # outputs False
print(pillow ==  Cat('Pillow')) # outputs True
print(pillow == 'Pillow')       # outputs False
print(pillow != is_pillow)      # outputs True

## LS Solution ##

# class Cat:
#     def __init__(self, name):
#         self.name = name

#     def __eq__(self, other):
#         if not isinstance(other, Cat):
#             return NotImplemented

#         return self.name.casefold() == other.name.casefold()

#     def __ne__(self, other):
#         if not isinstance(other, Cat):
#             return NotImplemented

#         return self.name.casefold() != other.name.casefold()

# bugs = Cat('Bugs')
# bugs2 = Cat('Bugs')
# elmer = Cat('Elmer')

# print(bugs == elmer)                # False
# print(bugs == bugs2)                # True

# print(bugs != elmer)                # True
# print(bugs != bugs2)                # False

# print(bugs == 'Bugs')               # False
# print(bugs != 'Bugs')               # True