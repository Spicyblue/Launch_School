'''
Convert a Number to a String.
In the previous two exercises, you developed functions 
that convert simple numeric strings to signed integers. 
In this exercise and the next, you're going to reverse those functions.
Write a function that converts a non-negative integer value (e.g., 0, 1, 2, 3, and so on)
to the string representation of that integer.
You may not use any of the standard conversion functions available in Python such as str.
Your function should do this the old-fashioned way
and construct the string by analyzing and manipulating the number.

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


# Examples:

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True

# Data structure
Dictionary 

# Algorithm
    - High End 
        1. Get input.
        2. Create variable for an empty list.
        3. Create a variable for an empty string.
        4. Convert integer to list and add to empty list.
        5. Iterate through list with integer:
            - for each element within the list, check if it is a dictionary key and get its string value.
            - Increment the value of string.
            - Repeat for all element till the last element in input.
        6. Return result

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

#code check
print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True

# Note!
# Time take to write PEDAC and test/debug code is 28 mins, 43 seconds.

## LS Answer ##

# DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# def integer_to_string(number):
#     result = ''

#     while number > 0:
#         number, remainder = divmod(number, 10)
#         result = DIGITS[remainder] + result

#     return result or '0'
