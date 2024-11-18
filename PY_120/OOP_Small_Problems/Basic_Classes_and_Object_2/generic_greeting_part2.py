'''
Generic Greeting (Part 2).

Using the following code, add two methods: generic_greeting and personal_greeting.
The first method should be a class method and print a greeting that's generic to the class.
The second method should be an instance method and print a greeting that's custom to the object.

class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

kitty = Cat('Sophie')

# Comments show expected output
Cat.generic_greeting()        # Hello! I'm a cat!
kitty.personal_greeting()     # Hello! My name is Sophie!

'''

# Solution

class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @classmethod
    def generic_greeting(cls):
        print(f"Hello! I'm a cat!")

    def personal_greeting(self):
        print(f"Hello! My name is {self._name}!")

kitty = Cat('Sophie')

# Comments show expected output
Cat.generic_greeting()        # Hello! I'm a cat!
kitty.personal_greeting()     # Hello! My name is Sophie!


## LS Solution ##
# class Cat:
#     def __init__(self, name):
#         self._name = name

#     @classmethod
#     def generic_greeting(cls):
#         print("Hello! I'm a cat!")

#     @property
#     def name(self):
#         return self._name

#     def personal_greeting(self):
#         print(f"Hello! My name is {self.name}!")

# kitty = Cat('Sophie')

# # Comments show expected output
# Cat.generic_greeting()        # Hello! I'm a cat!
# kitty.personal_greeting()     # Hello! My name is Sophie!
