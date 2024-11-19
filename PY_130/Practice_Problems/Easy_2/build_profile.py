'''
Build Profile.
Write a function build_profile that takes a 
first name and a last name, and any number of keyword arguments
to add to a user's profile.
'''

# Solution

def build_profile(firstname, lastname, **kwarg):
       return{'first_name': firstname, 
       'last_name': lastname}|kwarg

print(build_profile("Max", "Hawkins", location="San Francisco", field="Software Engineering"))
# {{'first_name': 'Max', 'last_name': 'Hawkins', 'location': 'San Francisco', 'field': 'Software Engineering'}}

## LS Solution ##
# def build_profile(first_name, last_name, **user_info):
#     profile = {"first_name": first_name, "last_name": last_name}
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile

# print(build_profile("Max", "Hawkins", location="San Francisco", field="Software Engineering"))
# {{'first_name': 'Max', 'last_name': 'Hawkins', 'location': 'San Francisco', 'field': 'Software Engineering'}}
