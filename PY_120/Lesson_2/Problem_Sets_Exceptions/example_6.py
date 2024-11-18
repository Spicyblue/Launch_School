'''
Example 6.

Write a function that takes a list of numbers and returns
the inverse of each number (if n is a number, then 1 / n is its inverse).
Handle any exceptions that might occur.

'''

# Solution

def get_inverse(lst):
    
    for num in lst:
        if validate_number(num):
            valid_num = int(num)
            validate_inverse(valid_num)

def validate_inverse(num):
    try:
        result = 1 / num
    
    except ZeroDivisionError as e:
        print(f'{num} cannot be divided by zero', e, )
    else: 
        print(f'The inverse of {num} is {result}')

def validate_number(num):
    try:
        num  =  int(num)
        return True
    except ValueError as e:
        print(f" {num} is not a valid number'", e)
        return False

my_list = [num for num in range(2, 10, 2)]
my_list_new = ['20', '10', '5', '0']
word_list = ['Hello']

get_inverse(my_list)
get_inverse(my_list_new)
get_inverse(word_list)

## LS Solution ##
# def invert_numbers(numbers):
#     result = []
#     for num in numbers:
#         try:
#             result.append(1 / num)
#         except ZeroDivisionError:
#             result.append(float('inf'))  # or handle as desired

#     return result

# numbers = [1, 2, 0, 3, 4]
# print(invert_numbers(numbers))
# # [1.0, 0.5, inf, 0.3333333333333333, 0.25]
