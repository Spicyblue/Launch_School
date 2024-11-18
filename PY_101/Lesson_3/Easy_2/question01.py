# Write two distinct ways of reversing the list without mutating the original list.

numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

# using indexing 
print (numbers[::-1])

# using range to iterate through the numbers
reversed_number = []
for i in range(len(numbers) - 1, -1, -1):
    reversed_number.append(numbers[i])

print(reversed_number)

# method hunthing using reversed method
print(list(reversed(numbers))) 

# method hunting using the list.sort method
# This method sorts the list in place, using only < comparisons between items.
# reverse is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.
# This method operates by side effect, it does not return the sorted sequence.
numbers.sort(key = int, reverse = True)
print(numbers)

# method hunting using sorted method
# Return a new sorted list from the items in iterable.
# new sorted list is a different object in memory.
sorted_number = sorted(numbers, reverse= True)
print(sorted_number)
