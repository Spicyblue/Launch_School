'''
Reverse Number.
Write a function that takes a positive integer as an argument and 
returns that number with its digits reversed.

# Problem
- Input: 
Integer
- Output:
Integer

- Rules
    Explicit:
    Positive integer as an argument and returns that number with its digits reversed.
    if number is ends with zero, removes the zero.

# Examples
print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True

# Data structure
None

# Algorithm
    - High End 
        1. Get input.
        2. Convert input to string and reverse string.
        3. Return the integer of the reversed string.

# Code
'''

# Solution

def reverse_number(number):
    number = str(number)
    rev_number = number[ : : -1]

    return int(rev_number)

# Code Check
print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True

# Note!
# Time take to write PEDAC and test/debug code is 2 mins, 03 seconds.

## LS Answer ##
# def reverse_number(number):
#     return int(str(number)[::-1])