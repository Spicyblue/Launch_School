'''
Stack Machine Interpretation.
This problem takes a while to describe, which also gives a feeling of great complexity.
The solution, however, is surprising in its overall lack of complexity.
While it will may take a while for you to come up with an appropriate mental model,
and may also take considerably longer than other exercises in this section, go ahead and give it a try anyway.

A stack is a list of values that grows and shrinks dynamically.
A stack may be implemented as a list that uses two list methods: list.append and list.pop.
In most languages, we would use a list.push method instead of list.append,
but Python uses list.append instead.
Thus, we can talk of pushing things to the stack (adding them to the top of the stack)
and popping them from the stack (removing the topmost stack item).

A stack-and-register programming language is a language that uses a stack instead of variables
for all of its data. Each operation in the language operates on a register,
which can be thought of as the current value.
The register is not part of the stack.

An operation that requires two values pops the topmost item from the stack
(i.e., the operation removes the most recently pushed value from the stack),
operates on the popped value and the register value,
then stores the result back in the register.

This sounds complex, but the behavior is straightforward to walk through manually.
Consider a MULT operation in a stack-and-register language.
It pops the topmost value from the stack,
multiplies the popped value with the current value in the register,
then replaces the register content with the result value.
For example, suppose we start with a stack of [3, 6, 4] (where 4 is the topmost item in the stack) and a register value of 7,
the MULT operation mutates the stack to [3, 6] (the 4 is popped),
and the result of the multiplication, 28, is left in the register.
If we do another MULT at this point, the stack is mutated to [3],
and the register is left with the value 168.

Write a function that implements a miniature stack-and-register-based programming language
that has the following commands (also called operations or tokens):

n: Place an integer value, n, in the register. Do not modify the stack.
PUSH : Push the current register value onto the stack. Leave the value in the register.
ADD : Pop a value from the stack and add it to the register value, storing the result in the register.
SUB : Pop a value from the stack and subtract it from the register value, storing the result in the register.
MULT : Pop a value from the stack and multiply it by the register value, storing the result in the register.
DIV : Pop a value from the stack and divide the register value by the popped stack value, storing the integer result back in the register.
REMAINDER : Pop a value from the stack and divide the register value by the popped stack value, storing the integer remainder of the division back in the register.
POP : Remove the topmost item from the stack and place it in the register.
PRINT : Print the register value.
All operations are integer operations (which is only important with DIV and REMAINDER).

Programs will be supplied to your language function via a string argument.
Your function may assume that all arguments are valid programs -- i.e.,
they will not do anything like trying to pop a non-existent value from the stack,
and they won't contain any unknown tokens.

Initialize the stack and register to the values [] and 0, respectively.

# Problem:
- Input:
String
- Output:
Integers

- Rules
    Explicit:
    Arguments will all be valid.
    The argument will process in a logical order.


# Examples:

minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed)

# Data structure
list

# Algorithm
    - High End 
        1. Get input.
        2. Initialize stack and register.
        3. Establish what each operation keyword does.
        4. Split input into list.
        5. Iterate through the list.
            - Based on the item in the list.
            - Check if item is valid for an operation.
            - Perform the required operation.
            - Repeat for all items in the list.
    
# Code
'''

# Solution
def get_opetation(string_input):

    try:
        string_input = int(string_input)
        return string_input
    
    except ValueError:
        return string_input

def minilang(string):
    
    register = 0
    stack = []
    order_of_operation = string.split(' ')

    for operation in order_of_operation:
        valid_operation = get_opetation(operation)

        match valid_operation:
            case "ADD":
                register += stack.pop()
            case "DIV":
                register //= stack.pop()
            case "MULT":
                register *= stack.pop()
            case "REMAINDER":
                register %= stack.pop()
            case "SUB":
                register -= stack.pop()
            case "PUSH":
                stack.append(register)
            case "POP":
                register = stack.pop()
            case "PRINT":
                print(register)
            case _:
                register = valid_operation

    return register

#code check
minilang('PRINT')
# 0

minilang('5 PRINT')
# 5

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
#(nothing is printed)

# Was intresting getting to work on the program and debug it. The key was understanding what each operation does 

## LS Answer ##
# def minilang(program):
#     stack = []
#     register = 0

#     for token in program.split():
#         match token:
#             case "ADD":
#                 register += stack.pop()
#             case "DIV":
#                 register //= stack.pop()
#             case "MULT":
#                 register *= stack.pop()
#             case "REMAINDER":
#                 register %= stack.pop()
#             case "SUB":
#                 register -= stack.pop()
#             case "PUSH":
#                 stack.append(register)
#             case "POP":
#                 register = stack.pop()
#             case "PRINT":
#                 print(register)
#             case _:
#                 register = int(token)

#     return register
