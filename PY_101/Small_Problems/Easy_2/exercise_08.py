# Odd Lists
# Write a function that returns a list that contains every other element of a list
# that is passed in as an argument. The values in the returned list should be 
# those values that are in the 1st, 3rd, 5th, and so on elements of the argument list.
# Bonus question Try to solve the problem using list slicing.
# Further Exploration
# Write a companion function that returns the 2nd, 4th, 6th, and so on elements of a list.
# Try to solve this differently from the exercise described above.

# Solution

def oddities(list_literal):
    new_list = []
    index = 0

    while index < len(list_literal):
        new_list.append(list_literal[index])
        index += 2

    return new_list

# bonus question

def oddities_new(list_input):
    return list_input[::2]

# Further exploration

def evenities(list_entry):
    if len(list_entry) < 2:
        return list_entry

    new_list = []
    index = 1

    while index < len(list_entry):
        new_list.append(list_entry[index])
        index += 2

    return new_list

def companion(list1):
    return list1[1::2] if len(list1) > 1 else list1



print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])               # True
print(oddities([1, 2, 3, 4]) == [1, 3])                     # True
print(oddities(["abc", "def"]) == ['abc'])                  # True
print(oddities([123]) == [123])                             # True
print(oddities([]) == [])                                   # True

print(oddities_new([2, 3, 4, 5, 6]) == [2, 4, 6])           # True
print(oddities_new([1, 2, 3, 4]) == [1, 3])                 # True
print(oddities_new(["abc", "def"]) == ['abc'])              # True
print(oddities_new([123]) == [123])                         # True
print(oddities_new([]) == [])                               # True


print(evenities([2, 3, 4, 5, 6, 7, 8, 9]) == [3, 5, 7, 9])  # True
print(evenities([1, 2, 3, 4]) == [2, 4])                    # True
print(evenities(["abc", "def"]) == ['def'])                 # True
print(evenities([123]) == [123])                            # True
print(evenities([]) == [])                                  # True

print(companion([2, 3, 4, 5, 6, 7, 8, 9]) == [3, 5, 7, 9])  # True
print(companion([1, 2, 3, 4]) == [2, 4])                    # True
print(companion(["abc", "def"]) == ['def'])                 # True
print(companion([123]) == [123])                            # True
print(companion([]) == [])                                  # True
