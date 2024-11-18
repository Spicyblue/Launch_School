'''
List Average
Write a function that takes one argument, a list of integers, and 
returns the average of all the integers in the list, 
rounded down to the integer component of the average.
The list will never be empty, and the numbers will always be positive integers.

# Problem
- Input: 
List
- Output:
None

- Rules
    Explicit:
    Returns the average of all the integers in the list, rounded down to the integer component of the average
  
# Examples
print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)    

# Data structure
list

# Algorithm
    - High End 
        1. Get input.
        2. Sum the input
        3. Return the avergae

# Code
'''

# Solution
def average(lst):
    result = sum(lst)
    return result // len(lst)

# code check
print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7) 

# Note!
# Time take to write PEDAC and test/debug code is 6 mins, 56 seconds.

# other Solution
# def average(lst):
#     result = 0

#     for num in lst:
#         result += num

#     result  = result // len(lst)

#     return result

## LS Answer ##

# def average(numbers):
#     total = sum(numbers)
#     return total // len(numbers)