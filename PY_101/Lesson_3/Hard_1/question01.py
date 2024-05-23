# Will the following functions return the same results?

def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())

# Try to answer without running the code or looking at the solution.

# Answer:
# The ideally should return a dictionary with key, value pair however, in the function second(),
# the dictionary is not indented in line with the return keyword. Hence, it will not be accessed and not be returned.
# the return keyword will return None is nothing is returned.

# LS answer
# These functions do not return the same thing. The function first() returns the expected value of { prop1: "hi there" }, 
# but second() returns None without throwing any errors.
# In Python, if there's nothing after a return statement, the function will return None. 
# The indented block after the return statement in second function is unreachable and doesn't affect the return value.

