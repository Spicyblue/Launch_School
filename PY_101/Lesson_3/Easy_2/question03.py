# Programmatically determine whether 42 lies between 10 and 100, inclusive. 
# Do the same for the values 100 and 101,

# using the range function
print(42 in range(10, 101))
print(100 in range(10, 101))
print(101 in range(10, 101))

# using the function to check everything
def check_number(start, stop, num_to_check):
    for x in range(start,stop + 1):
        if x == num_to_check:
            return True
    return False

print(check_number(10, 100, 42))
print(check_number(10, 100, 100))
print(check_number(10, 100, 101))