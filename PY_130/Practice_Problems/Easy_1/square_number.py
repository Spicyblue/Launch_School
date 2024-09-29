'''
Square Number.
Create a list where each number from the original list
is squared using the map method.
'''

# Solution
lst = [2, 4, 6, 8, 10]
squared_list = list(map(lambda number: number * number, lst))
print(squared_list)

## LS Solution ##
# Solution 1
# squared_numbers = list(map(lambda x: x**2, [1, 2, 3, 4]))

# Solution2
# def square(x):
#     return x ** 2

# squared_numbers = list(map(square, [1, 2, 3, 4]))