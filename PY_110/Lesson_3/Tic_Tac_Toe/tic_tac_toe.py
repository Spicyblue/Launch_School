#*****************************************************#
#            All Modules and Libraries Used           #
#*****************************************************#

import random as rd
import os
import time

#*****************************************************#
#               All Constants Used                    #
#*****************************************************#

INITIAL_MARKER = ' '
PLAYER_MARKER = 'X'
AI_MARKER = 'O'
VALID_RESPONSE = ['yes', 'y', 'no', 'n']
POSITIVE_ANSWER = ['yes', 'y']
NEGATIVE_ANSWER = ['no', 'n']
WINNING_CONDITION = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]
GAMES_NEEDED_TO_WIN = 3
FIRST_PLAYER = "choose"

#*****************************************************#
#   All helper function for stylizing or displaying   #
#*****************************************************#

def boxify_message(message):
    '''
    Create a block around a message body
    '''
    lines = message.strip().split('\n')
    max_length = max(len(line) for line in lines)
    print('+' + '-' * (max_length + 2) + '+')
    for line in lines:
        print(f'| {line.ljust(max_length)} |')
    print('+' + '-' * (max_length + 2) + '+')

def clear_terminal():
    '''
    clear terminal before executing the next code.
    '''
    os.system('clear')

def three_seconds_delay():
    '''
    Add a 3 seconds system delay before executing the next code
    '''
    time.sleep(3)

def prompt(message):
    '''
    Stylize strings that are printed to the terminal
    by adding ===> before printing.
    '''
    print(f"===> {message}")

def display_game_board(board, username, scoreboard):
    '''
    Display the board for tic tac toe and the respective
    marker for both the user/player and computer.
    '''
    horizonatal_divider = "-----" + ("+-----" * 2)
    vertical_divider = "     |" * 2

    clear_terminal()

    display_scoreboard(scoreboard, username)
    print('\n')
    print(f"{username} is {PLAYER_MARKER}. Computer is {AI_MARKER} \n")
    print(vertical_divider)
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}  ")
    print(vertical_divider)
    print(horizonatal_divider)
    print(vertical_divider)
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}  ")
    print(vertical_divider)
    print(horizonatal_divider)
    print(vertical_divider)
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}  ")
    print(vertical_divider)
    print('\n')

def display_game_instructions():
    '''
    Instruction on how to play
    '''
    training_board = display_training_board()

    message = f"""
How to Play:
The layout of the board is shown belown 
{training_board}
Choose a number between 1 and 9 to mark your position on the board.
Remember!
The first player to get 3 squares in a row
-- horizontally, vertically, or diagonally -- wins a round.
All the best!!!
"""
    boxify_message(message)

def display_grand_winner(scoreboard, username):
    '''
    Display the grand winner based on who gets to
    three wins first.
    '''
    if scoreboard[username] == GAMES_NEEDED_TO_WIN:
        prompt(f'Congrats, {username} is the grand winner!')
    elif scoreboard['Computer'] == GAMES_NEEDED_TO_WIN:
        prompt('Computer is the grand winner! Try again!')

def display_finished_game_round(scoreboard, winner, username):
    '''
    Display the round after a match ends.
    '''
    if winner in [username, "Computer"]:
        prompt(f"{winner} won this game round")

    if winner not in [username, "Computer"]:
        prompt("A tie! Tough game right?")

    prompt(f"End of round {scoreboard['round']}.")

def display_scoreboard(score_board, username):
    '''
    Display the score board for the game.
    '''
    user_score_label = f"{username} score is:"
    ai_score_label = "A.I score is:"
    round_label = "Current round is:"

    max_label_length = max(len(user_score_label),
                           len(ai_score_label),
                           len(round_label))

    prompt(f"{user_score_label:<{max_label_length}} {score_board[username]}")
    prompt(f"{ai_score_label:<{max_label_length}} {score_board['Computer']}")
    prompt(f"{round_label:<{max_label_length}} {score_board['round']}")

def display_training_board():
    '''
    Generate the training board to show positions that user can mark
    '''
    horizontal_divider = "-----" + ("+-----" * 2)
    vertical_divider = "     |     |"

    board_lines = [
        vertical_divider,
        "  1  |  2  |  3  ",
        vertical_divider,
        horizontal_divider,
        vertical_divider,
        "  4  |  5  |  6  ",
        vertical_divider,
        horizontal_divider,
        vertical_divider,
        "  7  |  8  |  9  ",
        vertical_divider,
    ]

    return '\n'.join(board_lines)

def display_welcome_message():
    """
    Display welcome message to to user
    """
    message = """
Welcome to Tic Tac Toe Game:
Tic Tac Toe is a 2-player game played on a 3x3 grid called the board.
Each player takes a turn and marks a square on the board.
The first player to get 3 squares in a row
-- horizontally, vertically, or diagonally -- wins a round.
If all squares are filled with no winner, game is a Tie. 
The grand winner is the best of 5 (first to get to 3 points)
    """
    boxify_message(message)

