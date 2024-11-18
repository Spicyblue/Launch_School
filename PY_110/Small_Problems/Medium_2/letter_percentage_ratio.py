'''
Lettercase Percentage Ratio.
Write a function that takes a string and returns a dictionary containing the following three properties:

the percentage of characters in the string that are lowercase letters
the percentage of characters that are uppercase letters
the percentage of characters that are neither
All three percentages should be returned as strings whose numeric values lie between "0.00" and "100.00", respectively. 
Each value should be rounded to two decimal points.

You may assume that the string will always contain at least one character.

# Problem
- Input: 
String
- Output:
Dictionary

- Rules
    Explicit:
    Returns the percentage of characters in the string that are lowercase letters.
    Returns the percentage of characters that are uppercase letters.
    Returns the percentage of characters that are neither.
    Percentages should be returned as strings whose numeric values lie between "0.00" and "100.00", respectively.
    Each value should be rounded to two decimal points.

    Implicit:

# Examples
expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)

print(substrings('abcde') == expected_result)  # True

# Data structure
Dictionary

# Algorithm
    - High End:
        1. Get input.
        2. Create a variable to hold the sum
        3. Create a variable to hold the count of lowercase, uppercase and neither present in the input.
        4. Create an empty_dictionary
        5. Iterate through the input:
            - increase the counts based on the character
            - repeat for all element.
        
        6. Calculate the percentage and format to the correct decimal places.
        7. Add the result to the dictionary.
        8. Return the dictionary.

# Code
'''

# Solution
def get_percentage(num, denom):
    
    percentage = float(num * 100 / denom)

    return f'{percentage:.2f}'

def letter_percentages(string):
    string_lenght = len(string)
    lower_count = 0
    upper_count = 0
    other_count = 0

    string_precent_dict = {}

    for char in string:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
        else:
            other_count += 1

    lower_percent = get_percentage(lower_count, string_lenght)
    upper_percent = get_percentage(upper_count, string_lenght)
    other_percent = get_percentage(other_count, string_lenght)

    string_precent_dict['lowercase'] = str(lower_percent)
    string_precent_dict['uppercase'] = str(upper_percent)
    string_precent_dict['neither'] = str(other_percent)

    return string_precent_dict
    
# code check
expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)

# Note!
# Time take to write PEDAC and test/debug code is 23 mins, 30 seconds.

## LS Answer ##
# def percentage(count, total_count):
#     return f'{(count / total_count) * 100:.2f}'

# def letter_percentages(string):
#     total_chars = len(string)
#     lowercase_count = 0
#     uppercase_count = 0
#     neither_count = 0

#     for char in string:
#         if char.islower():
#             lowercase_count += 1
#         elif char.isupper():
#             uppercase_count += 1
#         else:
#             neither_count += 1

#     return {
#         'lowercase': percentage(lowercase_count, total_chars),
#         'uppercase': percentage(uppercase_count, total_chars),
#         'neither':   percentage(neither_count, total_chars),
#     }