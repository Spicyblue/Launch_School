'''
Greatest_product.
Create a function that takes a string argument that consists entirely of numeric digits
and computes the greatest product of four consecutive digits in the string.
The argument will always have more than 4 digits.

# Problem
- Input: 
String
- Output:
Integer

- Rules
    Explicit:
    - Computes the greatest product of four consecutive digits in the string.
    - The argument will always have more than 4 digits.

    Implicit:

# Examples
print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6

# Data structure
None

# Algorithm
    High level
    1. Get all possible four consecutive numbers.
    2. Get the High product.

    Low level:
        1. Get input.
        2. Create a result to store the max product.
        3. Interate through the string:
            - Get the four consecutive number.
            - Set a product to 1.
                - integer trought the consecutive number.
                    - Mutiply the current value of product by the integer value of the current number.
                    - check if product is greater than max product.
                    - If yes.
                        - Set max product to product.
        4. Return the max product.

# Code
'''

# Solution
def greatest_product(string):
    max_product = 0
    end = len(string) - 3

    for idx in range(end):
        four_consecutive = string[idx : idx + 4]
        product  = 1

        for num in four_consecutive:
            product *= int(num)
            if product > max_product:
                max_product =  product

    return max_product

# Using list comprehension
# def return_string_product(string):
#     nums = [int(char) for char in string]
#     product = 1
#     for num in nums:
#         product *= num
#     return product

# def greatest_product(string):
#     substrings = [string[start_idx: start_idx + 4]
#                   for start_idx in range(len(string) - 3)]
#     products = [return_string_product(substring)
#                 for substring in substrings]
#     return max(products)
# Code Check
print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6

# Note!
# Time take to write PEDAC and test/debug code 11 mins 31 seconds

## LS Answer ##
# Not Available