'''
Reverse String.
Use a generator expression to yield each character of a string in reverse order.
'''

# Solution

def rewind_string(string_input):
    for idx in range(len(string_input) -1, -1, -1):
        yield string_input[idx]

wierd_string = "sdrawkcab daer si gnirts sihT"
generator_unwierd_string = (rewind_string(wierd_string))

for char in generator_unwierd_string:
    print(char)

def rewind_string2(string_input):
    yield string_input[::-1]

wierd_string = "sdrawkcab daer si gnirts sihT"
generator_unwierd_string = (rewind_string2(wierd_string))

for char in generator_unwierd_string:
    print(char)

## LS Solution ##
# string = "Hello"
# reverse_generator = (string[i] for i in range(len(string) - 1, -1, -1))
# for char in reverse_generator:
#     print(char)
