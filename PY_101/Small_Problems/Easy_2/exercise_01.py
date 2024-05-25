# Welcome Stranger
# Create a function that takes 2 arguments, a list and a dictionary. 
# The list will contain 2 or more elements that, when joined with spaces, will produce a person's name. 
# The dictionary will contain two keys, "title" and "occupation", and the appropriate values. 
# Your function should return a greeting that uses the person's full name, and mentions the person's title.

# Solution

def greetings(list_obj, dict_obj):
    if len(list_obj) < 2:
        print("List Element must be atleast 2")
        return False

    new_list = " ".join(list_obj)
    title, occupation = dict_obj['title'], dict_obj['occupation']

    return (f'Hello {new_list}! Nice to have a {title} {occupation} around.')

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)

new_greeting = greetings(
    ["James", "Bond"], 
    {"title": "Senior", "occupation": "Programmer"},
)   
print(greeting)
print(new_greeting)