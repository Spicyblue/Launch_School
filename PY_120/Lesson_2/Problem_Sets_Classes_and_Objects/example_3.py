'''
Example 3

Add a new setter property for name that takes either a first name or full name,
and knows how to set the first_name and last_name properties appropriately. 
Use the following code to test your code:

'''

# Solution

class Person:
    
    def __init__(self, name, last_name = ""):
        self._first_name = name
        self._last_name = last_name

    @property
    def name(self):
        return self._first_name + ' ' + self._last_name
    
    @name.setter
    def name(self, name):
        self._name = name.split()
        if len(self._name) == 1:
            self._first_name = self._name[0]
            self._last_name = ''

        elif len(self._name) > 1:
            self._first_name = self._name[0]
            self._last_name = " ".join([names for names in self._name[1:]])

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

bob.name = 'Prince'
print(bob.first_name)       # Prince
print(repr(bob.last_name))  # ''

bob.name = 'John Adams'
print(bob.first_name)       # John
print(bob.last_name)        # Adams

print(bob.name)             # John Adams

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

#     @name.setter
#     def name(self, name):
#         parts = name.split()
#         self.first_name = parts[0]
#         self.last_name = ''
#         if len(parts) > 1:
#             self.last_name = parts[1]

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