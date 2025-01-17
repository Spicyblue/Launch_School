# Always Return Negative
# Write a function that takes a number as an argument. 
# If the argument is a positive number, return the negative of that number. 
# If the argument is a negative number, return it as-is.

def negative(number):
    return number if number < 0 else -number

print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True
