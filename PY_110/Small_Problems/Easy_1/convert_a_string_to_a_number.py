'''
Convert a String to a Number.
Write a function that takes a string of digits and 
returns the appropriate number as an integer.
You may not use any of the standard conversion functions available in Python,
such as int. Your function should calculate the result by 
using the characters in the string.
For now, do not worry about leading + or - signs, 
nor should you worry about invalid characters;
assume all characters are numeric.

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
    no leading + or minus sign

# Examples 
print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True

# Data structure
Not needed..perhaps an dictionary? 

# Algorithm
    - High Level
        1. Get Input.
        2. Create a result variable with an inital integer value set to zero.
        3. Iterate through the inputs.
            - Get the integer value by and substact the ord value of the string from ord ('0').
            - multiply the current value of result by 10 and add it to the integer value.
        4. Return the result.

# Code
'''

# Solution
def string_to_integer(string):

    result = 0

    for char in string:
        
        digit = ord(char) - ord('0')

        result = (result * 10) + digit

    return result

# code check
print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True
print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True

# Note!
# Time take to write PEDAC and test/debug code is 19 mins, 12 seconds.
# Tricky was how to implement the logic for add the numbers together.


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

'''
Further Exploration
Write a hexadecimal_to_integer function that converts a string
representing a hexadecimal number to its integer value.
Hexadecimal numbers use base 16 instead of 10,
and the characters A, B, C, D, E and F
(and the lowercase equivalents) correspond to
decimal values of 10-15.

# Problem
    - Input:
    String
    - Output:
    integer

    Rules
    - Explicit:
    Cannot use any startd conversion function such as int
    Function should calculate the result by using the characters in the string.
    All inputs are valid
    Hexadecimal numbers use base 16 instead of 10, 
    A, B, C, D, E and F (and the lowercase equivalents
    correspond to decimal values of 10-15.

# Examples 
print(hexadecimal_to_integer('4D9f') == 19871)  # True

# Data structure
not needed

#Algorithm
    - High Level
        1. Get Input.
        2. Convert string to lowecase using casefold.
        2. Create a result variable with an inital integer value set to zero.
        3. Iterate through the inputs.
            - if value is between 0 and 9.
                - Get the integer value by and substact the ord value of the string from ord ('0').
                - multiply the current value of result by 10 and add it to the integer value.
            - If value is between a and f.
                - Get the integer value by and substact the ord value of the string from ord ('a').
                - add 10 to the integer value to account for 10 - 15
                - multiply the current value of result by 10 and add it to the integer value.

        4. Return the result.

# Code
'''

# Solution
def hexadecimal_to_integer(hex_str):

    hex_str = hex_str.casefold() 

    result = 0
    for char in hex_str:
        if '0' <= char <= '9':
            digit = ord(char) - ord('0')

        if 'a' <= char <= 'f':
            digit = (ord(char) - ord('a')) + 10 #( adding 10 to account for 10 - 15)

        result = (result * 16) + digit

    return result

print(hexadecimal_to_integer('4D9f') == 19871)  # True

# Note!
# Time take to write PEDAC and test/debug code is 8 mins, 33 seconds.
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

# An intresting code
# def string_to_integer(input):
#     value = {
#         '0' : 0,
#         '1' : 1,
#         '2' : 2,
#         '3' : 3,
#         '4' : 4,
#         '5' : 5,
#         '6' : 6,
#         '7' : 7,
#         '8' : 8,
#         '9' : 9,
#     }

#     result = 0
#     multiplier = 1
#     for str_num in input[::-1]:
#         result += (value[str_num] * multiplier)
#         multiplier *= 10

#     return result
