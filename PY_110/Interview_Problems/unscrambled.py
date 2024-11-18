'''
Unscrambled.
Create a function that takes two strings as arguments and returns True 
if some portion of the characters in the first string can be rearranged to match the characters in the second.
Otherwise, the function should return False.
You may assume that both string arguments only contain
lowercase alphabetic characters. Neither string will be empty.

# Problem
- Input: 
String
- Output:
Bool

- Rules
    Explicit:
    - All characters in second string must be in frist string.
    Implicit:

# Examples
print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)

# Data structure
Set and list

# Algorithm
    High level
    1. Compare substring with string
    2. Return result of comparison

    Low level:
        1. Get input.
        2. iterate through the second string
            - Check if current character is in first stirng
                - Return false if not in main string.
        3. Return true if all character in main string.

# Code
'''

# Solution
def unscramble(scrambled_string, main_string):
    for char in main_string:
        if char not in scrambled_string:
            return False

    return True
    
# Code Check
print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)

# Note!
# Time take to write PEDAC and test/debug code 10 mins 52 seconds

## LS Answer ##
# Not Available
