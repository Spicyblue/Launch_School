'''
Identify Yourself (Part 2).
Update the following code so that it prints I'm Sophie! when it invokes print(kitty).

class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

# Comments show expected output
kitty = Cat('Sophie')
print(kitty)        # I'm Sophie!

'''

# Solution

class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    def __str__(self):
        return f"I am {self._name}"

# Comments show expected output
kitty = Cat('Sophie')
print(kitty)        # I'm Sophie!


## LS Solution ##
# class Cat:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name

#     def __str__(self):
#         return f"I'm {self.name}!"

# # Comments show expected output
# kitty = Cat('Sophie')
# print(kitty)        # I'm Sophie!