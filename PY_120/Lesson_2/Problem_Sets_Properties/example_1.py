'''
Example 1.

Create a Person class with a "private" attribute _name.
Use properties to create a getter and setter for the _name attribute.
The _name attribute must be a string. Be sure to test your code.

'''

# Solution

class Person:
    
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError ('Input must be a valid name')
        self._name = name

emeka = Person('Emeka')
print(emeka.name)           # Emeka
emeka.name = 'Uche'
print(emeka.name)           # Uche

## LS Solution ##
# class Person:
#     def __init__(self, name):
#         self.name = name

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, name):
#         if not isinstance(name, str):
#             raise TypeError('Name must be a string.')

#         self._name = name

# linda = Person('Linda')
# print(linda.name)                   # Linda

# linda.name = 'Lin'
# print(linda.name)                   # Lin

# linda.name = ['Linda']
# # TypeError: Name must be a string.