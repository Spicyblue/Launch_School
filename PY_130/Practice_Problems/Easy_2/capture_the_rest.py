'''
Capture all the rest.
Unpack the first two elements from a list and s
tore the remaining elements in another list.
'''

# Solution
numbers = [1, 2, 3, 4, 5, 6]

fst_ele, sec_ele, *rest = numbers
print(fst_ele, sec_ele)
print(rest)

## LS Solution ##
# numbers = [1, 2, 3, 4, 5, 6]
# a, b, *rest = numbers