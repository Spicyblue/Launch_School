'''
List Deduplication.
A developer is trying to remove duplicates from a list.
They use a set for deduplication, but the order of elements is lost.
How can we preserve the order?
'''

# # Current code
# data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
# unique_data = list(set(data))
# print(unique_data == [4, 2, 1, 3]) # order not guaranteed

'''
Issue with the current code:
The current code passes the list referenced by `data` to the
set function which return a set of unique objects but are unordered.

To solve this, we can use a iterater through the data
and only add element not present in `unique_data`. 
This will keep the order.
'''

# fixed code
data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = []

for num in data:
    if num not in unique_data:
        unique_data.append(num)

print(unique_data == [4, 2, 1, 3]) # order not guaranteed

# Note!
# Time take to debug code is  mins, 3 mins 23 seconds.
# Took more time to because I wanted to keep the same structure.

## LS Answer ##
# data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
# unique_data = []
# seen = set()

# for item in data:
#     if item not in seen:
#         seen.add(item)
#         unique_data.append(item)

# print(unique_data == [4, 2, 1, 3]) # True
