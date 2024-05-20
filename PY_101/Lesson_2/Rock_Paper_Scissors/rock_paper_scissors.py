import random
import json
import time
import os
import sys

with open ('game_play_messages.json', 'r') as file:
    INFO = json.load(file)

# Constant used
VALID_CHOICES = {'r'  : 'rock',
                 'p'  : 'paper', 
                 's'  : 'scissors', 
                 'l'  : 'lizard', 
                 'sp' : 'spock'}

WINNING_COMBOS = {
    'rock'  : ['scissors', 'lizard'],
    'paper' : ['rock', 'spock'],
    'scissors' : ['paper', 'lizard'],
    'lizard' : ['paper', 'spock'],
    'spock' : ['rock', 'scissors']
    }

VALID_RESPONSE = ['yes', 'y', 'no', 'n']
WIN_SCORE = 3

# Stylize print function to include '==>' before messages
def prompt(text):
    print(f"==> {text}")

def clear_screen():
    # for macOS and Linux
    if os.name == 'posix':
        os.system('clear')
    # for windows
    elif os.name == 'nt':
        os.system('cls')

def display_welcome():
    prompt(INFO['welcome'])
    time.sleep(2)

def display_game_info():
    prompt(''.join(INFO['game_intro']))
    time.sleep(2)

    prompt(''.join(INFO['how_to_play']))
    time.sleep(2)

    prompt(''.join(INFO['game_rules']))
    time.sleep(4)

    prompt(''.join(INFO['win_rules']))
    time.sleep(4)

def display_choice():
    prompt(''.join(INFO['choice']))

def display_score(score_table):
    score_info = ''.join(INFO['game_summary'])
    prompt(score_info.format(board = score_table))
    time.sleep(2)

def display_winner(player, computer, round_winner):
    winner_info = INFO['round_winner']
    prompt(winner_info.format(user_choice = player,
                              virtual_choice = computer))

    if round_winner == 'player wins':
        prompt(INFO['player_win'])
    elif round_winner == 'computer wins':
        prompt(INFO['computer_win'])
    else:
        prompt(INFO['tie'])

    time.sleep(2)

def display_overall_winner(scores):
    if scores['player'] > scores['computer']:
        prompt(INFO['winner'])
    else:
        prompt(INFO['try_again'])

# Ask player after reading game info if they are ready to start!
def ask_start_game():

    while True:
        prompt(INFO['start_game'])
        answer = input('Enter your answer: ').strip().lower()

        while answer not in VALID_RESPONSE:
            prompt(INFO['invalid_choice'])
            prompt(INFO['start_game'])
            answer = input('Enter your answer: ').strip().lower()
        break
    return answer

def ask_player_choice():

    while True:
        display_choice()

        answer = input('Enter your choice: ').strip().lower()
        answer = check_choice(answer)
        while answer not in list(VALID_CHOICES.values()):
            prompt(INFO['invalid_choice'])
            display_choice()
            answer = input('Enter your choice: ').strip().lower()
            answer = check_choice(answer)
        break

    return answer

def ask_restart_game():

    while True:
        prompt('Do you want to play again? (y/n)?')
        answer = input('Enter your answer: ').strip().lower()

        while answer not in VALID_RESPONSE:
            prompt(INFO['yes_or_no'])
            answer = input('Enter your answer: ').strip().lower()
        break

    return answer

def check_choice(player_input):
    if player_input in VALID_CHOICES:
        return VALID_CHOICES[player_input]
    if player_input in VALID_CHOICES.values():
        return player_input

    return None

# checks updated score table and return false when score == 3
def check_scores(scores):
    return WIN_SCORE not in [scores['player'], scores['computer']]

def get_computer_choice():
    return random.choice(list(VALID_CHOICES.values()))

def get_player_wins(player_choice, computer_choice):
    return computer_choice in WINNING_COMBOS[player_choice]

def get_winner(player, computer):
    champion = ""

    if get_player_wins(player, computer):
        champion = 'player wins'
    elif player == computer:
        champion = 'tie'
    else:
        champion = 'computer wins'

    return champion

# Validates player response to either start or end game!
def start_game(answer_string):

    if answer_string.startswith('n'):
        prompt(INFO['goodbye'])
        time.sleep(2)
        clear_screen()
        sys.exit()
    else:
        prompt(INFO['begin_game'])
        time.sleep(1)

def update_scoreboard(score, winner):

    if winner == 'player wins':
        score['player'] += 1
        score['rounds'] += 1
    elif winner == 'computer wins':
        score['computer'] += 1
        score['rounds'] += 1
    else:
        score['rounds'] += 1

#orchestra function that displays game information
def game_play_intro():
    display_welcome()
    display_game_info()
    response = ask_start_game()
    start_game(response)
    clear_screen()

# orchestra function that runs the ROPSACLISP game
def run_ropasclisp_game():
    score_board = {'player' : 0,
                'computer' : 0,
                'rounds' : 0}

    while check_scores(score_board):
        choice = ask_player_choice()
        computer_choice = get_computer_choice()
        result = get_winner(choice, computer_choice)
        display_winner(choice, computer_choice, result)
        update_scoreboard(score_board, result)
        clear_screen()
        display_score(score_board)
    display_overall_winner(score_board)

# main function
def main():
    game_play_intro()

    while True:
        run_ropasclisp_game()

        while True:
            reply = ask_restart_game()

            if reply in VALID_RESPONSE:
                break

        if reply[0].startswith('n'):
            prompt(INFO['goodbye'])
            time.sleep(2)
            clear_screen()
            break

# Main function call
main()  