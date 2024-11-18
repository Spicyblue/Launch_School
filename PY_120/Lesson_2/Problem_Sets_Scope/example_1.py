'''
Example 1.

Define a Dog class that has a breed instance variable.
Instantiate two objects from this class, one with the breed 'Golden Retriever'
and another with the breed 'Poodle'.
Print the breed of each dog.

'''

# Solution

class Dog:
    
    def __init__(self, breed):
        self.breed = breed

    
husky = Dog('Golden Retriever')
print(husky.breed)           # Outputs Golden Retriever
bruno  = Dog('Poodle')
print(bruno.breed)           # Outputs Poodle

## LS Solution ##
# class Dog:
#     def __init__(self, breed):
#         self.breed = breed

# dog1 = Dog('Golden Retriever')
# dog2 = Dog('Poodle')

# print(dog1.breed)  # Golden Retriever
# print(dog2.breed)  # Poodle
