# Madlibs
# Madlibs is a simple game where you create a story template with "blanks" for words.
# You, or another player, then construct a list of words and place them into the story, 
# creating an often silly or funny story as a result.
# Create a simple madlib program that prompts for a noun, a verb, 
# an adverb, and an adjective, and injects them into a story that you create.
# Example
# Enter a noun: dog
# Enter a verb: walk
# Enter an adjective: blue
# Enter an adverb: quickly
# Expected output
# Do you walk your blue dog quickly? That's hilarious!
# The blue dog walks quickly over the lazy dog.
# The dog quickly walks up to Joe's blue turtle.

# Solution 

noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
adverb = input("Enter an adverb: ")

print(f"""
Do you {verb} your {adjective} {noun} quickly? That's hilarious!
The {adjective} {noun} {verb}s {adverb} over the lazy {noun}.
The {noun} {adverb} {verb}s up to Joe's {adjective} turtle.
      """)

# A Madlib star wars story

def star_wars_madlib():
    print("Welcome to the Star Wars Madlib! Please provide the following words:")
    
    character_name = input("A Star Wars character: ")
    planet = input("A fictional planet: ")
    creature = input("A type of creature: ")
    verb1 = input("A verb (action word): ")
    adjective1 = input("An adjective (describing word): ")
    noun1 = input("A noun (thing): ")
    verb2 = input("Another verb: ")
    adjective2 = input("Another adjective (describing word): ")
    silly_word = input("A silly word: ")
    food_item = input("A type of food: ")
    exclamation = input("An exclamation (e.g., Wow!): ")

    story = f"""
    Once upon a time in a galaxy far, far away, there was a {adjective1} hero named {character_name}.
    One day, {character_name} was traveling through the {adjective2} deserts of {planet} when they stumbled upon a
    group of {creature}s. These creatures were known for their strange habit of {verb1}ing {noun1}s.

    "What in the name of the Force is going on here?" {character_name} wondered aloud. Suddenly, a {creature}
    wearing a {silly_word} hat appeared and said, "{exclamation}! We need your help to {verb2} the great {food_item} of {planet}!"

    {character_name} couldn't believe their ears. With a shrug, they decided to help the {creature}s. Together,
    they {verb2}ed all the way to the hidden temple where the great {food_item} was kept. After a fierce battle,
    {character_name} emerged victorious and the {creature}s threw a huge celebration.

    And that, my friends, is how {character_name} saved {planet} from the great {food_item} disaster.
    The end.
    """

    print(story)

# Run the function to play the Madlib
star_wars_madlib()
