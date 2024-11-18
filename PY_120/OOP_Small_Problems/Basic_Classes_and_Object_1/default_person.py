'''
Default Person.
Create a class named Person.

When you instantiate a Person object, you should pass in one argument that contains the person's name.
If no arguments are given, the Person object should be instantiated with a name of "John Doe".

Copy Code
person1 = Person()
person2 = Person("Pepe Le Pew")

# Comments show expected output
print(person1.name)    # John Doe
print(person2.name)    # Pepe Le Pew

'''

# Solution

class Person:
    def __init__(self, name = 'John Doe'):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            return 'Please enter a valid alphabetical name'

        self._name = name

    def greet(self):
        print(f"Hello! My name is {self.name}!")

person1 = Person()
person2 = Person("Pepe Le Pew")

# Comments show expected output
print(person1.name)    # John Doe
print(person2.name)    # Pepe Le Pew


## LS Solution ##
# class Person:
#     def __init__(self, name="John Doe"):
#         self._name = name

#     @property
#     def name(self):
#         return self._name

# person1 = Person()
# person2 = Person("Pepe Le Pew")

# # Comments show expected output
# print(person1.name)  # John Doe
# print(person2.name)  # Pepe Le Pew
