'''
Multiplicative Average
Write a function that takes a list of positive integers as input,
multiplies all of the integers together, divides the result by the number of entries in the list,
and returns the result as a string with the value rounded to three decimal places.

# Problem
- Input: 
List
- Output:
String

- Rules
    Explicit:
    Positive integers as input.
    multiplies all of the elements together.
    Divides the result by the number of entries in the list.
    Returns the result as a string with the value rounded to three decimal places.

# Examples
# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")


# Data structure
list

# Algorithm
    - High End 
        1. Get input.
        2. Create a result with an inital value of 1
        3. Iterate through the list 
            - multiply each element with the current value of result
        4. Divide result by the number of items in the input
        3. Return results with the right format method

# Code
'''

# Solution
def multiplicative_average(lst):

    result = 1

    for ele in lst:
        result *= ele

    result  = result / len(lst)

    return f"{result:.3f}"
            
# code check
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")

# Note!
# Time take to write PEDAC and test/debug code is 8 mins, 04 seconds.

## LS Answer ##
# def round_to_three_digits(number):
#     rounded_number_as_str = str(round(number, 3))
#     decimal_position = rounded_number_as_str.find('.')

#     while len(rounded_number_as_str) - decimal_position < 4:
#         rounded_number_as_str += '0'

#     return rounded_number_as_str

# def multiplicative_average(numbers):
#     product = 1

#     for num in numbers:
#         product *= num

#     return round_to_three_digits(product / len(numbers))
