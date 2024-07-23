'''
Key Check.
You have a function that should check whether a key exists in a dictionary and returns its value.
However, it's raising an error.
Why is that? How would you fix this code?
'''

# # Current code
# def get_key_value(my_dict, key):
#     if my_dict[key]:
#         return my_dict[key]
#     else:
#         return None

'''
Issue with the current code:
The error occurs because the `if` conditional only returns the value for a valid `key` argument.
For invalid keys, it raises an key error.

To solve this, we need to check if the `key` argument is in the dictionary, and if present, return its value.
to the new list and return the new list after the ietration is complete.
'''

# fixed code with new list
# def get_key_value(my_dict, key):
#     if key in my_dict:
#         return my_dict[key]
#     else:
#         return None

# print(get_key_value({"a": 1}, "b"))

# fixed code mutating the list in place.

# Note!
# Time take to debug code is 1 mins, 12 seconds.
# Took more time to write the reason for the error but didnt include it.

## LS Answer ##
# def get_key_value(my_dict, key):
#     return my_dict.get(key, None)