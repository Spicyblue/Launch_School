# What does the last line in the following code output?

dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)
print(dictionary)

# Try to answer without running the code or looking at the solution.

# print dictionary will output {'first': [1, 2] }.
# Since num_list references the original list in dictionary, appending ot mutating num_list will update the original dictionary list.

# LS answer
# [1, 2]
# {'first': [1, 2]}
# Since num_list is a reference to the original list in dictionary, appending to num_list modifies the list. 
# Thus, the original dictionary is also updated.