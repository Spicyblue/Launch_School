import json
import os
import time

# Import .json file and save to dictionary to a constant
with open('mortgage_message.json', 'r') as file:
    MEMO = json.load(file)

YEAR_TO_MONTHS = int(12)
APR_CONVERSION = 0.01
CHECK_INF_NAN = [float('inf'), -float('inf')]

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

def get_language():
    prompt(MEMO['en']['set_language'])
    language = input().strip().lower()

    while language not in ['en','de']:
        prompt(MEMO['en']['invalid_lang'])
        prompt(MEMO['en']['set_language'])
        language = input().strip().lower()

    return language

def check_invalid_loan_amount(number_str, lang):
    try:
        check_num = float(number_str)
        if check_num <= 0:
            prompt(MEMO[lang]['invalid_amount'])
            return True
        if check_num in CHECK_INF_NAN:
            prompt(MEMO[lang]['invalid_text'])
            return True
    except ValueError:
        prompt(MEMO[lang]['invalid_text'])
        return True

    return False

def check_invalid_rate(number_str, lang):
    try:
        check_num = float(number_str)
        if check_num < 0:
            prompt(MEMO[lang]['negative_check'])
            return True
        if check_num in CHECK_INF_NAN:
            prompt(MEMO[lang]['invalid_text'])
            return True
    except ValueError:
        prompt(MEMO[lang]['invalid_text'])
        return True

    return False

def check_invalid_year(number_str, lang):
    try:
        int(number_str)
        if int(number_str) < 0:
            prompt(MEMO[lang]['negative_check'])
            return True
    except ValueError:
        return True

    return False

def check_invalid_month(number_str, lang):
    try:
        int(number_str)
        if int(number_str) < 0:
            prompt(MEMO[lang]['negative_check'])
            return True
    except ValueError:
        return True

    return False

def get_loan(lang):
    prompt(MEMO[lang]['loan_entry'])
    principal = input("$").strip().lower()

    while check_invalid_loan_amount(principal, lang):
        prompt(MEMO[lang]['invalid_loan_entry'])
        principal = input("$").strip().lower()

    return float(principal)

def get_annual_interest_rate(lang):
    prompt(MEMO[lang]['rate_entry'])
    interest_rate = input().strip().lower()

    while check_invalid_rate(interest_rate, lang):
        prompt(MEMO[lang]['invalid_rate_entry'])
        interest_rate = input().strip().lower()

    interest_rate = round(float(interest_rate), 2)

    return float(interest_rate)

def get_years(lang):
    prompt (MEMO[lang]['year_entry'])
    loan_years = input().strip()

    while check_invalid_year(loan_years, lang):
        prompt (MEMO[lang]['invalid_entry'])
        prompt (MEMO[lang]['year_entry'])
        loan_years = input().strip()

    return int(loan_years)

def get_months(lang):
    prompt(MEMO[lang]['month_entry'])
    loan_months = input().strip()

    while check_invalid_year(loan_months, lang):
        prompt (MEMO[lang]['invalid_entry'])
        prompt(MEMO[lang]['month_entry'])
        loan_months = input().strip()

    return int(loan_months)

def get_years_to_months(year, month):
    if year > 0:
        entire_months = (year * YEAR_TO_MONTHS) + month
    else:
        entire_months = month

    return entire_months

def get_total_loan_duration(lang):
    years = get_years(lang)
    months = get_months(lang)
    total_months = get_years_to_months(years, months)

    while total_months == 0:
        prompt(MEMO[lang]['zero_duration'])
        years = get_years(lang)
        months = get_months(lang)
        total_months = get_years_to_months(years, months)

    return total_months

def get_monthly_payment(loan, rates, duration):
    if rates == 0:
        monthly_rate = 0
        amount = loan / duration
    else:
        monthly_rate = (rates * APR_CONVERSION) / YEAR_TO_MONTHS
        amount = loan * (monthly_rate /
                         (1 - (1 + monthly_rate) ** (-duration)))

    amount = round(float(amount), 2)

    return amount

def display_summary(credit, full_rate, time_span, repay, lang):
    recap_info = '\n'.join(MEMO[lang]['morgage_summary'])
    prompt(recap_info.format(cash = credit,
                                APR = full_rate,
                                span = time_span,
                                refund = repay))

def get_another_mortgage_calculation(lang):
    choices = ['y', 'yes','j', 'ja', 'n', 'no', 'nein']

    prompt(MEMO[lang]['restart'])
    response = input().strip().lower()

    while response not in choices:
        if response == "":
            prompt(MEMO[lang]['invalid_answer'])
            response = input().strip().lower()
        else:
            prompt(MEMO[lang]['invalid_answer'])
            response = input().strip().lower()

    return response

def get_morgage_entries(lang):
    loan_amount = get_loan(lang)
    interest_rate = get_annual_interest_rate(lang)
    time_span = get_total_loan_duration(lang)
    monthly_cost = get_monthly_payment(loan_amount, interest_rate, time_span)
    display_summary(loan_amount, interest_rate, time_span, monthly_cost, lang)

def run_mortgage_caulator(lang):
    while True:
        get_morgage_entries(lang)
        answer = get_another_mortgage_calculation(lang)
        positive_choice = ['yes', 'y', 'j', 'ja']

        if answer not in positive_choice:
            prompt(MEMO[lang]['farewell'])
            time.sleep(3)
            clear_screen()
            break

        prompt(MEMO[lang]['new_calculation'])
        time.sleep(3)
        clear_screen()

def main():
    display_welcome()
    lang = get_language()
    run_mortgage_caulator(lang)

main()