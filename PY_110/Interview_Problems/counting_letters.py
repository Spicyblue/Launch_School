'''
Counting letters.
Create a function that takes a string argument and returns a dict object in which the keys
represent the lowercase letters in the string, and the values represent how often the corresponding
letter occurs in the string.

# Problem
- Input: 
String
- Output:
Dictionary

- Rules
    Explicit:
    - Keys represent the lowercase letters in the string, and the values represent the count.

    Implicit:
    - Capital letters, space, symbols, or numerice characters are invalid.
    - Empty string return Empty dictionary.

# Examples
expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})

# Data structure
Dictionary

# Algorithm
    High level
    1. Make dictionary with keys as  lower letters and value as the number of times in appear
    2. Get back dictionary

    Low level:
        1. Get input.
        2. Create a empty dictionary to store result.
        3. Iterate through the input:
            - Check the input is valid (not a number, or space, or uppercase, or symbols):
                - if valid, set key to the current element and increase its value by 1
                - repeat for all element in the string.
        5. Return result

# Code
'''

# Solution
def is_valid_key(key):
    if key.islower():
        return True

    return False

def count_letters(string):
    result = {}
    
    for key in string:
        if is_valid_key(key):
            result.setdefault(key, 0)
            result[key] = string.count(key)

    return result

# using a dictionary comprehension
# def count_letters(string):
#     result = {key: string.count(key) for key in string if is_valid_key(key)}

#     return result

# code check
expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})

# Note!
# Time take to write PEDAC and test/debug code 14 mins 38 seconds

## LS Answer ##
# Not Available