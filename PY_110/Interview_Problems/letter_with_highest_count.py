'''
Letter with highest count.
Create a function that takes a string argument and returns the character that occurs most often in the string. 
If there are multiple characters with the same greatest frequency, return the one that appears first in the string.
When counting characters, consider uppercase and lowercase versions to be the same.

# Problem
- Input: 
String
- Output:
String

- Rules
    Explicit:
    - When counting characters, consider uppercase and lowercase versions to be the same.
    - If there are multiple characters with the same greatest frequency, return the one that appears first in the string.
    - Returns the character that occurs most often in the string.

# Examples
print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')

# Data structure
None

# Algorithm
    High Level:
    1. Make a count of ever letter in the sentence.
    2. Get back the letter that occurs most.

    Low level:
        1. Get input.
        2. Create a result to store string.
        3. Create a counter for max count.
        4. Iterate through the input in lowercase:
            - Check the count of the current element in lowercase:
                - If the value is greater than the max count.
                - max count becomes the count
                - result becomes the current string.
                - repeat for all element
        5. Return result

# Code
'''

# Solution
def most_common_char(string):
    result = ''
    max_count = 0

    for char in string:
        string_lower = string.casefold()
        letter_lower = char.casefold()
        count = string_lower.count(letter_lower)

        if count > max_count:
            max_count = count
            result = letter_lower

    return result

# code check
print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')

# Note!
# Time take to write PEDAC and test/debug code 16 mins 22 seconds

## LS Answer ##
# Not Available
