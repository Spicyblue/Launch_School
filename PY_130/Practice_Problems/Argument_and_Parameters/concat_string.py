'''
Concat Strings.
Define a function named concat_strings that takes any number of strings and
returns the concatenation of all the strings.
Add a keyword-only argument sep with a default value of ' '
that specifies the separator to use between the strings.
'''

# Solution

def concat_strings(*args, sep = ' '):
    return sep.join([string for string in args])

print(concat_strings('This', 'is', 'how', 'to', 'use', 'kwargs')) # This is how to use kwargs
print(concat_strings('This', 'is', 'how', 'to', 'use', 'kwargs', 
                     'using', 'a', 'keyword', 'only', 'argument', 
                     sep = '/')) # This/is/how/to/use/kwargs/using/a/keyword/only/argument

## LS Solution ##
# def concat_strings(*args, sep=' '):
#     return sep.join(args)

# print(concat_strings("Hello", "world!"))              # Hello world!
# print(concat_strings("one", "two", "three", sep='+')) # one+two+three