def join_or(list_entry, sep = ', ', word = 'or'):
    '''
    stylize the available position(s) that can be played on the board.
    '''
    match len(list_entry):
        case 0:
            return ''
        case 1:
            return str(list_entry[0])
        case 2:
            return f"{list_entry[0]} {word} {list_entry[1]}"
        case _:
            preceding_values = sep.join(str(num) for num in list_entry[ : -1])
            return f"{preceding_values}{sep}{word} {list_entry[-1]}"

#*****************************************************#
#  All helper function for user input and validation  #
#*****************************************************#

def ask_enter_to_proceed():
    '''
    Ask user to press enter to proced.
    '''
    while True:
        prompt('Done reading? Please Press "Enter" to proceed')
        answer = input()

        if answer == "":
            break

        prompt("This is not a valid answer")

def ask_next_round(scoreboard):
    '''
    Ask user if they are ready for next round.
    '''
    while True:
        prompt(f"Ready for round {scoreboard['round']}.")
        prompt("Hit Enter or type 'yes': ")
        answer = input().strip().lower()

        if answer == "" :
            break
        if answer in POSITIVE_ANSWER:
            break

        prompt("This is not a valid answer")

def ask_restart_game():
    '''
    Ask user if they want to play again and return their answer.
    '''
    while True:
        clear_terminal()
        prompt('Do you want to play again? (yes / no)?')
        prompt('Enter your answer: ')
        answer = input().strip().lower()

        if answer in VALID_RESPONSE:
            return answer

        prompt("This is not a valid answer")
        three_seconds_delay()

def ask_user_name():
    '''
    Ask user to input their username and validate the username during game play
    '''
    while True:
        clear_terminal()

        prompt('Enter your user name:')
        name = input().strip()

        if validate_username(name):
            while True:
                accepted_name  = confirm_username(name)

                if accepted_name:
                    return accepted_name

                if not accepted_name:
                    break

        if not validate_username(name):
            prompt('Please enter a valid name (atleast one character)')
            three_seconds_delay()

def ask_who_to_start_game(username):
    '''
    Ask user to choose who goes first between user and computer
    and returns users choice.
    '''
    if FIRST_PLAYER == 'choose':
        computer = 'Computer'
        while True:
            clear_terminal()
            prompt("Enter number '1' or '2' for who plays first:")
            prompt(f"1: {username} plays first ")
            prompt("2: Computer plays first ")

            answer = input().strip()
            match answer:
                case '1':
                    return username
                case '2':
                    return computer
                case _:
                    prompt("Sorry, this is not a valid choice")
                    prompt("Please Choose 1 or 2.")
                    three_seconds_delay()

    else:
        return None

def confirm_username(username):
    '''
    Confirms and returns username entered or returns a bool that
    allows user to update their username.
    '''
    while True:
        clear_terminal()

        prompt(f"Do you want to proceed with '{username}'")
        prompt('yes / no')

        answer = input().lower().strip()

        if answer in POSITIVE_ANSWER:
            return username

        if answer in NEGATIVE_ANSWER:
            prompt('You can change your username now')
            three_seconds_delay()
            return False

        if answer not in VALID_RESPONSE:
            prompt('This is not a valid answer')
            three_seconds_delay()

def validate_username(username):
    '''
    Validates username input by ensuring it is 
    alphanumeric (symbols accepted) and atleast with
    one character.
    '''
    return  username.isalnum and len(username) > 0

#*****************************************************#
#    All helper function concerned with gameplay      #
#*****************************************************#

def alternate_player(username, current_player):
    '''
    Checks the current player and return the alternate 
    player for the next game round
    '''
    computer = 'Computer'

    if current_player == username:
        return computer

    if current_player == computer:
        return username

    return None

def best_defense_and_offense(line, board, marker):
    '''
    Return the best position on the board for computer to either play
    offensively or defensively.
    '''
    if[board[position] for position in line].count(marker) == 2:
        for position in line:
            if board[position] == INITIAL_MARKER:
                return position

    return None

def best_of_five(score_board):
    '''
    Checks if the current game score for both the user 
    and computer is equall to the score needed to win
    and return True, else False.
    '''
    for score in score_board.values():
        if score == GAMES_NEEDED_TO_WIN:
            return True

    return False

def board_full(board):
    '''
    Return a bool True if all position in the board
    is filled, else False
    '''
    return len(empty_position(board)) == 0

def choose_position(board, current_player, username):
    '''
    Determines who plays a position on the board 
    based on the current player.
    '''
    if current_player == 'Computer':
        computer_chooses_position(board)

    if current_player == username:
        player_choose_position(board)

