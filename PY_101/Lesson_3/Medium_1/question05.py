# What do you think the following code will output?

nan_value = float("nan")

print(nan_value == float("nan"))

# Returns false because nan values are not equall. 
# nan -- not a number -- is a special numeric value that indicates that an operation 
# that was intended to return a number failed. 
# Python doesn't let you use == to determine whether a value is nan.

# How can you reliably test if a value is nan?
# Yes, using two different ways 
# solution 1
nan_value = float("nan")
print(nan_value != float("nan"))

# solution 2 which is more ideal
import math

nan_value = float("nan")
print(math.isnan(nan_value))
