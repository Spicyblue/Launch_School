# Given a number and a list, determine whether the number is included in the list.
numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

print(8 in numbers)
print(95 in numbers)

# making a function to do this

def check_number(number_list, number):

    for numb in number_list:
        if number == numb:
            return True

    return False

print(check_number(numbers, 8))
print(check_number(numbers, 95))
