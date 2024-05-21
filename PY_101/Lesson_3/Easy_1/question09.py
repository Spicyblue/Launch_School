# Print a new version of the sentence given by advice that ends just before the word house. 
# Don't worry about spaces or punctuation: remove everything starting from the beginning of house to the end of the sentence.

advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as

# method hunting
print(advice.split('house')[0])

# .split method returns a list of strings split at the substring. The substring
# is excluded from all elements of the list, the space is included in the 2nd
# element.

# Method 2. Using a for loop
split_word = advice.split()
print(split_word)

new_advice = []

for word in split_word:
    if 'house' in word:
        break
    new_advice.append(word)

new_advice_string = " ".join(new_advice)
print(new_advice_string)