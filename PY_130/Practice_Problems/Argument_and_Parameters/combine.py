'''
Combine.
Write a function named combine that takes three positional arguments
and returns a tuple containing all three. 
Call this function with three different values.
'''

# Solution

def combine(name, age, height):
    return (name, age, height)

print(combine('Harry', '20', '174cm'))
print(combine('Barry', '25', '198cm'))
print(combine('Larry', '30', '169cm'))

## LS Solution ##
# def combine(a, b, c):
#     return (a, b, c)

# print(combine('a', 2, None))  # ('a', 2, None)