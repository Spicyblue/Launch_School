'''
Convert a Signed Number to a String.
In the previous exercise, you developed a function that converts non-negative numbers to strings.
In this exercise, you're going to extend that function by adding the
ability to represent negative numbers as well.
Write a function that takes an integer and converts it to a string representation.
You may not use any of the standard conversion functions available in Python, such as str.
You may, however, use integer_to_string from the previous exercise.

# Problem:
- Input:
Integer of digits.
- Output:
String of digits.

- Rules
    Explicit:
    You may not use any of the standard conversion functions available in Python, such as str
    Your function should calculate the result by using the characters in the input.
    construct the string by analyzing and manipulating the number
    Implicit:
    If integer is positive, add '+' to integer.
    If integer is negative, add '-' to integer.
    If integer is zero, do not add any sign.

# Examples:
print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True

# Data structure
Dictionary 

# Algorithm
    - High End 
        1. Get input.
        2. If number is 0, return '0'
        3. Pass the absolute value of input as an argument to the integer_to_string function
        4. If number is greater than zero:
            - add '+' sign to return value of the function call
            - return number
        5. If number is less than zero:
            - add '-' sign to return value of the function call
            - return number

# Code
'''

# Solution
def integer_to_string(number):

    num_lst = []
    result = ''

    while number >= 0:
        number, remainder = divmod(number, 10)
        num_lst.insert(0, remainder)
        if number == 0:
            break

    dict_string = {
        0 : '0',
        1 : '1',
        2 : '2',
        3 : '3',
        4 : '4',
        5 : '5',
        6 : '6',
        7 : '7',
        8 : '8',
        9 : '9',
    }

    for num in num_lst:
        str_num = dict_string[num]
        result += str_num
        
    return result    

def signed_integer_to_string(number):

    if number == 0:
        return '0'
    
    result = integer_to_string(abs(number))

    if number > 0:
        return '+' + result
    
    if number < 0:
        return '-' + result

# code check
print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True

# Note!
# Time take to write PEDAC and test/debug code is 12 mins, 59 seconds.

## LS Answer ##

# DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# def integer_to_string(number):
#     result = ''

#     while number > 0:
#         number, remainder = divmod(number, 10)
#         result = DIGITS[remainder] + result

#     return result or '0'

# def signed_integer_to_string(number):
#     if number < 0:
#         return f"-{integer_to_string(-number)}"
#     elif number > 0:
#         return f"+{integer_to_string(number)}"
#     else:
#         return "0"
