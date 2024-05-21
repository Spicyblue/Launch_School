# Determine whether the name Dino appears in the strings below -- check each string separately:
str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

# method hunting 1
print('Dino' in str1)
print('Dino' in str2)

# using a for loop to interate over words in the string 
def finding_dino(word_string):
    words = word_string.split()

    for word in words:
        if 'Dino' in word:
            return True

        return False

print(finding_dino(str1))
print(finding_dino(str2))