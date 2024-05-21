# Print the following string with the word important replaced by urgent:

advice = "Few things in life are as important as house training your pet dinosaur."

# using method hunding
print(advice.replace('important', 'urgent'))

# using a forloop
split_advice = advice.split()
new_advice  = []

for word in split_advice:
    if word == 'important':
        new_advice.append('urgent')
    else:
        new_advice.append(word)

new_advice = " ".join(new_advice)

print(new_advice)
    


