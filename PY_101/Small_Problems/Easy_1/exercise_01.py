# Isn't it Odd?
# Write a function that takes one integer argument and returns True when the number's absolute value is odd, 
# False otherwise.

# Solution

def is_odd(number):
    return abs(number) % 2 == 1

print(is_odd(30))
print(is_odd(-52))
print(is_odd(-140))
print(is_odd(33))
print(is_odd(101))
