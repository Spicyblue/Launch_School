# Strings Strings
# Write a function that takes one argument, a positive integer, 
# and returns a string of alternating '1's and '0's, always starting with a '1'. 
# The length of the string should match the given integer.

# Solution

def stringy(number):
    if not number or number < 0:
        return "Invalid Input"
    
    results = ""
    for index in range(number):
        if index % 2 == 0:
            results += "1"
        else:
            results += "0"

    return results

print(stringy(6)  == "101010")           # True
print(stringy(9)  == "101010101")        # True
print(stringy(4)  == "1010")             # True
print(stringy(7)  == "1010101")          # True
print(stringy(1)  == "1")                # True
print(stringy(0)  == "Invalid Input")    # True
print(stringy(-7) == "Invalid Input")    # True