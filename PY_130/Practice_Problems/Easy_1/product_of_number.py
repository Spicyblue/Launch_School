'''
Product of Numbers.
Calculate the product of all numbers in a list using the reduce function.
'''

# Solution

from functools import reduce
lst = [1, 2, 3, 4, 5]
lst_product = reduce(lambda num1, num2: num1 * num2, lst)
print(lst_product)

## LS Solution ##
# Solution 1
# from functools import reduce
# product = reduce(lambda x, y: x * y, [1, 2, 3, 4])

# Solution 2
# from functools import reduce
# def multiply(x, y):
#     return x * y
# product = reduce(multiply, [1, 2, 3, 4])