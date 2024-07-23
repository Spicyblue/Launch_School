'''
Copy Issues.
We have a list of lists and want to duplicate it.
After making the copy, we modify the original list,
but the copied list also seems to be affected:
What's wrong here? How can you fix it?
'''

# # Current code
# import copy

# original = [[1], [2], [3]]
# copied = copy.copy(original)

# original[0][0] = 99

# print(copied[0] == [1])

'''
Issue with the current code:
The current code has the variable `copied` which is a shallow copy of `original`.
Thus all nested list are referenced.

To solve this, we can make a deepcopy which creates two seperate list that do not reference each other at any level.
'''

# fixed code 
import copy

original = [[1], [2], [3]]
copied = copy.deepcopy(original)

original[0][0] = 99

print(copied[0] == [1])

# Note!
# Time take to debug code is  mins, 50 seconds.

## LS Answer ##
# import copy

# original = [[1], [2], [3]]
# copied = copy.deepcopy(original)

# original[0][0] = 99

# print(copied[0] == [1])  # True


