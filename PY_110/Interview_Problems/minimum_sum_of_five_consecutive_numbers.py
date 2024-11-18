'''
Minimum sum of 5 consecutive numbers.
Create a function that takes a list of integers as an argument.
The function should return the minimum sum of 5 consecutive numbers in the list.
If the list contains fewer than 5 elements, the function should return None.

# Problem
- Input: 
list
- Output:
Integer or None

- Rules
    Explicit:
    - The function should return the minimum sum of 5 consecutive numbers in the list.
    - If the list contains fewer than 5 elements, the function should return None.
    Implicit:

# Examples
print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)

# Data structure
List

# Algorithm
    High Level:
    1. Make list of every 5 consecutive numbers.
    2. Find their sum.
    3. Get back the lowest possible sum.

    Low level:
        1. Get input.
        2. Check if the list has more than 5 element.
        3. Make a copy of the originaly.
        3. Creat a list that stores the result.
        4. Iterate through the input:
            - Get the sum of the first 5 element in the copied list.
            - Append to result.
            - Remove the first element in the copied list.
            - Repeat until the list has less than 5 elements.
        5. Return the min value of the list.   

# Code
'''

# Solution
def is_valid(lst):
    return len(lst) >= 5

def minimum_sum(lst):

    if not is_valid(lst):
        return None

    copied_lst = list(lst)

    result = []

    while is_valid(copied_lst):
        total = sum(copied_lst[ : 5])
        result.append(total)
        copied_lst.pop(0)

    return min(result)

# code check
print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)

# Note!
# Time take to write PEDAC and test/debug code 12 mins 03 seconds

# other solutions
# def min_sum_of_5_consecutive(nums):
#     if len(nums) < 5:
#         return None

#     # Initial sum of the first 5 elements
#     min_sum = sum(nums[:5])
#     current_sum = min_sum

#     # Slide the window over the list
#     for i in range(5, len(nums)):
#         current_sum = current_sum - nums[i - 5] + nums[i]
#         if current_sum < min_sum:
#             min_sum = current_sum

#     return min_sum

# print(min_sum_of_5_consecutive([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)

## LS Answer ##
# Not Available
