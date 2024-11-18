import random as rd
import os

def clear_screen():
    os.system('clear')

class Square:
    INITIAL_MARKER = " "
    HUMAN_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, marker = INITIAL_MARKER):
        self.marker = marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker

    def is_unused(self):
        return self.marker == Square.INITIAL_MARKER

    def __str__(self):
        return self.marker

class Board:
    def __init__(self):
        self.squares = {key: Square() for key in range(1, 10)}

    def display_with_clear_screen(self):
        clear_screen()
        print()
        self.display()

    def display(self):
        print()
        print("     |     |")
        print(f"  {self.squares[1]}  |"
              f"  {self.squares[2]}  |"
              f"  {self.squares[3]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[4]}  |"
              f"  {self.squares[5]}  |"
              f"  {self.squares[6]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[7]}  |"
              f"  {self.squares[8]}  |"
              f"  {self.squares[9]}")
        print("     |     |")
        print()

    def count_markers_for(self, player, keys):
        marker = [self.squares[key].marker for key in keys ]
        return marker.count(player.marker)

    def is_full(self):
        return len(self.unused_squares()) == 0

    def mark_square(self, key, marker):
        self.squares[key].marker = marker

    def unused_squares(self):
        return [key for key, square in self.squares.items()
                if square.is_unused()]

class Player:
    def __init__(self, marker):
        self.marker = marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, value):
        self._marker = value

class Human(Player):
    def __init__(self):
        super().__init__(Square.HUMAN_MARKER)

class Computer(Player):
    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)

class TTTGame:
    POSSIBLE_WINNING_ROWS = (
        (1, 2, 3),  # top row of board
        (4, 5, 6),  # center row of board
        (7, 8, 9),  # bottom row of board
        (1, 4, 7),  # left column of board
        (2, 5, 8),  # middle column of board
        (3, 6, 9),  # right column of board
        (1, 5, 9),  # diagonal: top-left to bottom-right
        (3, 5, 7),  # diagonal: top-right to bottom-left
    )

    def __init__(self):
        self.board = Board()
        self.human = Human()
        self.computer = Computer()

    def computer_moves(self):
        valid_choice = self.board.unused_squares()
        choice = rd.choice(valid_choice)
        self.board.mark_square(choice, self.computer.marker)

    def display_goodbye_message(self):
        print("Thanks for playing Tic Tac Toe")

    def display_results(self):
        if self.is_winner(self.human):
            print("You won! Congratulations!")
        elif self.is_winner(self.computer):
            print("AI will rule the world")
        else:
            print("A tie game.")

    def display_welcome_message(self):
        clear_screen()
        print("Welcome to Tic Tac Toe")
        print()

    def human_moves(self):
        choice = None

        while True:
            valid_choice = self.board.unused_squares()
            choices_list = [str(choice) for choice in valid_choice]
            choice_str = ", ".join(choices_list)
            prompt = f"Choose a square ({choice_str}): \n"
            choice = input(prompt)

            try:
                choice = int(choice)
                if choice in valid_choice:
                    break
            except ValueError:
                pass
            print("Sorry, that's not a valid choice.")
            print()

        self.board.mark_square(choice, self.human.marker)

    def is_game_over(self):
        return self.board.is_full() or self.someone_won()

    def is_winner(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.three_in_a_row(player, row):
                return True
        return False

    def someone_won(self):
        return (self.is_winner(self.human) or self.is_winner(self.computer))

    def three_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == 3

    def play(self):
        self.display_welcome_message()
        self.board.display()

        while True:
            self.human_moves()
            if self.is_game_over():
                break

            self.computer_moves()
            if self.is_game_over():
                break

            self.board.display_with_clear_screen()

        self.board.display_with_clear_screen()
        self.display_results()
        self.display_goodbye_message()

game = TTTGame()
game.play()

