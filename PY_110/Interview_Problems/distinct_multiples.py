'''
Distinct multiples.
Create a function that returns the count of distinct case-insensitive alphabetic characters.
and numeric digits that occur more than once in the input string.
You may assume that the input string contains only alphanumeric characters.

# Problem
- Input: 
String
- Output:
Integer

- Rules
    Explicit:
    - Computes the count of distinct case-insensitive alphabetic characters and 
    numeric digits that occur more than once in the input string.
    - The argument contains only alphanumeric characters..

    Implicit:

# Examples
print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5

# Data structure
None

# Algorithm
    High level
    1. Get all character that count more than once
    2. Get how many of them are present.

    Low level:
        1. Get input.
        2. Create a result to store double digit.
        3. Check if input is a string, 
            - If yes, convert the string to lowercase.
        4. Interate through the string:
            - get the count of the current character.
            - Check if the count is greater than one.
                If yes, add the current character to the result.
                repeat for all string
        5. Covert the result to a set.     
        6. Return the lenght of the set.

# Code
'''

# Solution
def distinct_multiples(string):
    if isinstance(string, str):
        string = string.casefold()
    
    result = ''

    for char in string:
        count = string.count(char)
        if count > 1:
            result += char

    final_result = set(result)

    return len(final_result)

# using a dictionary
# def distinct_multiples(string):
#     if isinstance(string, str):
#         string = string.casefold()

#     result = {char : string.count(char) for char in string if string.count(char) > 1}

#     return len(result)

# Code Check
print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5

# Note!
# Time take to write PEDAC and test/debug code 12 mins 39 seconds

## LS Answer ##
# Not Available