'''
Print Message.
Create a function named print_message that requires a keyword-only argument (message)
and an optional keyword-only argument (level) with a default value of "INFO".
The function should print out the message prefixed with the level.
The function shouldn't accept any positional arguments.
'''

# Solution

def print_message(*, message, level = 'INFO'):
    print(f"{level} : {message}")

print_message(message = 'This is not a drill', level = "WARNING") # Max2020 ****** 24
print_message(message= 'Welcome to the Google' ) # Max2020 ****** 24

print_message("'Why doesn't this word") # raise a TypeError

# register(age = 24 , password = '******', 'Max2020') # SyntaxError

## LS Solution ##
# def print_message(*, message, level="INFO"):
#     print(f"[{level}] {message}")

# print_message(message="This is a test message.", level="WARNING")
# # [WARNING] This is a test message.

# print_message(message="This is an informational message.")
# # [INFO] This is an informational message.