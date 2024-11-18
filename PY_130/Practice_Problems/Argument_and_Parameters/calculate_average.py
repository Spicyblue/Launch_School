'''
Calculate Average.
Write a function named calculate_average that any number of
numeric arguments and returns their average.
Make sure it returns None if no arguments are provided.
'''

# Solution

def calculate_average(*numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
    

print(calculate_average()) # None
print(calculate_average(1, 2, 3, 4, 5)) # outputs 3.0

## LS Solution ##
# def calculate_average(*args):
#     return sum(args) / len(args) if args else None

# print(calculate_average(1, 2, 3, 4))      # 2.5
# print(calculate_average(1, 2, 3, 4, 5))   # 3.0
# print(calculate_average())                # None