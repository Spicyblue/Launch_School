'''
Example 3.

Modify your answer to the previous problem so it handles both 
ZeroDivisionError and ValueError with a single exception handler.
The output for both exception types can be obtained from the exception object.

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
# except (ZeroDivisionError, ValueError) as e:
#     print(e)
# else:
#     print(f'The result is: {result}')
# finally:
#     print('End of the program.')
