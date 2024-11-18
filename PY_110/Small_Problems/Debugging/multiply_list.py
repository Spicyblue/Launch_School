'''
Multiply List.
You want to multiply all elements of a list by 2.
However, the function is not returning the expected result.
Explain the bug, and provide a solution.
'''

# # Current code
# def multiply_list(lst):
#     for item in lst:
#         item *= 2

#     return lst

# print(multiply_list([1, 2, 3]) == [2, 4, 6])

'''
Issue with the current code:
Within the fuction definition of `multiply_list`,
although we are multiply each element within the list by 2,
we are not reassigning the list element after the operation.

To solve this, we can create a new list and append the result of the operation `ìtem *= 2` 
to the new list and return the new list after the ietration is complete.

If we want to mutate the list in place, 
we can access perform a index reassignment or element reassignment by initializing a variable `index`
to access the correct element referenced by `lst`  and incrementing it by 1 after each iteration. 
However, is not an ideal practice.
'''

# fixed code with new list
def multiply_list(lst):
    result = []
    for item in lst:
        item *= 2
        result.append(item)

    return result

print(multiply_list([1, 2, 3]) == [2, 4, 6])

# fixed code mutating the list in place.
def multiply_list2(lst):
    idx = 0
    for item in lst:
        lst[idx] = item * 2
        idx += 1

    return lst

print(multiply_list2([1, 2, 3]) == [2, 4, 6])

# Note!
# Time take to debug code is 4 mins, 12 seconds.
# Took more time to write the reason for the error but didnt include it.

## LS Answer ##
# def multiply_list(lst):
#     return [item * 2 for item in lst]

# print(multiply_list([1, 2, 3]) == [2, 4, 6])  # True