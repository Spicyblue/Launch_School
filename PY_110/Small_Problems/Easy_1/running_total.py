'''
Running Totals.
Write a function that takes a list of numbers 
and returns a list with the same number of elements, 
but with each element's value being the running total 
from the original list.

Example

# Problems
    -Input: 
    list
    - Output:
    list

    Rules
    - Explicit:
    Output must has same len of element as list
    Each element's value being the running total from the original list
    - Implicit:
    Empty list returns empty list
    One element list return one element list


# Example
print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True

# Data Structure
List

# Algorithm
 -High level:
    1. Get Input.
        If empty list, return empty list.
        if list has one element, return list.
        if list has more than one element, go to 2.
    2. Create new list to hold results.
    3. Pop first element from input and add to new list.
    4. Iterate through the element in input.
        - Access last element in new list
        - Add its value to the value of the current element in input.
        - Add the reult to new list.
        - Repeat until last element.
    5 Return the new list.
    
# Code
'''

# Solution
def running_total(list_input):
    # Guard checks are good due to the pop method being called on line 58.
    if len(list_input) == 0:
        return list_input
    
    if len(list_input) == 1:
        return list_input

    result = []
    result.append(list_input.pop(0))

    for element in list_input:
        sum = result[-1] + element
        result.append(sum)

    return result

# code check
print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True

# Note! Time Taken is about 15 mins 31 seconds.
# Time take to write PEDAC and test/debug code is 15 mins, 10 seconds.
## LS answer ##

# def running_total(nums):
#     result_list = []
#     total = 0

#     for num in nums:
#         total += num
#         result_list.append(total)

#     return result_list
