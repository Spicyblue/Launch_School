'''
Available at https://www.codewars.com/kata/583f158ea20cfcbeb400000a/python  
Level = 7kyu

Arithmetic.
Given two numbers and an arithmetic operator (the name of it, as a string),
return the result of the two numbers having that operator used on them.
a and b will both be positive integers, and a will always be the first number in the operation, and b always the second.
The four operators are "add", "subtract", "divide", "multiply".
A few examples:(Input1, Input2, Input3 --> Output)

5, 2, "add"      --> 7
5, 2, "subtract" --> 3
5, 2, "multiply" --> 10
5, 2, "divide"   --> 2.5
Try to do it without using if statements!

# Problem:
Input:
- integer, string
Output:
- Integer

    Rules:
        Exp:
        - a and b will both be positive integers, and a will always be the first number in the operation, and b always the second.
        
# Example
print(arithmetic(1, 2, "add") == 3)
print(arithmetic(8, 2, "subtract") == 6)
print(arithmetic(5, 2, "multiply") == 10)
print(arithmetic(8, 2, "divide") == 4)

# Data Structure:
None

# Alg:
    High End:
    1. Check what arithmetic calculation is involved.
    2. Return the Value after calculation

        Low end:
        1. Get input.
        2. Use a match case and return the corresponnding calculation

# Code  
'''

# Solution
def arithmetic(input1, input2, operation):
    match operation:
        case 'add':
            return input1 + input2
        case 'subtract':
            return input1 - input2
        case 'multiply':
            return input1 * input2
        case 'divide':
            return input1 / input2

# Code Check
print(arithmetic(1, 2, "add") == 3)
print(arithmetic(8, 2, "subtract") == 6)
print(arithmetic(5, 2, "multiply") == 10)
print(arithmetic(8, 2, "divide") == 4)

# Note!
# Time take to write PEDAC and test/debug code 6 mins 53 seconds