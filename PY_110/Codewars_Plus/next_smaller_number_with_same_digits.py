'''
Available at https://www.codewars.com/kata/5659c6d896bc135c4c00021e/train/python
Level = 4kyu

Next smaller number with same digit.
Write a function that takes a positive integer and
returns the next smaller positive integer containing the same digits.

For example:
next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017

Return -1, when there is no smaller number that contains the same digits.
Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.

next_smaller(9) == -1
next_smaller(135) == -1
next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros

# Problem
- Input: 
Interger 
- Output:
Integer

- Rules
    Explicit:
    - Function that takes a positive integer and returns the next smaller positive integer containing the same digits.
    - Return -1, when there is no smaller number that contains the same digit.

    Implicit:

# Examples
print(next_smaller(907) == 790)
print(next_smaller(531) == 513)
print(next_smaller(135) == -1)
print(next_smaller(2071) == 2017)
print(next_smaller(414) == 144)
print(next_smaller(123456798) == 123456789)
print(next_smaller(123456789) == -1)
print(next_smaller(1234567908) == 1234567890)

# Data structure
None

# Algorithm
    High level
    1. Count from the current number till 0
    2. Get the first number that has the same number in the input
    3. Get back this number.

    Low level:
        1. Get input.
        2. Create a string of the input
        3. Create a result to hold a string.
        4. Iterate through the input from the current number till zero:
            - Convert the result to a string:
            - Check if all the current string is in the original string and have the same lenght:
                - If yes, set result to the current string:
                - return the int value of result.
        5. If no number matches, return -1

        Helper function (Check if a substring in string)
            - Get the string.
            - Get the length of the string.
            - Check if lenght of substring == string.
                - If false, return False
                - If true, 
                    - Iterate through the substring.
                        - If a character is not present in the main string or its count is not the same in the main string and substring.
                            - Return False.
            - Return True otherwise:

# Code
'''

# Solution
def is_valid_number(main_number, sub_number):
    if len(main_number) != len(sub_number):
        return False

    for num in sub_number:
        if num not in main_number or main_number.count(num) != sub_number.count(num):
            return False

    return True

def next_smaller(number):
    number_str = str(number)
    result = ''

    for nums in range(number - 1,  -1,  -1):
        nums_str = str(nums)

        if is_valid_number(number_str, nums_str):
            result = nums_str
            return int(result)

    return -1

# other solution:

# Code Check
print(next_smaller(907) == 790)
print(next_smaller(531) == 513)
print(next_smaller(135) == -1)
print(next_smaller(2071) == 2017)
print(next_smaller(414) == 144)
print(next_smaller(123456798) == 123456789)
print(next_smaller(1234567908) == 1234567890)

# Note!
# Time take to write PEDAC and test/debug code 24 mins 37 seconds

## LS Answer ##
# Not Available
