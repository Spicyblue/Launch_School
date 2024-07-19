'''
Matching Parenthesis?
Write a function that takes a string as an argument and returns
True if all parentheses in the string are properly balanced, False otherwise.
To be properly balanced, parentheses must occur in matching '(' and ')' pairs.

Note that balanced pairs must start with a (, not a ).

# Problem
- Input: 
String
- Output:
Bool

- Rules
    Explicit:
    Returns True if all parentheses in the string are properly balanced, False otherwise.
    Note that balanced pairs must start with a (, not a ).
    Implicit:
    A parenthesis cannot end with (.

# Examples
print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True

# Data structure
list

# Algorithm
    - High End 
        1. Get input.
        2. Create a result to store paranthesis.
        3. Iterate through the list.
            - Add only parenthesis to the result.
        4. If parentheses starts with ) or ends with (.
                - Return False
        5. Check the count of the parenthesis in both string and return True if they are the equall.

# Code
'''

# Solution
def is_balanced(string):

    parenthesis = ''

    for char in string:
        if char in ['(', ')']:
            parenthesis += char

    if parenthesis.startswith(')') or parenthesis.endswith('('):
        return False

    return parenthesis.count('(') == parenthesis.count(')')

#Code Check
print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True

# Note!
# Time take to write PEDAC and test/debug code is 10 mins, 58 seconds.

## LS Answer ##
# def is_balanced(s):
#     parens = 0
#     for char in s:
#         if char == "(":
#             parens += 1
#         elif char == ")":
#             parens -= 1
#         if parens < 0:
#             return False
#     return parens == 0