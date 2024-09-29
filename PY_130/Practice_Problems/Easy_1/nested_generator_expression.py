'''
Nested Generator Expressions.
Use nested generator expressions to create a flat list of numbers from a list of lists.
'''

# Solution

def flatten_lst(lst_input):

    for outer_number in lst_input:
        for number in outer_number:
            yield number

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
generator_lst_of_number = (flatten_lst(lst))

print(list(generator_lst_of_number))

for num in generator_lst_of_number:
    print(num)

# note that the last line `print(num)` does not output anything since generators are single use :D

## LS Solution ##
# Solution
# nested_lists = [[1, 2, 3], [4, 5], [6]]

# flat_generator = (num for sub-list in nested_lists for num in sub-list)

# for number in flat_generator:
#     print(number)