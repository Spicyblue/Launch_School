'''
Set Modifications.
We want to remove certain items from a set while iterating over it,
but the code below throws an error. Why is that and how can we fix it?
'''

# # Current code
# data_set = {1, 2, 3, 4, 5}

# for item in data_set:
#     if item % 2 == 0:
#         data_set.remove(item)

'''
Issue with the current code:
The current code throws an error because the size of the set changes during iteration. 
Iterating and mutating over an iterable at the same time isnt considered a good practice.

To solve this, we can use the create a list of the original set.
and then modify the origanl set during the iteration.
'''

# fixed code 
data_set = {1, 2, 3, 4, 5}

for item in list(data_set):  
    if item % 2 == 0:
        data_set.remove(item) 

print(data_set) 

# Note!
# Time take to debug code is  mins, 5 mins 23 seconds.
# Took more time to because I wanted to keep the same structure.

## LS Answer ##
# data_set = {item for item in data_set if item % 2 != 0}