'''
Mutable Default Arguments.
We want to create a function that appends a given value to a list. 
However, the function seems to be behaving unexpectedly:
'''

# # Current code
# def append_to_list(value, lst=[]):
#     lst.append(value)
#     return lst

# print(append_to_list(1) == [1])
# print(append_to_list(2) == [2])

'''
Issue with the current code:
The current code sets a `lst` default parameter as an empty list which is mutable.
However, every time the function is called, since list are mutable,
the default value of the paramenter gets updated.

To solve this, we set 'lst' default parameter to `None` and within the function definition of `append_to_list`,
only initilize `lst` to reference to an empty list if `lst` is None.
This was, `lst` doesnt get mutated after every function call.
'''

# fixed code 
def append_to_list(value, lst = None):
    if lst is None:
        lst = []

    lst.append(value)
    return lst

print(append_to_list(1) == [1])
print(append_to_list(2) == [2])

print(append_to_list(11, [10]) == [10, 11])
print(append_to_list(12, [10, 11, 12]) == [10, 11, 12, 12])

# Note!
# Time take to debug code is 1 mins, 20 seconds.
# Took more time to write the reason for the error but didnt include it.

## LS Answer ##
# def append_to_list(value, lst=None):
#     if lst is None:
#         lst = []

#     lst.append(value)
#     return lst

# print(append_to_list(1) == [1])
# print(append_to_list(2) == [2])

# Discussion
# In Python, default mutable arguments are shared between function calls.
# This means that if you modify the default argument,
# its state will persist across function calls.
# In the initial function, the list lst is only created once and is shared across function calls. 
# As a result, when we append to the list in subsequent calls, we're appending to the same list.

# The refactored solution uses None as the default value and initializes the list inside the function,
# ensuring a fresh list is used every time the function is called.