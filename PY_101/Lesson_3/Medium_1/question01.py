#Let's do some "ASCII Art": a stone-age form of nerd artwork f
# rom back in the days before computers had video screens.
# For this practice problem, write a program that outputs The Flintstones Rock! 10 times, 
# with each line prefixed by one more hyphen than the line above it. 
# The output should start out like this:

# -The Flintstones Rock!
# --The Flintstones Rock!
# ---The Flintstones Rock!
#   ...

REPEAT_WORD ='The Flingstones Rock!'

# using a forloop
for adding in range(1, 11):
    print(f'{"-" * adding + REPEAT_WORD}')

# using a while loop
start = 1
end = 11
times = 1

while start < end:
    new_string = ('-' * start)+ REPEAT_WORD
    print(new_string)
    start += 1