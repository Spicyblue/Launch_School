'''
Example 6.

Consider the following code:

class Cat:
    def __init__(self, type):
        self.type = type

print(Cat('hairball'))
# <__main__.Cat object at 0x10695eb10>
The output here isn't very useful. It only tells us that we've got an instance of the Cat class,
and it's memory address. It would be better if the output were more meaningful.
For instance, maybe it can print I am a hairball instead. Update the code to produce that result.

'''

# Solution

# class Cat:
#     def __init__(self, type):
#         self.type = type

# cat = Cat('hairball')
# print(cat.type)             # hairball

## LS Solution ##
# class Cat:
#     def __init__(self, type):
#         self.type = type

#     def __str__(self):
#         return f'I am a {self.type}'

# print(Cat('hairball'))

# To do this, we first need to remember that print converts its positional
# arguments to strings before printing them. It does that with the built-in str function. 
# Fortunately, we can customize str by defining a __str__ instance method in the Cat class: