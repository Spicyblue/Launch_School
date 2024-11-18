'''
Generator with User Input
Create a generator function that yields user
input strings until the word "stop" is entered.
'''

# Solution

def get_user_input():
    message = """
Please enter a word
Note ==> To end, enter 'stop'
Enter your word: 
"""
    while True:
        entry = input(message).strip().lower()
        if entry == 'stop':
            break
        else:
            yield str(entry)

for word in get_user_input():
    print()
    print(f"You entered {word}")

## LS Solution ##
# def input_generator():
#     while True:
#         s = input("Enter a string: ")
#         if s == "stop":
#             break
#         yield s

# for user_input in input_generator():
#     print(user_input)