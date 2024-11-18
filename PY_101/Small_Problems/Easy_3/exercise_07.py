# Double Doubles
# A double number is an even-length number whose left-side digits are exactly the same as its right-side digits.
#  For example, 44, 3333, 103103, and 7676 are all double numbers,
# whereas 444, 334433, and 107 are not.
# Write a function that returns the number provided as an argument multiplied by two, 
# unless the argument is a double number. If the argument is a double number, return the double number as-is.

# Solution

def twice(number):
    num = str(number)
    left_side = []
    right_side = []
    mid_index = len(num)// 2
    if len(num) % 2 == 0:
        left_side += num[:mid_index]
        right_side += num[mid_index:]
        if left_side == right_side:
            return number
        else:
            return number * 2
    else:
        return number * 2
    
# A more concise solution

def twice_updated(number):
    num = str(number)
    mid_index = len(num)// 2
    if num[:mid_index] == num[mid_index:]:
        return number
    else:
        return number * 2

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True

print(twice_updated(37) == 74)                  # True
print(twice_updated(44) == 44)                  # True
print(twice_updated(334433) == 668866)          # True
print(twice_updated(444) == 888)                # True
print(twice_updated(107) == 214)                # True
print(twice_updated(103103) == 103103)          # True
print(twice_updated(3333) == 3333)              # True
print(twice_updated(7676) == 7676)              # True
