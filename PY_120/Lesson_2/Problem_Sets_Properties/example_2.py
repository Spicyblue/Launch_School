'''
Example 2.

Update your answer from problem 1 to disallow empty strings.
You should raise a ValueError. 
Be sure to test your code.

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
        if name == '':
            raise ValueError('Name must be atleast one letter long')
        self._name = name

emeka = Person('Emeka')
print(emeka.name)           # Emeka
emeka.name = 'Uche'
print(emeka.name)           # Uche

# emeka.name = ''             # ValueError: Name must be atleast one letter long

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

#         if name == '':
#             raise ValueError('Name must not be empty.')

#         self._name = name

# linda = Person('Linda')
# print(linda.name)                   # Linda

# linda.name = 'Lin'
# print(linda.name)                   # Lin

# linda.name = ['Linda']
# # TypeError: Name must be a string.

# linda.name = ''           # ValueError: Name must not be empty.
