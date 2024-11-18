# When Will I Retire?
# Build a program that displays when the user will retire and how many years she has to work till retirement.
#What is your age? 30
#At what age would you like to retire? 70
#It's 2024. You will retire in 2064.
# You have only 40 years of work to go!

# Solution

from datetime import datetime

def ask_age():
    age = int(input("What is your age? "))

    return age

def ask_retirement_age():
    retire_age = int(input("At what age would you like to retire? "))

    return retire_age

def get_work_time_left(age_now, retiring_age):
    work_time = retiring_age - age_now

    return work_time

def get_current_year():
    current_date = datetime.now()
    current_year = current_date.year
    
    return current_year

def display_retirement_plans(current_year, work_time_left):
    print(f"It's {current_year}. You will retire in {current_year + work_time_left}")
    print(f"You have only {work_time_left} years of work to go!")


def main():
    age = ask_age()
    retirement_age = ask_retirement_age()
    present_year = get_current_year()
    working_time_left = get_work_time_left(age, retirement_age)
    display_retirement_plans(present_year, working_time_left)

main()