def computer_chooses_position(board):
    '''
    Sometimes the best defense is offense. 
    Core function that allows computer to choose 
    and order of play based on availability
    first an offensive position (if available)
    Second a defensitve podition (if available)
    Third the strategic position 5 (if available)
    A random position (if available).
    '''
    if board_full(board):
        return

    position = None

    for line in WINNING_CONDITION:
        position = best_defense_and_offense(line, board, AI_MARKER)
        if position:
            break

    if not position:
        for line in WINNING_CONDITION:
            position = best_defense_and_offense(line, board, PLAYER_MARKER)
            if position:
                break

    if not position and board[5] == INITIAL_MARKER:
        position = 5

    if not position:
        position = rd.choice(empty_position(board))

    board[position] = AI_MARKER

def empty_position(board):
    '''
    Checks and return the position(s) on the board
    that are free or empty.
    '''
    return [key for key, value in board.items()
            if value == INITIAL_MARKER]

def get_winner(board, username):
    '''
    Checks if there is a winning combination
    on the board and returns who has the winning
    combination (user or computer).
    '''
    computer = 'Computer'

    for line in WINNING_CONDITION:
        pos1, pos2, pos3 = line
        if (board[pos1] == PLAYER_MARKER
            and board[pos2] == PLAYER_MARKER
            and board[pos3] == PLAYER_MARKER):
            return username

        if (board[pos1] == AI_MARKER
              and board[pos2] == AI_MARKER
              and board[pos3] == AI_MARKER):
            return computer

    return None

def initialize_scoreboard(username):
    '''
    Initalize a dictionary used to access the 
    score board.
    '''
    game_board = {f'{username}': 0,
                   'Computer' : 0,
                   'round' : 0
                   }

    return game_board

def player_choose_position(board):
    '''
    Core function that allows user/player to choose a
    position on the board.
    '''
    if board_full(board):
        return

    while True:
        valid_choices = [str(num) for num in empty_position(board)]
        prompt(f"'Choose a position ({join_or(valid_choices)}): ")
        position = input().strip()
        if position in valid_choices:
            position = int(position)
            break

        prompt("Sorry, this in not a valid position")

    board[position] = PLAYER_MARKER

def reset_game_board():
    '''
    Initalize a dictionary used to access and reset the 
    game board.
    '''
    return {position: " " for position in range(1, 10)}

def someone_won(board, username):
    '''
    Checks and return True if there is a round 
    winner, else False.
    '''
    return bool(get_winner(board, username))

def update_score(scoreboard, winner, username):
    '''
    Access the dictionary for the scoreboard and
    updates the score based on the winner of the
    game round. For a tie, increments only the 
    round count.
    '''

    if winner == username:
        scoreboard[username] += 1
        scoreboard['round'] += 1

    if winner == 'Computer':
        scoreboard['Computer'] += 1
        scoreboard['round'] += 1

    else:
        scoreboard['round'] += 1
        prompt("A Tie! Tought game right!! Keep trying!!!")

#*****************************************************#
#      All orchestral game and main function          #
#*****************************************************#

def game_play_intro():
    '''
    orchestral function that welcomes player and
    displays instructions.
    '''
    display_welcome_message()
    ask_enter_to_proceed()
    clear_terminal()
    display_game_instructions()
    ask_enter_to_proceed()
    clear_terminal()

def play_a_single_game_round(player_name, current_player, game_score):
    '''
    orchestral function that plays a single game round and
    finds the winner
    '''
    board = reset_game_board()
    while True:
        display_game_board(board, player_name, game_score)
        choose_position(board, current_player, player_name)
        current_player = alternate_player(player_name, current_player)
        if someone_won(board, player_name) or board_full(board):
            winner = get_winner(board, player_name)
            update_score(game_score, winner, player_name)
            display_game_board(board, player_name, game_score)
            display_finished_game_round(game_score, winner, player_name)
            three_seconds_delay()
            break

def play_tic_tac_toe():
    '''
    main function that shows main game logic
    '''
    game_play_intro()
    player_name = ask_user_name()

    start_game = True
    while start_game:
        current_player = ask_who_to_start_game(player_name)
        game_score = initialize_scoreboard(player_name)

        while not best_of_five(game_score):
            play_a_single_game_round(player_name, current_player, game_score)
            if best_of_five(game_score):
                break
            ask_next_round(game_score)

        display_grand_winner(game_score, player_name)
        three_seconds_delay()

        answer = ask_restart_game()

        if answer not in POSITIVE_ANSWER:
            start_game = False

        prompt('Thank you for playing Tic Tac Toe')

#*****************************************************#
#                 main function call                  #
#*****************************************************#

play_tic_tac_toe()