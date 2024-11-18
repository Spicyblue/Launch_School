'''
Odd fellow.
Create a function that takes an list of integers as an argument and returns the integer that appears an odd number of times.
There will always be exactly one such integer in the input list.

# Problem
- Input: 
List
- Output:
Integer

- Rules
    Explicit:
    - There will always be exactly one such integer in the input list.
    - Returns the integer that appears an odd number of times

    Implicit:

# Examples
print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)

# Data structure
list or none

# Algorithm
    High level
    1. Get and return the number than occurs odd number of time:

    Low level:
        1. Get input.
        2. Create an empyt list to store result.
        3. Iterate through the input:
            - Check if the count of the current element is is odd:
            - If yes, add number to list
            - Repeat for all number.
        4. Return the number in the list.

# Code
'''

# Solution
# def odd_fellow(lst):
#     result = [num for num in lst if lst.count(num) % 2 == 1]
#     return result[0]

# Solution2
def odd_fellow(lst):

    result = 0
    for num in lst:
        if lst.count(num) % 2 == 1:
            result =  num

    return result

# Code Check
print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)

# Note!
# Time take to write PEDAC and test/debug code 5 mins 39 seconds

## LS Answer ##
# Not Available
