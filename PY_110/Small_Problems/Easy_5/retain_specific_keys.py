'''
Retain Specific Keys.
Given a dictionary and a list of keys,
produce a new dictionary that only contains the key/value pairs for the specified keys.

# Problem
- Input: 
Dictionary and list
- Output:
Dictionary

- Rules
    Explicit:
    New dictionary only contains the key/value pairs for the specified keys.
    Implicit:

# Examples

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True

# Data structure
Dictionary and list

# Algorithm
    - High End:
        1. Get input.
        2. Create a new dictionary to hold result.
        3. Iterate through input.
            - If dictionary key in list input, add dictionary key and its value to result.
            - Repeat for all key and values.
        4. Return result.
        
# Code
'''

# Solution
def keep_keys(dct, lst):

    result = {key : value for key, value in dct.items() if key in lst}

    return result

# # Solution 2
# def keep_keys2(dct, lst):
#     result = {}

#     for key, value in dct.items():
#         if key in lst:
#             result[key] = value

#     return result

# code check
input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True

# Note!
# Time take to write PEDAC and test/debug code is 3 mins, 54 seconds.

## LS Answer ##
# def keep_keys(my_dict, key_list):
#     new_dict = {}
#     for key in key_list:
#         if key in my_dict:
#             new_dict[key] = my_dict[key]

#     return new_dict

# Solution 2
# def keep_keys(my_dict, key_list):
#     return {key: my_dict[key]
#             for key in key_list
#             if key in my_dict}
