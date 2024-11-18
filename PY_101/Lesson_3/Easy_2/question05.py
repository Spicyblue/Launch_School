# How would you verify whether the data structures assigned 
# to the variables numbers and table are of type list?

numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

# use the type method
print(type(numbers) is list)
print(type(table) is list)

# use the isintance list
# The isinstance() function returns True if the specified object is of the specified type, otherwise False.
print(isinstance(numbers, list))  # True
print(isinstance(table, list))   # False
