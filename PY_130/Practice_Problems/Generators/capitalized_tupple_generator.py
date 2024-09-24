'''
Capitalized Tuple generator.
Use a generator expression to capitalize every string in a list of strings. 
Use a single print invocation to print all the capitalized strings as a tuple.
'''

# Solution 
string = ['africa', 'america', 'europe', 'asia']

capitalized_tupple = tuple((letter.capitalize() for letter in string))

print(capitalized_tupple)

# LS Solution
# strings = ['four', 'score', 'and', 'seven', 'years', 'ago']
# capitalized = (string.capitalize() for string in strings)
# print(tuple(capitalized))
# # ('Four', 'Score', 'And', 'Seven', 'Years', 'Ago')