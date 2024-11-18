# Consider these two simple functions:

def foo(param="no"):
    return "yes"

def bar(param="no"):
    return param == "no" and foo() or "no"

# What will the following function invocation return?

bar(foo())
# returns "yes" == "no" and "yes" or "no"
# return False and True or True
# return False or True
# return True == "no"

# LS answer
# When bar(foo()) is called, the foo function is executed first, returning "yes". 
# This return value ("yes") is then passed as the argument to the bar function. 
# In bar, the parameter param is now "yes". The expression param == "no" and foo() or "no" is evaluated as follows:
# param == "no" evaluates to False since param is "yes".
# Due to the and operator, foo() is not executed because the first part of the and expression is already False.
# Since the left side of the or (the result of the and expression) is False, 
# Python evaluates and returns the right side of the or, which is "no".
# Therefore, bar(foo()) ultimately returns "no".
# This is because the value returned from the foo function will always be "yes" , 
# and "yes" == "no" will be False.