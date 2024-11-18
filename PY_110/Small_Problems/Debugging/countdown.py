'''
Countdown.
Our countdown to launch isn't behaving as expected.
Why? Change the code so that our program successfully counts down from 10 to 1 before launching.
'''

# # Current code
# def decrease(counter):
#     return counter - 1

# counter = 10

# for _ in range(10):
#     print(counter)
#     decrease(counter)

# print('LAUNCH!')

'''
Issue with the current code:

Passing counter as argument to the function `decrease` return a new integer object.
However, since integers are immutable, this does not reassign the global variable `counter`
and thus counter will alway be 10. 
To fix the code, the return value of the function call of `decrease` 
should be used to reassigned `counter`.
'''

# fixed code 
def decrease(counter):
    return counter - 1

counter = 10

for _ in range(10):
    print(counter)
    counter = decrease(counter)

print('LAUNCH!')


# Note!
# Time take to debug code is 0 mins, 15 seconds.
# Took more time to write the reason for the error but didnt include it.

## LS Answer ##
# def decrease(counter):
#     return counter - 1

# counter = 10

# for _ in range(10):
#     print(counter)
#     counter = decrease(counter)

# print('LAUNCH!')