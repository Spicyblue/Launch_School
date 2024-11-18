'''
Halvsies
Write a function that takes a list as an argument and returns a list that contains two elements,
both of which are lists.
Put the first half of the original list elements in the first element
of the return value and put the second half in the second element.
If the original list contains an odd number of elements,
place the middle element in the first half list.

# Problem
- Input: 
List
- Output:
List

- Rules
    Explicit:
    Put the first half of the original list elements in the first element of the return.
    Put the second half in the second element.
    If the original list contains an odd number of elements, place the middle element in the first half list.
    Implicit:
    If list is empty, return two empty list.
    If list has one element, first half goes into the first element, second half is empty list.

# Examples
# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])


# Data structure
List and Nested list

# Algorithm
    - High End 
        1. Get input.
        2. Create an empty list to hold result.
        3. Check if length of the input is even or odd
        5. If even
            - split list into two equall half
        6. If odd
            - split list into two unequall equall half with the first half containing the middle element

        7. Add first half and second half to result and return it.

# Code
'''

# Solution
def halvsies(lst):

    result = []

    middle_index = len(lst) // 2

    if len(lst) % 2 == 0:
        left_side = lst[ : middle_index]
        right_side = lst[middle_index : ]
    
    else:
        left_side =  lst[ : middle_index + 1]
        right_side = lst[middle_index + 1 : ]
    
    result.append(left_side)
    result.append(right_side)

    return result

# code check
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])

# Note!
# Time take to write PEDAC and test/debug code is 20 mins, 16 seconds.

## LS Answer ##
# def halvsies(lst):
#     half = (len(lst) + 1) // 2
#     first_half = lst[:half]
#     second_half = lst[half:]
#     return [first_half, second_half]
