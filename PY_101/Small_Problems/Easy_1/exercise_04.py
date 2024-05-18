import math

# constrants used
CONVERT_TO_SQUARE_FEET = 10.7638
ZERO = 0
MEASUREMENT = ['feet', 'meter']

def display_welcome():
    print('Welcome to Room Area Calulator')

# validate float inputs
def get_valid_float(number_str):
    try:
        num = float(number_str)
        if num <= ZERO:
            print('Negative or Zero values not accepter')
            return True
        if math.isnan(num) or math.isinf(num):
            raise ValueError
    except ValueError:
        print('Hmm... this is not a valid answer')
        return True

    return False

def ask_length():
    room_lenght = input('Please enter lenght of room: ')

    while get_valid_float(room_lenght):
        room_lenght = input('Please enter lenght of room: ')

    return float(room_lenght)

def ask_width():
    room_width = input('Please enter widht of room: ')

    while get_valid_float(room_width):
        room_width = input('Please enter widht of room: ')

    return float(room_width)

def get_area(room_lengh, room_width):
    area = room_lengh * room_width

    return area

def ask_measurement_type():
    print('Do you want to measure in meters or feets')
    answer = input("Please enter 'meter' or 'feet':").strip().lower()

    while answer not in MEASUREMENT:
        print('This is not a valid answer')
        answer = input("Please enter 'meter' or 'feet':").strip().lower()

    return answer

def display_measurement(measurement, area):

    if measurement == 'meter':
        print(f"The roam area is {area:.2f} square meters")
    elif measurement == 'feet':
        area_in_feet = area * CONVERT_TO_SQUARE_FEET
        print (f'The roam area is {area_in_feet:.2f} square feets')
    else:
        print('Cant calculate this measurement!')

def main():
    display_welcome()
    lenght = ask_length()
    width = ask_width()
    area = get_area(lenght, width)
    measurement_type = ask_measurement_type()
    display_measurement(measurement_type, area)

main()