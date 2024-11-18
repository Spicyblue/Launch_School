'''
Sum of Digits.
Write a function that takes one argument, a positive integer, and returns the sum of its digits.

# Problem
- Input: 
Integer
- Output:
Integer

- Rules
    Explicit:
    Takes one argument, a positive integer, and returns the sum of its digits.
    Implicit:

# Examples

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True

# Data structure
None

# Algorithm
    - High End:
        1. Get input.
        2. Convert input to string
        3. Create a result to store the total.
        4. Iterate through the string.
            - Increase total by the integer value of the string
            - Repeat for all element.
        5. Return result.
        
# Code
'''

# Solution
def sum_digits(integer):

    result = 0

    for num in str(integer):
        result += int(num)

    return result

# Solution 2
def sum_digits2(integer):
    return sum([int(num) for num in str(integer)])

# code check
print(sum_digits2(23) == 5)              # True
print(sum_digits2(496) == 19)            # True
print(sum_digits2(123456789) == 45)      # True

# Note!
# Time take to write PEDAC and test/debug code is 2 mins, 21 seconds.

## LS Answer ##
# def sum_digits(number):
#     digits = [int(digit) for digit in str(number)]
#     return sum(digits)

