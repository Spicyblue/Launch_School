'''
Capitalized set generator.
Use a generator expression to capitalize the strings in a 
list of strings whose length is at least 5.
Use a single print invocation to print all the capitalized strings as a set.
'''

# Solution 
string = ['africa', 'america', 'europe', 'asia', 'antartica',]

capitalized_set = set((word.capitalize() for word in string if len(word) >= 5))

print(capitalized_set)
