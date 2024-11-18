'''
What is odd.
Create a function that takes a list of numbers, all of which are the same except one.
Find and return the number in the list that differs from all the rest.
The list will always contain at least 3 numbers,
and there will always be exactly one number that is different.

# Problem
- Input: 
List
- Output:
Integer
- Rules
    Explicit:
    - Find and return the number in the list that differs from all the rest.
    - The list will always contain at least 3 numbers, and there will always be exactly one number that is different

    Implicit:

# Examples
print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)

# Data structure
None

# Algorithm
    High level
    1. Get and return the number than occurs once.

    Low level:
        1. Get input.
        2. Create a result and set it to one.
        3. Iterate through the input:
            - Check if the current count of the element is 1
            - If yes, set result to number.
        4. Return the result

# Code
'''

# Solution
def what_is_different(lst):

    result = 0
    for num in lst:
        if lst.count(num) == 1:
            result =  num

    return result

# Code Check
print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)

# Note!
# Time take to write PEDAC and test/debug code 4 mins 53 seconds

## LS Answer ##
# Not Available