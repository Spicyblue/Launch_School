'''
Reciprocal generator function.
Create a generator expression that generates the reciprocals of the numbers from 1 to 10.
A reciprocal of a number n is 1 / n. Use a for loop to print each value.
'''

def reciprocal(num):
    
    for numbers in range(1, num + 1):
        result = 1 / numbers
        yield result

reciprocals_nums = reciprocal(10)

for values in reciprocals_nums:
    print(values)