'''
Example 5.

Modify your answer from the previous problem to raise a custom exception named 
NegativeNumberError instead of an ordinary ValueError exception.

'''

# Solution

class NegativeNumberError(ValueError):
    message = 'This is a negative error'

def ask_first_input():
    while True:
        number = input('Please enter the first number ')
        if validate_number(number):
            number  = int(number)
            check_negative(number)
            return number

def check_negative(num1):
    if num1 < 0:
        raise NegativeNumberError

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
# class NegativeNumberError(ValueError):
#     pass

# num = float(input('Enter a number: '))
# if num < 0:
#     raise NegativeNumberError('Negative numbers are not allowed!')
# print(f'You entered {num}')
# Note that our custom exception inherits from ValueError since 
# it's a special case of a ValueError much as ZeroDivisionErrors are also ValueErrors.

# If you subclassed Exception instead, that's fine too.