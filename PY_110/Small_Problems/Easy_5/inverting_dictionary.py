'''
Inverting Dictionary.
Given a dictionary where both keys and values are unique,
invert this dictionary so that its keys become values and its values become keys.

# Problem
- Input: 
Dictionary
- Output:
Dictionary

- Rules
    Explicit:
    Invert dictionary key and values.
    Implicit:

# Examples

print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True

# Data structure
Dictionary.

# Algorithm
    - High End:
        1. Get input.
        2. Create a new dictionary to hold result.
        3. Iterate through input:
            - Get dictionary value and set as key of result dictionary.
            - Get dictionary key and set as value of result dictionary.
            - Repeat for all key and values.
        4. Return result.
        
# Code
'''

# Solution
def invert_dict(dct):

    result = {value : key for key, value in dct.items()}

    return result

# Solution 2
def invert_dict2(dct):
    result = {}

    for key, value in dct.items():
        result[value] = key

    return result

# code check
print(invert_dict2({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True

# Note!
# Time take to write PEDAC and test/debug code is 3 mins,10 seconds.

## LS Answer ##
# def invert_dict(my_dict):
#     return {value: key for key, value in my_dict.items()}
    