'''
Register.
Create a function named register that takes exactly three arguments:
username as positional-only, password as keyword-only,
and age as either a positional or keyword argument.

'''

# Solution

def register(username, *, password, age):
    print(username, password, age)

register('Max2020', password = '******', age = 24) # Max2020 ****** 24
register(username= 'Max2020', password = '******', age = 24 ) # Max2020 ****** 24

register(username= 'Max2020', age = 24 , password = '******',) # Max2020 ****** 24

# register(age = 24 , password = '******', 'Max2020') # SyntaxError

## LS Solution ##
# def register(username, /, age=None, *, password):
#     return {'username': username, 'password': password, 'age': age}

# print(register('user1', 30, password='pass123'))
# # {'username': 'user1', 'password': 'pass123', 'age': 30}

# print(register('user2', age=45, password='pass132'))
# # {'username': 'user2', 'password': 'pass132', 'age': 45}

# print(register('user3', password='pass321'))
# # {'username': 'user3', 'password': 'pass321', 'age': None}
