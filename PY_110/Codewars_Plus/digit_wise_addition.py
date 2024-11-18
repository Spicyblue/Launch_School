'''
Available at https://www.codewars.com/kata/663e0eccecb2d0a12da51f84
Level = 5kyu

Digitwise Addition.
Digitwise addition is a special kind of addition where instead of adding 1 normally to the number, it adds 1 to every digit of that number. If the digit is a 9, we replace it with a 10 without carrying over to the next digit.

Examples
123 -> 234
910 -> 1021
789 -> 8910
Task
Program a function that takes two numbers, n and k, and outputs the number of digits in n after applying Digitwise addition k times. Since the answer can be very large, return the answer modulo 1_000_000_007.

Your solution is expected to be O(klogn).

Examples
(9812, 2) -> 6
# Explanation:
# 9812 -> 10923 -> 211034 -> 6 digits

(9899, 3) -> 8
# Explanation:
# 9899 -> 1091010 -> 21102121 -> 32213232 -> 8 digits


# Problem
- Input: 
Interger 
- Output:
Integer

- Rules
    Explicit:
    - Add 1 to the current digit, if its 9, return 10
    - Program a function that takes two numbers, n and k, and outputs the number of digits in n after applying Digitwise addition k times.
    - Your solution is expected to be O(klogn).

    Implicit:
    - 

# Examples
print(digit_wise_addition(9812, 2), 6)
print(digit_wise_addition(9899, 3), 8)

# Data structure


# Algorithm
    High level
    1. Get the digitwise addition for the input.
    2. Repeat based on the number of times given.
    3. Get the final output.

    Low level:
        1. Get input.
        2. Create a result to hold string result.
        3. Convert input to string.
        4. Create a dictionary that works like the digit_wise_addition.
        5. Iterate through the converted string:
            - Get the result of the digit_wise_addition for each number.
            - Increament result by this.
            - repeat for all elmeent in the string
        6. Get the new value of result.
            - Using the new value, repeat 1 - 5 based on the number of times required.
        4. Return the len after the final number of repeat.

# Code
'''

# Solution
def digit_wise_addition(string):
    plus_one_dict = {str(num) : str(num + 1) for num in range(0, 10)}
    return plus_one_dict[string]

def get_digit_wise_addition(integer):
    string_int = str(integer)
    result = ''

    for num in string_int:
        result += digit_wise_addition(num)

    return result

def digit_wise_addition_pro(number, count):
    digit_wise_num = number
    result = ''

    for _ in range(count):
        digit_wise_num = get_digit_wise_addition(digit_wise_num)
        result = digit_wise_num

    return len(str(result))

# other solution:

# Code Check
print(digit_wise_addition_pro(9812, 2) == 6)
print(digit_wise_addition_pro(9899, 3) == 8)

# Note!
# Time take to write PEDAC and test/debug code 19 mins 07 seconds

# I know this could have beeter been solved with recusion but still yeat to learn about recursion.

## LS Answer ##
# Not Available