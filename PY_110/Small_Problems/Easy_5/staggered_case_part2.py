'''
Staggered Case (Part 2).
Modify the function from the previous exercise so it ignores non-alphabetic characters
when determining whether it should uppercase or lowercase each letter.
The non-alphabetic characters should still be included in the return value;
they just don't count when toggling the desired case.

# Problem
- Input: 
String
- Output:
String

- Rules
    Explicit:
    Returns that string with a staggered capitalization scheme.
    Ignore non-alphabetic characters when determining whether it should uppercase or lowercase each letter.
    The non-alphabetic characters should still be included in the return value.
    Implicit:

# Examples

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
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
        3. Create a counter that increases for only alphabetic character.
        4. Iterate through the input.
            - If string is not alphabetic, add string to result 
                - Do not increase counter.
            - If counter even, convert string to upper case and add to result.
                - Increase counter.
            - If counter is odd,  covert string to lower case for odd index and add to result.
            - Repeat for all element.
        5. Return result.
        
# Code
'''

# Solution
def staggered_case(string):

    result = ''
    counter = 0

    for idx in range(len(string)):
        if not string[idx].isalpha():
            result += string[idx]
            counter += 0

        elif counter % 2 == 0:
            result += string[idx].upper()
            counter += 1
        else:
            result += string[idx].lower()
            counter += 1

    return result

# code check
string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True

# Note!
# Time take to write PEDAC and test/debug code is 12 mins, 32 seconds.

## LS Answer ##
# def staggered_case(string):
#     result = ''
#     upper = True

#     for char in string:
#         if char.isalpha():
#             result += char.upper() if upper else char.lower()
#             upper = not upper
#         else:
#             result += char

#     return result