'''
Example 1.

class Game:
    def play(self):
        return 'Start the game!'

class Bingo:
    pass

Update this code so that Bingo inherits the play method from the Game class.

'''

# Solution

class Game:
    def play(self):
        return 'Start the game!'

class Bingo(Game):
    pass

## LS Solution ##

# class Game:
#     def play(self):
#         return 'Start the game!'

# class Bingo(Game):
#     pass
