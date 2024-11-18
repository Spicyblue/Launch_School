'''
Double Char (Part 2).
Write a function that takes a string, doubles every consonant in the string,
and returns the result as a new string.
The function should not double vowels ('a','e','i','o','u'), digits, punctuation, or whitespace.

You may assume that only ASCII characters will be included in the argument.

# Problem
- Input: 
String
- Output:
String

- Rules
    Explicit:
    Doubles every consonant in the string.
    The function should not double vowels ('a','e','i','o','u'), digits, punctuation, or whitespace.

# Examples
# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")

# Data structure
none

# Algorithm
    - High End 
        1. Get input.
        2. Set an empty string to hold result.
        2. Iterate through each char input:
            - For each ele, double the character if char is consonant.
            - Add to result.
            - If char isn't a consonant, add char to result without doubling.
        3. Return result.

# Code
'''

# Solution
CONSONANTS = 'BCDFGHJKLMNPQRSTVWXYZ'
 
def double_consonants(string):

    result = ''

    for char in string:
        if char.upper() in CONSONANTS:
            result += char * 2
        else:
            result += char
    
    return result

# Code Check
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")

# Note!
# Time take to write PEDAC and test/debug code is 7 mins, 39 seconds.

## LS Answer ##
# CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

# def double_consonants(string):
#     result = []

#     for char in string:
#         if char.lower() in CONSONANTS:
#             result.append(char * 2)
#         else:
#             result.append(char)

#     return ''.join(result)
