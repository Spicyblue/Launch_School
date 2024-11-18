'''
Available at https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python
Level = 6kyu

Split Strings.
Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace
the missing second character of the final pair with an underscore ('_').

Examples:
* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']


# Problem
- Input: 
String
- Output:
List

- Rules
    Explicit:
    - Splits the string into pairs of two .
    - For odd pair, add a _ to the end

    Implicit:
    - Return and empty list for empty string.

# Examples
print(split_string("asdfadsf" ) == ['as', 'df', 'ad', 'sf'])
print(split_string("asdfads" ) == ['as', 'df', 'ad', 's_'])
print(split_string("" ) == [])
print(split_string("x" ) == ["x_"])

# Data structure
List 

# Algorithm
    High level
    1. Get all the pairs in the string.
    2. Add the to the list, and add a _ to odd pairs.
    3. Get back the list.

    Low level:
        1. Get input.
        2. Create list to hold string.
        3. Iterate through the input:
            - Get the first two character:
                - check if the len of the character is 2:
                - If yes, add string to the list
                - If not, add _ and then add the string to the list.
                - repeat for all strings.

        4. Return the list

# Code
'''

# Solution
def split_string(string):
    result = []

    for idx in range(0, len(string), 2):
        two_word = string[idx: idx + 2]
        if len(two_word) == 2:
            result.append(two_word)
        else:
            two_word += '_'
            result.append(two_word)

    return result
            

# other solution:
# def split_string(string):
#     return [string[idx : idx + 2] if len(string[idx: idx +2]) == 2
#              else string[idx : idx + 2] + '_' 
#              for idx in range(0, len(string), 2)]

# def split_string(string):
#     result = []
#     if len(string) % 2:
#         string += '_'
#     for i in range(0, len(string), 2):
#         result.append(string[i:i+2])
#     return result


# Code Check
print(split_string("asdfadsf" ) == ['as', 'df', 'ad', 'sf'])
print(split_string("asdfads" ) == ['as', 'df', 'ad', 's_'])
print(split_string("" ) == [])
print(split_string("x" ) == ["x_"])

# Note!
# Time take to write PEDAC and test/debug code 8 mins 37 seconds

## LS Answer ##
# Not Available