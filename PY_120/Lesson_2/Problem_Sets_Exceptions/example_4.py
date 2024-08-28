'''
Example 4.

Write a program that asks the user for a number.
If the input isn't a number, let Python raise an appropriate exception.
If the number is negative, raise a ValueError with an appropriate error message.
If the number isn't negative, print a message that shows its value.

'''

# Solution

def ask_first_input():
    while True:
        number = input('Please enter the first number ')
        if validate_number(number):
            number  = int(number)
            check_negative(number)
            return number

def check_negative(num1):
    if num1 < 0:
        raise ValueError ('Number cant be less than zero')

def validate_number(num):
    try:
        num  =  int(num)
        return True
    except ValueError as e:
        print(f" {num} is not a valid number'", e)
        return False

def main():
    number = ask_first_input()
    print(f"{number} is a valid number")

main()

## LS Solution ##
# num = float(input('Enter a number: '))
# if num < 0:
#     raise ValueError('Negative numbers are not allowed!')
# print(f'You entered {num}')
