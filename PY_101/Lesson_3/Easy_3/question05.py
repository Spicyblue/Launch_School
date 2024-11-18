# The following function unnecessarily uses two return statements to return boolean values. 
# Can you rewrite this function so it only has one return statement and does not explicitly 
# use either True or False?

# def is_color_valid(color):
#     if color == "blue" or color == "green":
#         return True
#     else:
#         return False

# solution 1   
MAIN_COLOR = ['blue', 'green']

def is_color_valid(color):
    return color in MAIN_COLOR

print(is_color_valid('blue'))
print(is_color_valid('green'))
print(is_color_valid('black'))

#solution 2
def is_color_valid_also(color):
    return color == 'blue' or color == 'green'

print(is_color_valid_also('blue'))
print(is_color_valid_also('green'))
print(is_color_valid_also('black'))

# In functions that return a boolean value, you often don't need separate return statements for the True and False cases. 
# Instead, you can return the value of a conditional expression directly.