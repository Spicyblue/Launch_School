'''
Ignore Middle.
Unpack values from a tuple of four elements,
but only keep the first and last values.
'''

# Solution
data = (100, 200, 300, 400)
first, *_, last = data

print(first, last)

## LS Solution ##
# data = (100, 200, 300, 400)
# first, *_ , last = data
