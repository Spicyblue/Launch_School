'''
List of Digits
Write a function that takes one argument, a positive integer,
and returns a list of the digits in the number.

Examples
print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True

# Problem
- Input: 
Integer
- Output:
list

- Rules
    Explicit:
    Order is  maintained.
    Integer is positive.
  
# Examples
print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True

# Data structure
list

# Algorithm
    - High End 
        1. Get input.
        2. Convert input to string
        3. Create an empty list to store result
        3. Iterate through the string 
            - convert string to interger
            - add integer to list
            - repeat for all elements
        4. Return result

# Code
'''

# Solution
def digit_list(integer):
    return [int(num) for num in str(integer)]

# Solution 2
# def digit_list(integer):

#     str_intger = str(integer)
#     result = []


#     for num in str_intger:
#         num = int(num)
#         result.append(num)

#     return result

# code check
print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True

# Note!
# Time take to write PEDAC and test/debug code is 5 mins, 46 seconds.

## LS Answer ##
# def digit_list(number):
#     return [int(digit) for digit in str(number)]