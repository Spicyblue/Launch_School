# We have most of the Munster family in our ages dictionary:

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}

# Add entries for Marilyn and Spot to the dictionary:
additional_ages = {'Marilyn': 22, 'Spot': 237}

# method hunting
# Update the dictionary with the key/value pairs from other, overwriting existing keys. Return None.
# update() accepts either another dictionary object or an iterable of key/value pairs 
# (as tuples or other iterables of length two). 
# If keyword arguments are specified, the dictionary is then updated with those key/value pairs: d.update(red=1, blue=2).
# ages.update(additional_ages)
#print(ages)

# using a function to update an existing dictionary
def update_dictionary(dict_entry, new_dict_to_add):
    change = dict_entry.update(new_dict_to_add)
    return change

new_ages = update_dictionary(ages,additional_ages)
print(new_ages)
