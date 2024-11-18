'''
Example 2.

Update your code from the previous question so the following code works as indicated:

bingo = Bingo('Bingo', 'Bill')
print(Game.count)                       # 1
print(bingo.play())                     # Start the Bingo game!
print(bingo.player_name)                # Bill

scrabble = Scrabble('Scrabble', 'Jill', 'Sill')
print(Game.count)                       # 2
print(scrabble.play())                  # Start the Scrabble game!
print(scrabble.player_name1)            # Jill
print(scrabble.player_name2)            # Sill
print(scrabble.player_name)
# AttributeError: 'Scrabble' object has no attribute 'player_name'

'''

# Solution

class Game:
    count = 0


    def play(self):
        return f'Start the {self.game} game!'

class Bingo(Game):
    
    def __init__(self, game, player_name):
        self.game = game
        self.player_name = player_name
        Game.count += 1

class Scrabble(Game):
    
    def __init__(self, game, player_name1, player_name2):
        self.game = game
        self.player_name1 = player_name1
        self.player_name2 = player_name2
        Game.count += 1

bingo = Bingo('Bingo', 'Bill')
print(Game.count)                       # 1
print(bingo.play())                     # Start the Bingo game!
print(bingo.player_name)                # Bill

scrabble = Scrabble('Scrabble', 'Jill', 'Sill')
print(Game.count)                       # 2
print(scrabble.play())                  # Start the Scrabble game!
print(scrabble.player_name1)            # Jill
print(scrabble.player_name2)            # Sill
# print(scrabble.player_name)
# # AttributeError: 'Scrabble' object has no attribute 'player_name'

## LS Solution ##

# class Game:
#     count = 0

#     def __init__(self, game_name):
#         self.game_name = game_name
#         Game.count += 1

#     def play(self):
#         return f'Start the {self.game_name} game!'

# class Bingo(Game):
#     def __init__(self, game_name, player_name):
#         super().__init__(game_name)
#         self.player_name = player_name

# class Scrabble(Game):
#     def __init__(self, game_name, player_name1, player_name2):
#         super().__init__(game_name)
#         self.player_name1 = player_name1
#         self.player_name2 = player_name2