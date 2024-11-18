'''
Staggered Case (Part 1).
Write a function that takes a string as an argument and
returns that string with a staggered capitalization scheme.
Every other character, starting from the first,
should be capitalized and should be followed by a lowercase or non-alphabetic character.
Non-alphabetic characters should not be changed,
but should be counted as characters for determining when to switch between upper and lower case.

# Problem
- Input:
String
- Output:
String

- Rules
    Explicit:
    Returns that string with a staggered capitalization scheme.
    Non-alphabetic characters should not be changed
    but should be counted as characters for determining when to switch between upper and lower case.
    Implicit:

# Examples

string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True

# Data structure

# Algorithm
    - High End:
        1. Get input.
        2. Create a result to store string.
        3. Iterate through the input.
            - If the index position is even, convert string to upper case and add to result.
            - Else, covert string to lower case for odd index and add to result.
            - Repeat for all element.
        4. Return result.
        
# Code
'''

# Solution
def staggered_case(string):

    result = ''

    for idx in range(len(string)):
        if idx % 2 == 0:
            result += string[idx].upper()
        else:
            result += string[idx].lower()

    print(result)

    return result

# code check
string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True

# Note!
# Time take to write PEDAC and test/debug code is 5 mins, 32 seconds.

## LS Answer ##
# def staggered_case(string):
#     result = ''
#     for idx, char in enumerate(string):
#         func = char.upper if idx % 2 == 0 else char.lower
#         result += func()

#     return result