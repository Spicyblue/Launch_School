# Write two different ways to remove all of the elements from the following list:
numbers = [1, 2, 3, 4]

# using the index slicing and del method.
del numbers[:]

# method hunting using the clear method.
numbers.clear()

# wusing a while loop
while numbers:
    numbers.pop()

print(numbers)
