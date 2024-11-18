'''
Example 9.

Given the following list:

numbers = [1, 2, 3, 4, 5]
Write two functions to fetch the sixth element from the list:
one using the LBYL approach and another using the AFNP approach.
In both cases, the function should return None when the element isn't found.

'''

# Solution
numbers = [1, 2, 3, 4, 5]

def get_sixth_element_lbly(lst):
    if len(lst) <= 5:
        return None
    
    return lst[5]

def get_sixth_element_afnp(lst):
    try:
        return lst[5]
    
    except IndexError:
        return None

print(get_sixth_element_lbly(numbers))
print(get_sixth_element_afnp(numbers))

## LS Solution ##
# LBYL approach
# def get_sixth_element_lbyl():
#     if len(numbers) > 5:
#         return numbers[5]

#     return None

# # AFNP approach
# def get_sixth_element_afnp():
#     try:
#         return numbers[5]
#     except IndexError:
#         return None
