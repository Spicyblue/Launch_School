'''
Pangram.
Create a function that takes a string as an argument and
returns True if the string is a pangram, False if it is not.
Pangrams are sentences that contain every letter of the alphabet at least once.
For example, the sentence "Five quacking zephyrs jolt my wax bed."
is a pangram since it uses every letter at least once. Note that case is irrelevant.

# Problem
- Input: 
String
- Output:
Bool

- Rules
    Explicit:
    - Pangrams are sentences that contain every letter of the alphabet at least once.
    Implicit:

# Examples
print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)
my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)

# Data structure
Set and list

# Algorithm
    High level
    1. Get all the alphabet
    2. Make sure atlease all the alphabet are in the string.
    3. Get back answer.

    Low level:
        1. Get input.
        2. Create a set of all the alphabets
        3. Create an Empty string:
        4. Iterate through the string:
            - Check if character is alphabetic.
            - Convert the character to lowercase.
            - Increment the empty string by the charater.
            - Reperat for all character.
        5. Conver the result string to a set
        6. Return the result of comparing the set of string to the set of alphabets.

# Code
'''

# Solution
def is_pangram(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = set(alphabet)
    join_string = ''.join([char.casefold() for char in string if char.isalpha()])
    result = set(join_string)

    return result == alphabet

# Code Check
print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)
my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)

# Note!
# Time take to write PEDAC and test/debug code 13 mins 52 seconds

## LS Answer ##
# Not Available
