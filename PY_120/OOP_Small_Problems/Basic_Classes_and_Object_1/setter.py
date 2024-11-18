'''
Setter.
Using the code snippet provided below, add a setter method named name.
Then, rename kitty to 'Luna' and invoke greet again.

class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def greet(self):
        print(f"Hello! My name is {self.name}!")

kitty = Cat('Sophie')
kitty.greet()

Expected output
Hello! My name is Sophie!
Hello! My name is Luna!

'''

# Solution

class Cat:
    def __init__(self, name):
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

kitty = Cat('Sophie')
kitty.greet()       # Outputs Hello! My name is Sophie!

kitty.name = 'Luna'
kitty.greet()       # Outputs Hello! My name is Luna!

## LS Solution ##
# class Cat:
#     def __init__(self, name):
#         self.name = name

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, new_name):
#         self._name = new_name

#     def greet(self):
#         print(f"Hello! My name is {self.name}!")

# kitty = Cat('Sophie')
# kitty.greet()
# kitty.name = 'Luna'
# kitty.greet()
