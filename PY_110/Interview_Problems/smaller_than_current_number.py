'''
Smaller than current number.
Create a function that takes a list of numbers as an argument.
For each number, determine how many numbers in the list are smaller than it, and place the answer in a list.
Return the resulting list.

When counting numbers, only count unique values.
That is, if a number occurs multiple times in the list, it should only be counted once.

# Problem
- Input: 
list
- Output:
list

- Rules
    Explicit:
    - For each number, determine how many numbers in the list are smaller than it, and place the answer in a list.
    - When counting numbers, only count unique values.
    - If a number occurs multiple times in the list, it should only be counted once.

    Implicit:

# Examples
print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)

# Data structure
List or List comprehension

# Algorithm
    High Level:
    1. Count every number bigger than the current number.
    2. Save the value
    3. Get back the values.

    Low level:
        1. Get input.
        2. Create a list to store the result.
        3. Ceate a set if the original list for keeping unique values.
        4. Iterate through the input:
            - Set a counter to zero.
            - Iterate through the set 
                - Check if the current element is greater than the set element
                - If yes, increase counter.
            - Add counter to current list.
            - Repeat for the next element.
        5. Return list.     

# Code
'''

# Solution
def smaller_numbers_than_current(lst):
    result = []
    lst_set = set(lst)

    for number in lst:
        count = 0
        for digit in lst_set:
            if number > digit:
                count += 1
        result.append(count)
    
    return result


def refactored_smaller_numbers_than_current(lst):
    lst_set = set(lst)
    return [sum(1 for digit in lst_set if number > digit) for number in lst]

# code check
print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)

print(refactored_smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(refactored_smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(refactored_smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(refactored_smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(refactored_smaller_numbers_than_current([1]) == [0])

# Note!
# Time take to write PEDAC and test/debug code 19 mins 03 seconds

## LS Answer ##
# Not Available
