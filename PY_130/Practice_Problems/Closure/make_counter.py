'''
Make greeting.
What does the following program print?
Try to answer without running the code:
'''

def make_counter():
    def counter_func():
        counter = 0
        counter += 1
        return counter

    return counter_func

increment_counter = make_counter()
print(increment_counter())
print(increment_counter())

increment_counter = make_counter()
print(increment_counter())
print(increment_counter())

# Solution
# The code will print 
# 1
# 1
# 1
# 1

## LS Answer ##
#The code will print:
# 1
# 1
# 1
# 1

# All four print calls print 1.
# Since counter is initialized inside the function returned by make_counter,
# closure plays no part in its execution.
# Instead, counter gets initialized to 0 each time we call incrementCounter.

