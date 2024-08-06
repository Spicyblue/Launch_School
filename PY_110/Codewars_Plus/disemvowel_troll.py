'''
Available at https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python
Level = 7kyu

Disemvowel Trolls.
Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
Your task is to write a function that takes a string and return a new string with all vowels removed.
For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
Note: for this kata y isn't considered a vowel.

# Problem
- Input: 
String
- Output:
String

- Rules
    Explicit:
    - Remove all the vowels in original string.
    - Case sensitive. 
    - Spaces and non numeric characters remain the same.

    Implicit:

# Examples
print(disemvowel('This website is for losers LOL!') == 'Ths wbst s fr lsrs LL!')

# Data structure
List or none

# Algorithm
    High level
    1. Get through the string.
    2. Remove all vowel.
    3. Get back the new string.

    Low level:
        1. Get input.
        2. Create a string of vowels.
        3. Create a string to hold result. 
        3. Iterate through the input:
            - Convert the current character to lowercase.
            - Check if the character is not in vowel.
                - Increment the new string by the character.
                - repeat for all strings.

        4. Return the result

# Code
'''

# Solution
VOWEL = 'aeiou'

# def disemvowel(string):

#     result = ''

#     for char in string:
#         if char.casefold() not in VOWEL:
#             result += char

#     return result

# using list comprehension
def disemvowel(string):
    return "".join([char for char in string if char.casefold() not in 'aeiou'])

# Code Check
print(disemvowel('This website is for losers LOL!') == 'Ths wbst s fr lsrs LL!')

# Note!
# Time take to write PEDAC and test/debug code 6 mins 23 seconds

## LS Answer ##
# Not Available