'''
Leading Substrings.
Write a function that takes a string argument and returns a list of substrings of that string.
Each substring should begin with the first letter of the word,
and the list should be ordered from shortest to longest.

# Problem
- Input: 
String
- Output:
List of substrings

- Rules
    Explicit:
    Each substring should begin with the first letter of the word.
    The list should be ordered from shortest to longest
    Implicit:

# Examples
# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])

# Data structure
list

# Algorithm
    - High End:
        1. Get input.
        2. Create a list to hold result.
        3. Create an end index and set it to 1.
        4. Iterate through the string.
           - Using string indexing, access the string element from start to the end index.
           - Add element to list.
           - Increase index by 1.
        5.Return list.

# Code
'''

# Solution
def leading_substrings(string):

    result = []
    end = 1

    while end < len(string) + 1:
        sub_string = string[: end]
        result.append(sub_string)
        end += 1

    return result

# code check
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])

# Note!
# Time take to write PEDAC and test/debug code is 7 mins, 09 seconds.

## LS Answer ##
# def unique_from_first(list1, list2):
#     return set(list1) - set(list2)
