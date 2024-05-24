# Sum or Product of Consecutive Integers
# Write a program that asks the user to enter an integer greater than 0, 
# then asks whether the user wants to determine the sum or the product of all 
# numbers between 1 and the entered integer, inclusive.
# Further Exploration
# Suppose the input was a list of space separated integers instead of just a single integer? 
# How would your compute_sum and compute_product functions change?

# Solution

import math

def ask_number():
    while True:
        numbers = input("Please enter a valid list of integers greater than zero, separated by spaces: ")
        number_list = numbers.split()  # Split on any whitespace and remove extra spaces
        number_valid = [int(number) for number in number_list if number.isnumeric() and int(number) > 0]

        if len(number_valid) == len(number_list): # Invalid integers will result in shorter lengths.
            return number_valid
        else:
            print("Invalid list of integers.")


def ask_sum_or_product():
    answer = input('Please enter "s" to compute the sum or "p" to compute the product: ').strip().lower()

    while answer not in ['p', 's']:
        answer = input('Invalid input. Please enter "s" to compute the sum or "p" to compute the product: ').strip().lower()

    return answer

def calculate_result(value, operation):
    if operation == 's':
        for digits in value:
            total_sum = sum(range(1, digits + 1))
            print(f"The sum of integers between 1 and {digits} is {total_sum}")

    if operation == 'p':
        for digits in value:
            total_product = math.prod(range(1, digits + 1))
            print(f"The product of integers between 1 and {digits} is {total_product}")

def main():
    number_input = ask_number()
    operation_input = ask_sum_or_product()
    calculate_result(number_input, operation_input)

main()