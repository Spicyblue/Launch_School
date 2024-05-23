# One day, Spot was playing with the Munster family's home computer,
# and he wrote a small program to mess with their demographic data:

munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"

# After writing this function, he typed the following code:

mess_with_demographics(munsters)

# Before Grandpa could stop him, Spot hit the Enter key with his tail. Did the family's data get ransacked? Why or why not?


# myanswer 
# Dictionary are mutable data type and using the right key, its values can be mutated. 
# When a dictionary is passed as an argument to a function, a reference to the dictionary is passed, not a copy.
# The key used in the mess_with demograhic function corresponds to the keys in the munster dictionary.
# the values corresponds to the nested dictionaries e.g {"age": 32, "gender": "male"}.
# hence passing a value['age'] and value['gender'] accesses the key in the nested dictionary and mutates their values
# adding +42 for age and reassingning 'others for gender.
# Hence when the function is called and the dictionary is passed as an argument, the changes are effected and the 
# nested dictionary values are reassigned. 


# ls answer
# In Python, dictionaries are mutable, and when passed to a function, 
# a reference to the dictionary is passed, not a copy. 
# Thus, Spot's demo_dict starts off pointing to the munsters object. 
# As a result, the changes made within the function directly affect the munsters dictionary.
# The key aspect here is that the nested dictionaries (the individual family members' data) 
# are the ones being mutated. Each family member's dictionary ({"age": x, "gender": y}) is accessed and modified. 
# Since these nested dictionaries are part of the larger munsters dictionary, 
# the changes are reflected in the original data structure.
# His program could replace that with some other object, 
# and the family's data would be safe. 
# However, in this case, the program doesn't reassign demo_dict; 
# it just uses it, as-is. Thus, the object that gets changed by the function is the munsters object.