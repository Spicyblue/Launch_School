# Exclusive Or
# The or operator returns
# a truthy value if either or both of its operands are truthy, 
# a falsy value if both operands are falsy.
# The and operator returns
# a truthy value if both of its operands are truthy, 
# a falsy value if either operand is falsy. 
# This works great until you need only one of two conditions to be truthy, 
# the so-called exclusive or, also known as xor (pronounced "ECKS-or").
# In this exercise, you will write an xor function that takes two arguments, 
# and returns True if exactly one of its arguments is truthy, False otherwise.
# Further Exploration
# Can you think of a situation in which a boolean xor function would be useful? 
# Suppose you were modeling a light at the top of a flight of stairs wired in such a way that 
# the light can be turned on or off using either the switch at the bottom of the stairs or
# the switch at the top of the stairs. Think of some additional examples.

# or and and are so-called short circuit operators in that the 
# second operand is not evaluated if its value is not needed. 
# Does the xor function perform short-circuit evaluation of its operands? Why or why not? 
# Does short-circuit evaluation in xor operations even make sense?

# Solution

def xor(arg1, arg2):
    if (arg1 and not arg2) or (arg2 and not arg1):
        return True

    return False

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)
print(xor(False, False) == False)

# Further exploration
# Short-circuit evaluation is a feature of the and and or operators 
# where the second operand is not evaluated if the first operand 
# is sufficient to determine the result.
# In the xor function,
# The expression (value1 and not value2) or (value2 and not value1) involves both and and or operators.
# Short-circuit behavior can occur within the evaluation of these sub-expressions:
# (value1 and not value2): If value1 is False, not value2 is not evaluated because the result of the and operation will be False.
# (value2 and not value1): If value2 is False, not value1 is not evaluated because the result of the and operation will be False.
# The or operator will short-circuit if the first expression (value1 and not value2) is True, meaning (value2 and not value1) will not be evaluated.
# Thus, while individual and and or operations within the function can short-circuit, 
# the overall XOR logic does not directly short-circuit in a single step 
# because both conditions must be evaluated to determine if exactly one operand is True.
# Short-circuit evaluation in the context of XOR does not entirely make sense because:
# XOR requires both operands to be evaluated to determine if they are different.
# You need to know the values of both operands to ascertain if exactly one is True and the other is False.
