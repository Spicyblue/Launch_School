'''
Multiply.
Define a function named multiply that accepts two positional-only arguments
and returns their product.
The function should not allow these parameters to be passed as keyword arguments.
'''

# Solution

def multiply(num1, num2, /):
    return num1 *  num2

print(multiply(10, 20)) # outputs 200
print(multiply(num1 = 20, num2 = 30)) # raises an TypeError

## LS Solution ##
# def multiply(a, b, /):
#     return a * b

# print(multiply(4, 5))         # 20
# multiply(a=4, b=5)
# # TypeError: multiply() got some positional-only arguments
# # passed as keyword arguments: 'a, b'