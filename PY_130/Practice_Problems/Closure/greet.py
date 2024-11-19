'''
Greet.
What will this code print? Try to answer without running the code:

'''
from functools import partial

def greet(name, greeting):
    return f"{greeting}, {name}!"

say_hello_to = partial(greet, greeting="Hello")
print(say_hello_to(name="Alice"))  # What will this print?

# Solution
# The code will print 
# Hello Alice!. 

## LS Answer ##
# The code will print:
# It prints "Hello, Alice!" since the partial function from the functools module
# creates a new version of the greet function with the greeting argument pre-filled as "Hello".
# Thus, when say_hello_to is called with "Alice" as the name,
# it completes the call by using the pre-set greeting.
