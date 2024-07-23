'''
Shadow.
We defined a function intending to multiply the sum of numbers by a factor.
However, the function raises an error. Why? How would you fix this code?
'''

# # Current code
# def sum(numbers, factor):
#     return factor * sum(numbers)

# numbers = [1, 2, 3, 4]
# print(sum(numbers, 2) == 20)

'''
Issue with the current code:
The current code has a function name that is non_idiomatic because 
it uses the same name with a built-in python function and thus shadows it.

To solve this, we simply rename out function name and update all function calls with the new name.
'''

# fixed code 
def total(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(total(numbers, 2) == 20)

# Note!
# Time take to debug code is  mins, 30 seconds.
# Took more time to write the reason for the error but didnt include it.
# It was so easy to see the error at first glance. 

## LS Answer ##
# def multiply_sum(numbers, factor):
#     return factor * sum(numbers)

# numbers = [1, 2, 3, 4]
# print(multiply_sum(numbers, 2) == 20) # True

