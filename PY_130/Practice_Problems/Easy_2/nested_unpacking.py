'''
Nested Unpacking.
Given a nested tuple data = ((1, 2), (3, 4), (5, 6)),
write a code to unpack this tuple
into individual variables a, b, c, d, e, f.
'''

# Solution
data = ((1, 2), (3, 4), (5, 6))
(one, two), (three, four),(five, six) = data

print(one , two, three, four, five, six)

## LS Solution ##
# data = ((1, 2), (3, 4), (5, 6))
# (a, b), (c, d), (e, f) = data

