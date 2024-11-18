'''
Even Numbers.
Obtain only the even numbers from a list using the filter function.
'''

# Solution
lst = list(range(0, 21))
even_list = list(filter(lambda number: number % 2 == 0, lst))
print(even_list)

## LS Solution ##
# Solution 1
# even_numbers = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))

# Solution2
# def is_even(x):
#     return x % 2 == 0

# even_numbers = list(filter(is_even, [1, 2, 3, 4, 5, 6]))