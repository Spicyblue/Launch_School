'''
Remove None Values.
Remove all None values from a list using the filter method.
'''

# Solution
lst = ['The', 'result', 'should', 'not', 'include', None, 'None']
lst_string = list(filter (lambda string: string != None, lst))
print(lst_string)

## LS Solution ##
# no_none = list(filter(None, [1, None, 2, None, 3]))

