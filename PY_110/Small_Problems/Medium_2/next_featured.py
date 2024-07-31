'''
Next Featured Number Higher than a Given Value.
A featured number (something unique to this exercise) is an odd number that is a multiple of 7,
with all of its digits occurring exactly once each.
For example, 49 is a featured number, but 98 is not (it is not odd),
97 is not (it is not a multiple of 7), and 133 is not (the digit 3 appears twice).

Write a function that takes an integer as an argument and returns the next featured number greater than the integer.
Issue an error message if there is no next featured number.

NOTE: The largest possible featured number is 9876543201

# Problem
- Input: 
Integer
- Output:
Integer or string

- Rules
    Explicit:
    A featured number (something unique to this exercise) is an odd number that is a multiple of 7,
    with all of its digits occurring exactly once each.

    Implicit:
    For example, 49 is a featured number,
    98 is not (it is not odd).
    97 is not (it is not a multiple of 7),

# Examples
print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

# Data structure
None

# Algorithm
    - High End:
        1. Get input.
        2. Iterate from the next number till the next feature:
            - Chekc if the number is featured:
                - If is a featured number
                    - return number

        3- If no number is found, issue an error message

       is_featured: Algorithm
        For the input:
            - check if number is a multiple of 7
            - check if number is odd.
            - check is any number apprears twice
            - return false in any case
        -Return true if all cases pass

# Code
'''

# Solution
def is_featured(number):

    str_number = str(number)

    return number % 7 == 0 and number % 2 == 1 and all(str_number.count(digit) == 1 
                                                       for digit in str_number)

def next_featured(number):

    error = ("There is no possible number that "
         "fulfills those requirements.")

    max_featured_number = 9876543201

    while number <= max_featured_number:
        number += 1
        if is_featured(number):
            return number

    return error

# code check

print(is_featured(49))
print(is_featured(98))
print(is_featured(133))

print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True

# Note!

# Note!
# Time take to write PEDAC and test/debug code is 19 mins, 30 seconds.

# However this solution is not optimized for checking larger numbers compared to ls solution. hence the last code may take longer to load. For now, the focus is understand, then comes optimization.

## LS Answer ##
# def to_odd_multiple_of_7(number):
#     number += 1
#     while number % 2 == 0 or number % 7 != 0:
#         number += 1

#     return number

# def all_unique(number):
#     digits = list(str(number))
#     return len(digits) == len(set(digits))

# def next_featured(number):
#     MAX_FEATURED = 9876543201
#     featured_num = to_odd_multiple_of_7(number)

#     while featured_num <= MAX_FEATURED:
#         if all_unique(featured_num):
#             return featured_num

#         featured_num += 14

#     return "There is no possible number that fulfills those requirements."