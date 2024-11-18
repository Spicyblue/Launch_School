'''
Capitalized Tuple Generator Function.
Create a generator function that generates the capitalized version of 
every string in a list of strings. 
Use a single print invocation to print all the capitalized strings as a tuple.
'''

# Solution 
def capitalizing_tupple(lst):

    for word in lst:
        yield word.capitalize()

string = ['africa', 'america', 'europe', 'asia', 'antartica']
capitalized_tupple = tuple(capitalizing_tupple(string))
print(capitalized_tupple)

