'''
Example 2.

Add a get_breed method to the Dog class from your answer to the previous problem.
The method should return the dog's breed.
Use the method to print the breeds of the two dog objects you created in the previous problem.
You should also mark the breed instance variable for internal use only.

'''

# Solution

class Dog:
    
    def __init__(self, breed):
        self._breed = breed
    
    def get_breed(self):
        return self._breed
    
husky = Dog('Golden Retriever')
print(husky.get_breed())           # Outputs Golden Retriever
bruno  = Dog('Poodle')
print(bruno.get_breed())           # Outputs Poodle

## LS Solution ##
# class Dog:
#     def __init__(self, breed):
#         self._breed = breed

#     def get_breed(self):
#         return self._breed

# dog1 = Dog('Golden Retriever')
# dog2 = Dog('Poodle')

# print(dog1.get_breed())  # Golden Retriever
# print(dog2.get_breed())  # Poodle