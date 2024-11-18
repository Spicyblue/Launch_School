'''
Multiples of 7 and 11.
Create a function that takes a single integer argument and returns the sum of all the multiples of 7 or 11
that are less than the argument. If a number is a multiple of both 7 and 11, count it just once.
For example, the multiples of 7 and 11 that are below 25 are 7, 11, 14, 21, and 22. 
The sum of these multiples is 75.
If the argument is negative, return 0.

# Problem
- Input: 
Integer
- Output:
Integer

- Rules
    Explicit:
    - If the argument is negative, return 0.
    - Returns the sum of all the multiples of 7 or 11 that are less than the argument.

    Implicit:

# Examples
print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)

# Data structure
list

# Algorithm
    High level
    1. Get all the required multiples.
    2. Sum them.

    Low level:
        1. Get input.
        2. Create a result to add the sum.
        3. Generate and iterate through the sequence on number
            - Check if current number is a multiple of seven or eleven:
                - If yes, increase result by the the number.
        3. Return  the sum of the result.

# Code
'''

# Solution
def is_multiple_of_seven_and_eleven(num):
    return num % 7 == 0 or num % 11 == 0

def seven_eleven(integer):
    result = 0

    for num in range(integer):
        if is_multiple_of_seven_and_eleven(num):
            result += num
    
    return result

# using list comprehension
# def seven_eleven(integer):
#     return sum([num for num in range(integer) if is_multiple_of_seven_and_eleven(num)])

# Code Check
print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)

# Note!
# Time take to write PEDAC and test/debug code 7 mins 52 seconds

## LS Answer ##
# Not Available