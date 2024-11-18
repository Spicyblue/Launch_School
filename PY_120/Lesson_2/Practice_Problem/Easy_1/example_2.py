'''
Example 2.

Suppose you have an AngryCat class that looks like this:

class AngryCat:
    def hiss(self):
        print('Hisssss!!!')

How would you create a new instance of this class?

'''

# Solution

class AngryCat:
    def hiss(self):
        print('Hisssss!!!')

kitty = AngryCat()
kitty.hiss()

## LS Solution ##
# To create an object from a class, you just call the constructor function,
# which has the same name as the class

AngryCat()

# You can create a new instance of any class by calling that class's constructor.
# The constructor returns a new object of the class that has the same name.
