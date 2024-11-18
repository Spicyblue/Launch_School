'''
Example 2

Modify the class definition from above to facilitate the
following methods. Note that there is no name= setter method now.

bob = Person('Robert')
print(bob.name)             # Robert
print(bob.first_name)       # Robert
print(repr(bob.last_name))  # ''
bob.last_name = 'Smith'
print(bob.name)             # Robert Smith

'''

# Solution

class Person:
    
    def __init__(self, name, last_name = ""):
        self._first_name = name
        self._last_name = last_name

    @property
    def name(self):
        return self._first_name + ' ' + self._last_name
    
    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

bob = Person('Robert')
print(bob.name)             # Robert
print(bob.first_name)       # Robert
print(repr(bob.last_name))  # ''
bob.last_name = 'Smith'
print(bob.name)             # Robert Smith

## LS Solution ##

# class Person:
#     def __init__(self, name):
#         parts = name.split()
#         self.first_name = parts[0]
#         self.last_name = ''
#         if len(parts) > 1:
#             self.last_name = parts[1]

#     @property
#     def name(self):
#         return f'{self.first_name} {self.last_name}'.strip()

#     @property
#     def first_name(self):
#         return self._first_name

#     @first_name.setter
#     def first_name(self, first_name):
#         self._first_name = first_name

#     @property
#     def last_name(self):
#         return self._last_name

#     @last_name.setter
#     def last_name(self, last_name):
#         self._last_name = last_name

# This class has three properties, two of which have a setter.
# The name property constructs the full name from the first_name and last_name properties.

# There are two items of note here besides the property definitions:

# The __init__ method parses the first and last name from the input name argument.
# Things get mildly tricky if name doesn't contain both a first and last name.
# The name property applies the strip method to the returned name.
# Once again, this code is in play if both names aren't available.