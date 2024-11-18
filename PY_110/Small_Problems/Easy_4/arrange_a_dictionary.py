'''
Arrange a Dictionary.
Given a dictionary, return its keys sorted by the values associated with each key.

# Problem
- Input: 
Dictionary
- Output:
list

- Rules
    Explicit:
    list of keys must be sorted alphabetically.
    Implicit:

# Examples
my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True

# Data structure
Dictionary and list.

# Algorithm
    - High End:
        1. Get input.
        2. Invert the dictionary to have its key as values and vice versa.
        3. Iterate through the swapped dictionary and sort its keys (now values) 
           and get the sorted values (now keys).
        4. Convert to list and return it.
        5. Return list.

# Code
'''

# Solution
def order_by_value(dct):
    swapped_dict = {value: key for key, value in dct.items()}

    return [value for _, value in sorted(swapped_dict.items())]

# code check
my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict))# == keys)  # True

# Note!
# Time take to write PEDAC and test/debug code is 17 mins, 26 seconds.
# I first tried to use the sorted function but could get through with a way that works. 
# So i decided to change my algorithm and swapped the dictionary values and keys. 
# Then it was easier to follow through.

## LS Answer ##
# def sort_key(item):
#     return item[1]

# def order_by_value(d):
#     sorted_items = sorted(d.items(), key=sort_key)
#     return [key for key, value in sorted_items]