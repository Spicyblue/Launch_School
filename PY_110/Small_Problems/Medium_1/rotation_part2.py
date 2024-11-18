'''
Rotation (Part 2).
Write a function that rotates the last count digits of a number.
To perform the rotation, move the first of the digits that you
want to rotate to the end and shift the remaining digits to the left.

# Problem:
- Input:
Integers
- Output:
Integers

- Rules
    Explicit:
    Rotates the last count digits of a number.
    Move the first of the digits that you want to rotate to the end and shift the remaining digits to the left.

# Examples:

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True

# Data structure
None

# Algorithm
    - High End 
        1. Get input.
        2. If the count is 1, return the integer input.
        3. Convert integer to string.
        4. Split string from start to the - count .
            - Concantenate rest of the string, ignoring - count value.
            - Concantenate finally with -count
        5. Convert string to integer.
        6. Return result

# Code
'''

# # Solution
def rotate_rightmost_digits(interger, count):

    if count == 1:
        return interger
    
    string_integer = str(interger)

    first = - count

    middle = first + 1

    result = string_integer[: first] + string_integer[middle:] + string_integer[first]

    return int(result)

# #code check
# print(rotate_rightmost_digits(735291, 2) == 735219)  # True
# print(rotate_rightmost_digits(735291, 3) == 735912)  # True
# print(rotate_rightmost_digits(735291, 1) == 735291)  # True
# print(rotate_rightmost_digits(735291, 4) == 732915)  # True
# print(rotate_rightmost_digits(735291, 5) == 752913)  # True
# print(rotate_rightmost_digits(735291, 6) == 352917)  # True
# print(rotate_rightmost_digits(1200, 3) == 1002)      # True


# Time take to write PEDAC and test/debug code is 16 mins, 45 seconds.

## LS Answer ##
# def rotate_rightmost_digits(number, count):
#     number_str = str(number)
#     first_part = number_str[:-count]
#     second_part = number_str[-count:]
#     result_str = first_part + rotate_string(second_part)

#     return int(result_str)

# def rotate_string(string):
#     return string[1:] + string[0]

