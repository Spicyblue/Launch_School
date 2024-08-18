'''
Exercise 2
Given an instance of a Foo object, show two ways to print I am a Foo object
without hardcoding the word Foo.

'''

# Solution

class Foo:

    def __init__(self):
        print(f'This is {self.__class__.__name__}')
        print(f'This is {type(self).__name__}')

Foo()

## LS Answer ##
# class Foo:
#     pass

# foo = Foo()
# print(f'I am a {type(foo).__name__} object')
# print(f'I am a {foo.__class__.__name__} object')