'''
Example 4.

Create an instance of the Dog class from your answer to Problem 2.
Set its breed directly from outside the class, then print the resulting breed.

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

dog = Dog('Bulldog')
dog._breed = 'Labrador'
print(dog.get_breed())

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

# dog = Dog('Bulldog')
# dog._breed = 'Labrador'
# print(dog.get_breed())
