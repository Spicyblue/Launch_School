'''
Remove Consecutive Duplicates.
Given a sequence of integers, filter out instances where the same value occurs successively,
retaining only the initial occurrence.
Return the refined sequence.

# Problem
- Input: 
List
- Output:
List

- Rules
    Explicit:
    Filter out instances where the same value occurs successively, retaining only the initial occurrence.
    Implicit:

# Examples

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True

# Data structure
List

# Algorithm
    - High End:
        1. Get input.
        2. Create a empty list to store result.
        3. Remove the first elment from the input and add to list.
        3. Iterate through the rest of the input.
            - If the current element is not the same as the last element in result,
                - Add current element.
            - Repeat for all element.
        4. Return result.
        
# Code
'''

# Solution
def unique_sequence(lst):

    result = []
    result = [lst[0]] 
     #This is a mutating method so might not be the best idea but 

    for ele in lst:
        if ele != result[-1]:
            result.append(ele)

    return result

# code check
original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True

# Note!
# Time take to write PEDAC and test/debug code is 5 mins, 32 seconds.

## LS Answer ##
# def unique_sequence(numbers):
#     if not numbers:
#         return []

#     unique = [numbers[0]]
#     for value in numbers[1:]:
#         if value != unique[-1]:
#             unique.append(value)

#     return unique
# Solution 2
# def unique_sequence(numbers):
#     return [value
#             for idx, value in enumerate(numbers)
#             if idx == 0 or value != numbers[idx-1]]
