'''
Delete Vowels.
Write a function that takes a list of strings and returns a list of the same string values,
but with all vowels (a, e, i, o, u) removed.

# Problem
- Input: 
List 
- Output:
List

- Rules
    Explicit:
    Removes all vowels in string.
    Implicit:

# Examples

# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True

# Data structure
List

# Algorithm
    - High End:
        1. Get input.
        2. Create a constant to hold vowels.
        3. Create a new list to hold result.
        5. Iterate through input.
            - Access the element in the list.
                - Create a string to hold char results.
                - Iterate through the char in the element.
                    - Check if char is not in constant:
                    - Add char to string.
                    - Repeat for all char.
                - Append strings to result list.
                - Reset string to empty.
        4. Return list.
        
# Code
'''

# Solution
VOWELS = 'aeiou'
def remove_vowels(lst):

    result = []

    for element in lst:
        cleaned_string = ''  # resets the string every for every new list element.

        for char in element:
            if char.casefold() not in VOWELS:
                cleaned_string +=  char

        result.append(cleaned_string)

    return result

# code check
# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True

# Note!
# Time take to write PEDAC and test/debug code is 12 mins, 54 seconds.

## LS Answer ##
# def strip_vowels(string):
#     VOWELS = "aeiouAEIOU"
#     no_vowels = [char for char in string
#                  if char not in VOWELS]
#     return ''.join(no_vowels)

# def remove_vowels(string_list):
#     return [strip_vowels(string) for string in string_list]