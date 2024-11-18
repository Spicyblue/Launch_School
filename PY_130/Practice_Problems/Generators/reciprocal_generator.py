'''
Reciprocal generator.
Create a generator expression that generates the reciprocals of the numbers from 1 to 10. 
A reciprocal of a number n is 1 / n. Use a for loop to print each value.
'''

# Solution
reciprocal = (1/x for x in range(1, 10))

for values in reciprocal:
    print(values)

## LS Solution ##
# reciprocals = (1 / x for x in range(1, 11))

# for value in reciprocals:
#     print(value)
