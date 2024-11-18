'''
Convert a String to a Signed Number.
In the previous exercise, you developed a function that converts simple numeric strings to integers.
In this exercise, you're going to extend that function to work with signed numbers.
Write a function that takes a string of digits and returns the appropriate number as an integer.
The string may have a leading + or - sign;
if the first character is a +, your function should return a positive number;
if it is a -, your function should return a negative number.
If there is no sign, return a positive number.
You may assume the string will always contain a valid number.
You may not use any of the standard conversion functions available in Python, such as int.
You may, however, use the string_to_integer function from the previous exercise.

# Problem
    - Input:
    String
    - Output:
    integer

    Rules
    - Explicit:
    Cannot use any standard conversion function such as int
    Function should calculate the result by using the characters in the string.
    All inputs are valid
    The string may have a leading + or - sign.
    If the first character is a +, your function should return a positive number.
    If it is a -, your function should return a negative number. 

# Examples 
print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True

# Data structure
Not needed..perhaps an dictionary? 

# Algorithm
    - High Level
        1. Get Input
        2. Create a result variable with an inital integer value set to zero 
        3. Iterate through the inputs
            - if a minus or plus sign is present, skip the element
            - Get the integer value by and substact the ord value of the string from ord ('0')
            - multiply the current value of result by 10 and add it to the integer value
        5. At the end of the iteration, If a minus sign exist in string, multiply the result by -1.

        4. Return the result.

# Code
'''

# Solution
def string_to_signed_integer(string):

    result = 0

    for char in string:
        if char in ['-', '+']:
            continue

        digit = ord(char) - ord('0')
        result = (result * 10) + digit
    
    if '-' in string:
        result *= - 1

    return result

# code check
print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True


# Note!
# Time take to write PEDAC and test/debug code is 7 mins, 22 seconds.
# Since it was a refatoring of an already exisitng code.


## LS Answer ##

# def string_to_integer(s):
#     DIGITS = {
#         '0': 0,
#         '1': 1,
#         '2': 2,
#         '3': 3,
#         '4': 4,
#         '5': 5,
#         '6': 6,
#         '7': 7,
#         '8': 8,
#         '9': 9,
#     }

#     value = 0
#     for char in s:
#         value = (10 * value) + DIGITS[char]

#     return value

# def string_to_signed_integer(string):
#     match string[0]:
#         case '-':
#             return -string_to_integer(string[1:])
#         case '+':
#             return string_to_integer(string[1:])
#         case _:
#             return string_to_integer(string)
