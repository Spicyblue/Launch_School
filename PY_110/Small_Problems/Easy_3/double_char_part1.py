'''
Double Char (Part 1).
Write a function that takes a string, doubles every character in the string,
then returns the result as a new string.

# Problem
- Input: 
String
- Output:
String

- Rules
    Explicit:
    Doubles every string including spaces.
   
# Examples

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True

# Data structure
list or none

# Algorithm
    - High End 
        1. Get input.
        2. Set an empty string to hold result.
        2. Iterate through each char input:
            - For each element, double the character.
            - Add to result
        3. Return result

# Code
'''

# Solution
def repeater(string):

    result = ''

    for char in string:
        result = result + (char * 2)
    
    return result

#using list comprehension
def repeater_2(string):
    return ''.join([(char*2) for char in string])

# Code Check
print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True
print(repeater_2('Hello') == "HHeelllloo")              # True
print(repeater_2('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater_2('') == "")                             # True

# Note!
# Time take to write PEDAC and test/debug code is 5 mins, 13 seconds.

## LS Answer ##

# def repeater(string):
#     return ''.join([char * 2 for char in string])