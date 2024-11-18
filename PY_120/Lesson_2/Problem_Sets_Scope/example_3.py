'''
Example 3.

Create a Cat class that has a single method named get_name
that returns the name instance variable.
Without initializing name, try to instantiate a Cat object and call get_name.
Print Name not set! when the error occurs.

'''

# Solution

class Dog:
    
    def __init__(self, breed):
        self._breed = breed
    
    def get_breed(self):
        return self._breed

class Cat:

    def get_name(self):
        try:
            return self.name
        except AttributeError:
            return "Name not set!"

husky = Dog('Golden Retriever')
print(husky.get_breed())           # Outputs Golden Retriever
bruno  = Dog('Poodle')
print(bruno.get_breed())           # Outputs Poodle

kitty = Cat()
print(kitty.get_name())

## LS Solution ##
# class Dog:
#     def __init__(self, breed):
#         self._breed = breed

#     def get_breed(self):
#         return self._breed

# class Cat:
#     def get_name(self):
#         try:
#             return self.name
#         except AttributeError:
#             return "Name not set!"

# dog1 = Dog('Golden Retriever')
# dog2 = Dog('Poodle')

# print(dog1.get_breed())  # Golden Retriever
# print(dog2.get_breed())  # Poodle