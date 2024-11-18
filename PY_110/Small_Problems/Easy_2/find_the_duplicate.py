'''
Find the Duplicate
Given an unordered list and the information that exactly one value in the list occurs twice
(every other value occurs exactly once),determine which value occurs twice.
Write a function that finds and returns the duplicate value.
You may assume that the input list will always have exactly one duplicate value.

# Problem
- Input: 
List
- Output:
Integer

- Rules
    Explicit:
    Exactly one value in the list occurs twice (every other value occurs exactly once)

# Examples
# All of these examples should print True
print(find_dup([1, 5, 3, 1]) == 1) # True
print(find_dup([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True

# Data structure
list comprehension, can also use set comprehension

# Algorithm
    - High End 
        1. Get input.
        2. Check if any value in input appears more than once.
        3. Return value

# Code
'''

# Solution
def find_dup(lst):

    dup_value = [num for num in lst if lst.count(num) == 2]

    return dup_value[0]

# code check
print(find_dup([1, 5, 3, 1]) == 1) # True
print(find_dup([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True
# Note!
# Time take to write PEDAC and test/debug code is 5 mins, 53 seconds.

## LS Answer ##
# def find_dup(lst):
#     seen = set()

#     for element in lst:
#         if element in seen:
#             return element

#         seen.add(element)
