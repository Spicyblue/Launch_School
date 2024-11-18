# Alan wrote the following function, 
# which was intended to return all of the factors of number:

# def factors(number):
#     divisor = number
#     result = []
#     while divisor != 0:
#         if number % divisor == 0:
#             result.append(number // divisor)
#         divisor -= 1
#     return result

# Alyssa noticed that this code would fail when the input is a negative number,
# and asked Alan to change the loop. How can he make this work?
# Note that we're not looking to find the factors for negative numbers,
# but we want to handle it gracefully instead of going into an infinite loop.

# What is the purpose of number % divisor == 0 in that code?

# To solve this, we would have adjust the while condition to be greater than zero.
# Eventually, we end up with a an empty list for negative numbers or zero.
# The purpose of number % divisor == 0 is that it evaluates to True only if the result is an integer.
# Hence, the if block will run and the integer factors get added to the result list.

def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result