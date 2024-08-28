'''
Example 1.

Write a program that asks the user for two numbers
and divides the first number by the second number. 
Handle any potential ZeroDivisionError or ValueError exceptions
(there is no need to retry inputs in this problem).

'''

# Solution

def ask_first_input():
    while True:
        number = input('Please enter the first number ')
        if validate_number(number):
            number = int(number)
            return number

def ask_second_input():
    while True:
        number = input('Please enter the second number ')
        if validate_number(number):
            number = int(number)
            return number

def perform_division(num1, num2):
    if check_zero_division(num1, num2):
        result = num1 / num2
        return int(result)

def validate_number(num):
    try:
        num  =  int(num)
        return True
    except ValueError as e:
        print(f" {num} is not a valid number'", e)
        return False

def check_zero_division(num1, num2):

    try:
        result = num1 / num2
        return True
    except ZeroDivisionError as e:
        print(f"Dividing {num1} ny {num2} is not possible because of ==>", e)
        return False

def main():
    number1 = ask_first_input()
    number2 = ask_second_input()
    result  = perform_division(number1, number2)
    print(f"The result from dividing {number1} by {number2} is {result}")
main()

## LS Solution ##
# try:
#     num1 = float(input('Enter the first number: '))
#     num2 = float(input('Enter the second number: '))
#     result = num1 / num2
#     print(f'The result is: {result}')
# except ZeroDivisionError:
#     print('Cannot divide by zero!')
# except ValueError:
#     print('Please enter valid numbers!')