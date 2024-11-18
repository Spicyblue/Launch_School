'''
Counting Up.
Write a function that takes an integer argument and 
returns a list containing all integers between 1 and the argument (inclusive),
in ascending order.

You may assume that the argument will always be a positive integer.

# Problem
- Input: 
Integer
- Output:
list

- Rules
    Explicit:
    Positive integer as an argument.
    Returns list containing all integers between 1 and the argument (inclusive).
    
# Examples
print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True

# Data structure
None

# Algorithm
    - High End 
        1. Get input.
        2. Create empty list to hold result.
        3. iterate through the range of the input plus 1.
            - append the number to the list.
        4. Return list.
        5. Do 1 - 4 in a list comprehension and return it.

# Code
'''

# Solution

def sequence(number):
    return [num for num in range(1 , number + 1)]
    
# Code Check
print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True

# Note!
# Time take to write PEDAC and test/debug code is 1 mins, 43 seconds.

## LS Answer ##
# def sequence(limit):
#     return list(range(1, limit + 1))