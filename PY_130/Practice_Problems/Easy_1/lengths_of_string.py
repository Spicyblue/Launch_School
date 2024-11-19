'''
Lengths of Strings.
Use map to create a list of lengths of each string in the original list.
'''

# Solution
lst = ['The', 'result', 'should', 'show', 
       'the', 'length', 'of', 'each', 'string']
lst_string_len = list(map(lambda string: len(string), lst))
print(lst_string_len)

## LS Solution ##
# lengths = list(map(len, ["apple", "banana", "cherry"]))

