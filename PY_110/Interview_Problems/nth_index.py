'''
Nth index.
Create a function that takes a list of integers as an argument.
Determine and return the index N for which all numbers with an index less
than N sum to the same value as the numbers with an index greater than N.
If there is no index that would make this happen, return -1.
If you are given a list with multiple answers, return the index with the smallest value.
The sum of the numbers to the left of index 0 is 0.
Likewise, the sum of the numbers to the right of the last element is 0.

Notes:
The list will always contain at least 2 integers.
All values in the list must be positive (> 0).
There may be multiple occurrences of the various numbers in the list.

# Problem
- Input: 
List
- Output:
Integer (Index)

- Rules
    Explicit:
    - The list will always contain at least 2 integers.
    - All values in the list must be positive (> 0).
    - There may be multiple occurrences of the various numbers in the list.

    Implicit:

# Examples
print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)

# Data structure
None

# Algorithm
    High level
    1. Get sum of left side and right side
    2. Find when they are equall
    3. Get the position that makes this equall or -1

    Low level:
        1. Get input.
        2. Iterate through the input:
            - Get the sum of left side (from start to the current element without the nth element)
            - Get the right side (from after the nth element to the end).
            - Check if right side equalls left side:
                - If yes,
                    - return the index

        3. Return -1

# Code
'''

# Solution
def equal_sum_index(lst):
    
    for idx in range(len(lst) -1):
        left_side = lst[ : idx]
        right_side = lst[idx + 1: ]
        sum_left_side = sum(left_side)
        sum_right_side = sum(right_side)

        if sum_left_side == sum_right_side:
            return idx

    return -1
# Code Check
print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# Note!
# Time take to write PEDAC and test/debug code 15 mins 21 seconds

## LS Answer ##
# Not Available