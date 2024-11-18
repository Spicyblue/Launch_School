# Odd Numbers
# Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.
# Bonus Question: Can you solve the problem by iterating over just the odd numbers?

# Solution

for x in range(1, 100):
    if x % 2 == 1:
        print(x)

for x in range(1, 100, 2):
    print (x)

begining_number = int(input('Enter start number: '))

ending_number = int(input('Enter end number: '))

def odd_numbers(start, end):
    if start > end:
        print ('Odd number cannot be printed backward!')
    elif start == end:
        print ('odd number operation cannot be performed!')
    else:
        print('Odd number will be printed forward')

    for num in range(start, end + 1, 2):
        print (num)

odd_numbers(begining_number, ending_number)