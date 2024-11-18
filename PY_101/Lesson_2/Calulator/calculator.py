import json
import os
import time

# Imports .json file needed.
with open('calculator_messages.json', 'r') as file:
    MSG = json.load(file)

def prompt(message):
    print(f'==> {message}')

# Display welcome message
def display_welcome():
    prompt(MSG['en']['welcome'])

# Setting user language
def obtain_language(text):
    prompt(text)
    language = input()

    while language not in ['en', 'fr', 'es', 'de']:
        prompt(MSG['en']['invalid_lang'])
        prompt(MSG['en']['set_language'])
        language = input()

    return language

# Prevents invalid floats
def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

# Prevents invalid division
def invalid_division(num1, num2):
    try:
        float(num1) / float(num2)
    except ZeroDivisionError:
        return True

    return False

# Obtains first and second operands/numbers
def obtain_operands(lang):
    prompt(MSG[lang]['first_number'])
    numb1 = input()

    while invalid_number(numb1):
        prompt(MSG[lang]['invalid_number'])
        numb1 = input()

    prompt(MSG[lang]['second_number'])
    numb2 = input()

    while invalid_number(numb2):
        prompt(MSG[lang]['invalid_number'])
        numb2 = input()

    return numb1, numb2

# Obtains mathematical operation to be made
def obtain_operation(lang):
    prompt(MSG[lang]['operation'])
    choice = input()

    while choice not in ['1', '2', '3', '4']:
        prompt(MSG[lang]['choice'])
        choice = input()

    return choice

# Begins mathematical calculation
def obtain_calc(n1, n2, operation, lang):
    match operation:
        case '1':
            sign = '+'
            total = float(n1) + float(n2)
        case '2':
            sign = '-'
            total = float(n1) - float(n2)
        case '3':
            sign = '*'
            total = float(n1) * float(n2)
        case '4':
            sign = '/'
            while invalid_division(n1, n2):
                prompt(MSG[lang]['zero_division'])
                n1, n2 = obtain_operands(lang)

            total = float(n1) / float(n2)
            total = round(total, 2)

    return n1, n2, sign, total

# Displays results
def obtain_result(numb1, numb2, sign, total, lang):
    return prompt(f"{MSG[lang]['result']}{numb1} {sign} {numb2} = {total}")

# Ask user for another calculation
def another_calculation(lang):
    prompt(MSG[lang]['another_operation'])
    answer = input().strip().lower()

    while answer not in ['y', 'n', 's', 'j', 'o']:
        if answer == "":
            prompt(MSG[lang]['answer'])
        else:
            prompt(MSG[lang]['answer'])
        answer = input().strip().lower()

    return answer

# Clears IDE for windos, macOS and Linux
def clear_screen():
    # for macOS and Linux
    if os.name == 'posix':
        os.system('clear')
    # for windows
    elif os.name == 'nt':
        os.system('cls')

# Calculator function
def run_calculator():

    # Prints welcome message
    display_welcome()

    # Set Calculator language
    main_lang = obtain_language(MSG['en']['set_language'])

    while True:
        #get the operands (numbers to work with)
        num_1, num_2 = obtain_operands(main_lang)

        #ops = return value for the operator i.e +, - , *, /
        ops = obtain_operation(main_lang)

        num_1, num_2, sign, total = obtain_calc(num_1, num_2, ops, main_lang)

        obtain_result(num_1, num_2, sign, total, main_lang)

        # Asks user if they want to perform another calculation
        answer = another_calculation(main_lang)

        # clear screen before restating another calculation
        if answer == ['y', 's', 'j', 'o']:
            clear_screen()

        # end calculator program
        if answer and answer[0].lower() == 'n':
            prompt(MSG[main_lang]['end'])
            break

# Calulator Starts
run_calculator()

# Gives you enough time to read the goodbye message
time.sleep(3)

# Clears screen.
clear_screen()
