'''
List Average
Write a function that takes one argument, a list of integers,
and returns the average of all the integers in the list,
rounded down to the integer component of the average.
The list will never be empty, and the numbers will always be positive integers.

# Problem
- Input: 
list
- Output:
integer

- Rules
    Explicit:
    Function that takes one argument.
    Returns the average of all the integers in the list
    Average is rounded down to the integer component of the average.
    The list will never be empty.
    The numbers will always be positive integers.
  
# Examples
print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True

# Data structure
list

# Algorithm
    - High End 
        1. Get input.
        2. Create a result and assign it a value of 0.
        3. Iterate to the list.
            - Add the element to the current value of result.
            - repeat for all elements.
        4. Get the average of result.
        5. Return the int value of result

# Code
'''

# Solution
def average(lst):

    result = 0

    for num in lst:
        result += num

    result  = result // len(lst)

    return result

# code check
print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True

# Note!
# Time take to write PEDAC and test/debug code is 6 mins, 56 seconds.

## LS Answer ##

# def average(numbers):
#     total = sum(numbers)
#     return total // len(numbers)