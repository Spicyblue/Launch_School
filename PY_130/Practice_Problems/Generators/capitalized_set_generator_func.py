'''
Capitalized Set Generator Function.
Create a generator function that generates the capitalized version of every
string in a list of strings whose length is less than 5.
Use a single print invocation to print all the capitalized strings as a set.

'''

# Solution 
def capitalizing_set(lst):

    for word in lst:
        if len(word) >= 5:
            yield word.capitalize()

string = ['africa', 'america', 'europe', 'asia', 'antartica']
capitalized_set = set(capitalizing_set(string))
print(capitalized_set)
