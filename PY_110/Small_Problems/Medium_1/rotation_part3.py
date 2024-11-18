'''
Rotation (Part 3).
Take the number 735291 and rotate it by one digit to the left, getting 352917.
Next, keep the first digit fixed in place and rotate the remaining digits to get 329175.
Keep the first two digits fixed in place and rotate again to get 321759.
Keep the first three digits fixed in place and rotate again to get 321597.
Finally, keep the first four digits fixed in place and rotate the final two digits to get 321579.
The resulting number is called the maximum rotation of the original number.

Write a function that takes an integer as an argument
and returns the maximum rotation of that integer.
You can (and probably should) use the rotate_rightmost_digits function from the previous exercise.

# Problem:
- Input:
Integers
- Output:
Integers

- Rules
    Explicit:
    Take the number, keep one, rotate, rest and repeat for all numbers.
    After the number you keep, always move the digits that you want to
    rotate to the end and shift the remaining digits to the left.

# Examples:

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True

# Data structure
None

# Algorithm
    - High End 
        1. Get input.
        2. If the count is 1, return the integer input.
        3. Create a max counter for storing the max_value after rotation.
        4. Convert integer to string.
        5. Split string from start to the - count.
            - Concantenate rest of the string, ignoring - count value.
            - Concantenate finally with -count.
            - Convert to integer.
            - Return result.
            - Repeat same process on the return result.
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

def max_rotation(integer):

    for idx in range(len(str(integer)), 1, -1):
        integer = rotate_rightmost_digits(integer, idx)

    return integer

# def max_rotation(n):
#     num_digits = len(str(n))

#     for i in range(num_digits):
#         n = rotate_rightmost_digits(n, num_digits - i)

#     return n

# #code check
print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# # Note that the final sequence here is `015`. The leading
# # zero gets dropped, though, since we're working with
# # an integer.
print(max_rotation(105) == 15)                 # True

# Time take to write PEDAC and test/debug code is 14 mins, 45 seconds.

# Getting the right argument for the range function and the rotate_rightmost_digits function was tricky.


## LS Answer ##
# def rotate_rightmost_digits(number, count):
#     number_str = str(number)
#     first_part = number_str[:-count]
#     second_part = number_str[-count:]
#     result_str = first_part + rotate_string(second_part)

#     return int(result_str)

# def rotate_string(string):
#     return string[1:] + string[0]

# def max_rotation(number):
#     number_digits = len(str(number))
#     for count in range(number_digits, 1, -1):
#         number = rotate_rightmost_digits(number, count)

#     return number
