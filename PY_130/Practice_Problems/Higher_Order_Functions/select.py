'''
Select.
Write a select function that mimics the built-in filter function.
Your select function should take two arguments: a callback function and an iterable object.
It should return a list of all the elements of the iterable for
which the callback function returns a truthy value.
It should not include any elements for which the callback returns a falsy value.
Start by writing a function that doesn't use any comprehensions.
Once your code works, refactor it to use a comprehension.
You can use the following examples to test your code:

'''

# Solution 
def select(callback, iterable):
    result = []
    for item in iterable:
        if callback(item):
            result.append(item)

    return result

numbers = [1, 2, 3, 4, 5]
colors = {'red', 'orange', 'yellow', 'green',
          'blue', 'indigo', 'violet'}

odd_numbers = select(lambda number: number % 2 != 0, numbers)
print(odd_numbers)            # [1, 3, 5]

large_numbers = select(lambda number: number >= 10, numbers)
print(large_numbers)          # []

small_numbers = select(lambda number: number < 10, numbers)
print(small_numbers)          # [1, 2, 3, 4, 5]

short_color_names = select(lambda color: len(color) <= 5, colors)
print(short_color_names)      # ['blue', 'red', 'green']
# The order of the colors may vary, but should include the
# indicated colors.

# using comprehension
def select2(callback, iterable):
    return [item for item in iterable if callback(item)]

odd_numbers = select2(lambda number: number % 2 != 0, numbers)
print(odd_numbers)            # [1, 3, 5]

large_numbers = select2(lambda number: number >= 10, numbers)
print(large_numbers)          # []

small_numbers = select2(lambda number: number < 10, numbers)
print(small_numbers)          # [1, 2, 3, 4, 5]

short_color_names = select2(lambda color: len(color) <= 5, colors)
print(short_color_names)      # ['blue', 'red', 'green']
# The order of the colors may vary, but should include the
# indicated colors.

# LS Solution
# without comprehension
# def select(callback, iterable):
#     selected = []
#     for item in iterable:
#         if callback(item):
#             selected.append(item)

#     return selected

# with comprehension
# def select(callback, iterable):
#     return [item for item in iterable if callback(item)]