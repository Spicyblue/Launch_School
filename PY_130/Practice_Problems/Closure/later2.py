'''
Later 2.
Write a function named later2 that takes two arguments:
a function, func, and an argument for that function, first_arg.
The return value should be a new function that takes an argument, second_arg.
The new function should call the func with the arguments provided by first_arg and second_arg.
Here's an example of how it might be used:

def notify(message, when):
    print(f"{message} in {when} minutes!")

shutdown_warning = later2(notify, "The system is shutting down")
shutdown_warning(30) # The system is shutting down in 30 minutes!
'''

# Solution
def later2(func, first_arg):

    def call_later2(second_arg):
        return func(first_arg, second_arg)

    return call_later2

def notify(message, when):
    print(f"{message} in {when} minutes!")

shutdown_warning = later2(notify, "The system is shutting down")
shutdown_warning(30) # The system is shutting down in 30 minutes!

## LS Answer ##
# def later2(func, first_arg):
#     def inner(second_arg):
#         return func(first_arg, second_arg)

#     return inner

# In the example code, we create a new function called shutdown_warning that issues the shutdown warning specified by the argument to later2.
# The new function takes an argument that it passes to the original input function as its second argument.