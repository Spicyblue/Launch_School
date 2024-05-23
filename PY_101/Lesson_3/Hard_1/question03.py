# Given the following similar sets of code, what will each code snippet print?
# Code A
def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# Answer
# print one is ["one"]
# print two is ["two"]
# print three is ["three"]
# The variables inside the mess_with_var function are local to the function and are different from the global varaibles
# Although we have new assignment withing the function i.e One = ["two"], two = ["three"] and there = ["one"] based on the arguments passed.
# However, these variables local to the function and do not mutate the global variable!
# Hence even after the fuction call, the global variables still point to the same object.


# Code B
def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# Answer
# print one is ["one"]
# print two is ["two"]
# print three is ["three"]
# Here, we initialized three varaibles and assign them list objects,  one = ["two"], two = ["three"], three = ["one"].
# However, we do not use the parameters of the function within the function.
# Also, because we have no return startment, the variables initialized will remain local to the function.
# Hence, even after calling the function, the global variables remain the same.


# Code C
def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# Answer
# Now this one is a bit tricky. 
# print one is ["two"]
# print two is ["three"]
# print three is ["one"]
# Within the function mess_with var, the index position of the parameters being referenced is accessed and the elements in that position is mutated.
# Hence, mutation within this index position is reflected in the origianl object as both point to the same object in memory.
# Hence, we we call the function and pass the object reference (variable) as arguments, the resulting mutation is reflected in
# the original object because list are mutable

# LS Answer
# In all three scenarios, the variables one, two, and three inside the mess_with_vars function are local to the function. 
# They are not the same as the variables one, two, and three defined outside the function. 
# This is known as variable shadowing, 
# where the local variables inside the function overshadow the variables outside the function with the same names.

# A
# The output is:
# one is: ['one']
# two is: ['two']
# three is: ['three']
# Since variables one, two, and three in the mess_with_vars function are local, reassigning them does not affect the original lists.

# B
# The output is:
# one is: ['one']
# two is: ['two']
# three is: ['three']
# Again, the local variables in the mess_with_vars function are being reassigned, but this doesn't change the original lists. 

# C
# The output is:
# one is: ['two']
# two is: ['three']
# three is: ['one']
# In this case, the mess_with_vars function modifies the content of the lists directly. 
# Since lists in Python are mutable and passed by reference, the changes are reflected outside the function.
