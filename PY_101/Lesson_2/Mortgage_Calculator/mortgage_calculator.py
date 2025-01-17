import json
import os
import time
import math

# Import .json file and save to dictionary to a constant
with open('mortgage_message.json', 'r') as file:
    MEMO = json.load(file)

YEAR_TO_MONTHS = 12
APR_CONVERSION = 0.01
CHECK_INF = [float('inf'), -float('inf')]
ZERO = 0
POSITIVE_CHOICES = ['yes', 'y', 'j', 'ja']
RESPONSE_CHOICES = ['y', 'yes','j', 'ja', 'n', 'no', 'nein']

# Inserts ==> before every message
def prompt(text):
    print(f"==> {text}")

def display_welcome():
    prompt(MEMO['en']['welcome'])

def clear_screen():
    # for macOS and Linux
    if os.name == 'posix':
        os.system('clear')
    # for windows
    elif os.name == 'nt':
        os.system('cls')

# Define user language for the application
def get_language():
    prompt(MEMO['en']['set_language'])
    language = input().strip().lower()

    while language not in ['en','de']:
        prompt(MEMO['en']['invalid_lang'])
        prompt(MEMO['en']['set_language'])
        language = input().strip().lower()

    return language

# Checks all input data type to ensure loan input is valid
def check_invalid_loan_amount(number_str, lang):
    try:
        check_num = float(number_str)
        if check_num <= ZERO:
            prompt(MEMO[lang]['invalid_amount'])
            return True
        if check_num in CHECK_INF:
            prompt(MEMO[lang]['invalid_text'])
            return True
        if math.isnan(check_num):
            raise ValueError
    except ValueError:
        prompt(MEMO[lang]['invalid_text'])
        return True

    return False

# Checks all input data type to ensure rate input is valid
def check_invalid_rate(number_str, lang):
    try:
        check_num = float(number_str)
        if check_num < ZERO:
            prompt(MEMO[lang]['negative_check'])
            return True
        if check_num in CHECK_INF:
            prompt(MEMO[lang]['invalid_text'])
            return True
        if math.isnan(check_num):
            raise ValueError
    except ValueError:
        prompt(MEMO[lang]['invalid_text'])
        return True

    return False

# Checks all input data type to ensure year input is valid
def check_invalid_year(number_str, lang):
    try:
        int(number_str)
        if int(number_str) < ZERO:
            prompt(MEMO[lang]['negative_check'])
            return True
    except ValueError:
        return True

    return False

# Checks all input data type to ensure month input is valid
def check_invalid_month(number_str, lang):
    try:
        int(number_str)
        if int(number_str) < ZERO:
            prompt(MEMO[lang]['negative_check'])
            return True
    except ValueError:
        return True

    return False

# Returns a valid loan amount
def ask_loan(lang):
    prompt(MEMO[lang]['loan_entry'])
    principal = input("$").strip().lower()

    while check_invalid_loan_amount(principal, lang):
        prompt(MEMO[lang]['invalid_loan_entry'])
        principal = input("$").strip().lower()

    return float(principal)

# Returns a valid interest rate
def ask_annual_interest_rate(lang):
    prompt(MEMO[lang]['rate_entry'])
    interest_rate = input().strip().lower()

    while check_invalid_rate(interest_rate, lang):
        prompt(MEMO[lang]['invalid_rate_entry'])
        interest_rate = input().strip().lower()

    interest_rate = round(float(interest_rate), 2)

    return float(interest_rate)

# Returns a valid year
def ask_years(lang):
    prompt (MEMO[lang]['year_entry'])
    loan_years = input().strip()

    while check_invalid_year(loan_years, lang):
        prompt (MEMO[lang]['invalid_entry'])
        prompt (MEMO[lang]['year_entry'])
        loan_years = input().strip()

    return int(loan_years)

# Returns a valid month
def ask_months(lang):
    prompt(MEMO[lang]['month_entry'])
    loan_months = input().strip()

    while check_invalid_year(loan_months, lang):
        prompt (MEMO[lang]['invalid_entry'])
        prompt(MEMO[lang]['month_entry'])
        loan_months = input().strip()

    return int(loan_months)

# Converts years to months if year is > 0
def get_years_to_months(year, month):
    if year > ZERO:
        entire_months = (year * YEAR_TO_MONTHS) + month
    else:
        entire_months = month

    return entire_months

# Returns the total months (including converted year(s))
def get_total_loan_duration(lang):
    years = ask_years(lang)
    months = ask_months(lang)
    total_months = get_years_to_months(years, months)

    while total_months == ZERO:
        prompt(MEMO[lang]['zero_duration'])
        years = ask_years(lang)
        months = ask_months(lang)
        total_months = get_years_to_months(years, months)

    return total_months

# Calculates and returns the monthly payment in 2 decimal places.
def get_monthly_payment(loan, rates, duration):
    if rates == ZERO:
        monthly_rate = ZERO
        amount = loan / duration
    else:
        monthly_rate = (rates * APR_CONVERSION) / YEAR_TO_MONTHS
        amount = loan * (monthly_rate /
                         (1 - (1 + monthly_rate) ** (-duration)))

    amount = round(float(amount), 2)

    return amount

# Display all user input and summary after calculation
def display_summary(credit, full_rate, time_span, repay, lang):
    recap_info = '\n'.join(MEMO[lang]['mortgage_summary'])
    prompt(recap_info.format(cash = credit,
                                APR = full_rate,
                                span = time_span,
                                refund = repay))

# Returns the answer necessary to restart the mortgage calculator
def ask_another_mortgage_calculation(lang):

    prompt(MEMO[lang]['restart'])
    response = input().strip().lower()

    while response not in RESPONSE_CHOICES:
        if response == "":
            prompt(MEMO[lang]['invalid_answer'])
            response = input().strip().lower()
        else:
            prompt(MEMO[lang]['invalid_answer'])
            response = input().strip().lower()

    return response

# Orchestration function for required for the main function.
def run_mortgage_calculator(lang):
    loan_amount = ask_loan(lang)
    interest_rate = ask_annual_interest_rate(lang)
    time_span = get_total_loan_duration(lang)
    monthly_cost = get_monthly_payment(loan_amount, interest_rate, time_span)
    display_summary(loan_amount, interest_rate, time_span, monthly_cost, lang)

# mini program than initites the app
def main():
    display_welcome()
    lang = get_language()

    while True:
        run_mortgage_calculator(lang)
        answer = ask_another_mortgage_calculation(lang)

        if answer not in POSITIVE_CHOICES:
            prompt(MEMO[lang]['farewell'])
            time.sleep(3)
            clear_screen()
            break

        prompt(MEMO[lang]['new_calculation'])
        time.sleep(2)
        clear_screen()

# main function necessary for mortgage calculator to run
main()
