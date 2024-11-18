# Starting with the string:

famous_words = "seven years ago..."

# Show two different ways to create a new string with "Four score and " prepended to the front of the string.
# method 1

new_string = "Four score and " + famous_words
print(new_string)

# method 2 using string interpolation
starting = "Four score and "
new_string_also = f'{starting}{famous_words}'
print(new_string_also)
