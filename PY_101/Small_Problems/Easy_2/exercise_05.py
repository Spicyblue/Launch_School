# Floating Point Arithmetic
# Write a program that prompts the user for two positive numbers (floating-point), 
# then prints the results of the following operations on those two numbers: 
# addition, subtraction, product, quotient, floor quotient, remainder, and power. Do not worry about validating the input.

# Solution

CALCULATIONS = ['+', '-', '*', '/', '//', '%', '**']

def prompt(message):
    print(f"==> {message}")

def ask_first_number():
    number_1 = float(input("==> Enter the first number: "))

    return number_1

def ask_second_number():
    number_2 = float(input("==> Enter the second number: "))

    return number_2

def math(numb1, numb2, calc_type):
    match calc_type:
        case '+':  return numb1 + numb2
        case '-':  return numb1 - numb2
        case '*':  return numb1 * numb2
        case '/':  return numb1 / numb2
        case '//': return numb1 // numb2
        case '%':  return numb1 % numb2
        case '**': return numb1 ** numb2

def calculate (num1, num2):
    for signs in CALCULATIONS:
        calculate = (f"{num1} {signs} {num2}")
        result = math(num1, num2, signs)
        prompt(f"{calculate} = {result}")

def main():
    number1 = ask_first_number()
    number2 = ask_second_number()
    calculate(number1, number2)

main()