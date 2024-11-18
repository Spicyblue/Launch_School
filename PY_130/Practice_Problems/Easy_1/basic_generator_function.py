'''
Basic Generator Function.
Create a generator function that yields numbers from 1 to 5.
'''

# Solution

def basic():
    for num in range(1, 6):
        yield num

generator_nums = (basic())

for nums in generator_nums:
    print(nums)

## LS Solution ##
# def number_generator():
#     for i in range(1, 6):
#         yield i

# for number in number_generator():
#     print(number)