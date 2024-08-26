'''
Example 3

Using the answer to the previous problem, create the methods needed
so you can perform ordered comparisons of Cat objects by their name value. 
As with the previous problem, the comparison should ignore case.
They should work for the <, <=, >, and >= operators. 
If the right-hand operand is not a Cat object, the methods should return NotImplemented.

'''

# Solution

class Cat:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):          # self == other
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name == other.name

    def __ne__(self, other):           # self != other
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name != other.name
    
    def __lt__(self, other):            # self < other
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name < other.name

    def __le__(self, other):            # self <= other
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name <= other.name

    def __gt__(self, other):            # self > other
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name > other.name

    def __ge__(self, other):            # self >= other
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name >= other.name

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
print(pillow >= harry)          # outputs True
#print(new_pillow >= is_pillow)# outputs TypeError
print(harry <= new_pillow)      # outputs True

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

#     def __lt__(self, other):
#         if not isinstance(other, Cat):
#             return NotImplemented

#         return self.name.casefold() < other.name.casefold()

#     def __le__(self, other):
#         if not isinstance(other, Cat):
#             return NotImplemented

#         return self.name.casefold() <= other.name.casefold()

#     def __gt__(self, other):
#         if not isinstance(other, Cat):
#             return NotImplemented

#         return self.name.casefold() > other.name.casefold()

#     def __ge__(self, other):
#         if not isinstance(other, Cat):
#             return NotImplemented

#         return self.name.casefold() >= other.name.casefold()

# bugs = Cat('Bugs')
# bugs2 = Cat('Bugs')
# elmer = Cat('Elmer')

# print(bugs < elmer)                 # True
# print(elmer < bugs)                 # False
# print(bugs < bugs2)                 # False

# print(bugs <= elmer)                # True
# print(elmer <= bugs)                # False
# print(bugs <= bugs2)                # True

# print(bugs > elmer)                 # False
# print(elmer > bugs)                 # True
# print(bugs > bugs2)                 # False

# print(bugs >= elmer)                # False
# print(elmer >= bugs)                # True
# print(bugs >= bugs2)                # True
