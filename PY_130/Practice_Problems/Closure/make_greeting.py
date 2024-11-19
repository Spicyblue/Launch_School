'''
Make greeting.
What will the following code print?
'''

def make_greeting():
    greeting = "Hello"

    def greet_func(name, greet=None):
        if not greet:
            return f"{greeting} {name}!"

        return f"{greet} {name}!"

    return greet_func

greet_person = make_greeting()
print(greet_person("John", "Goodbye"))
print(greet_person("Jane"))

# Solution
# The code will print 
# Goodbye John
# Hello Jane 


## LS Answer ##

#The code will print:
# Goodbye John!
# Hello Jane!
# On line 13, the greet_person variable holds a reference to the greet_func
# function returned by make_greeting(). 
# When called with "John" and "Goodbye", 
# greet_func checks whether the greet argument is truthy. 
# Since "Goodbye" is truthy, it uses this string instead of the closed-over greeting
# variable to return the string "Goodbye John!".

# On line 14, greet_func is called with only one argument, 
# so greet defaults to None, which is falsy. 
# Therefore, the function uses the value of the closed-over greeting variable,
#  "Hello", and returns "Hello Jane!".
