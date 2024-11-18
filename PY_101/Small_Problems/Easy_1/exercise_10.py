# Multiples of 3 and 5
# Write a function that computes the sum of all numbers between 1 and some other number, inclusive, that are multiples of 3 or 5. 
# For instance, if the supplied number is 20, the result should be 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).
# You may assume that the number passed in is an integer greater than 1.

# Solution

def multisum(number):
    total_sum = 0

    for num in range(1, number + 1):
        if num % 3 == 0 or num % 5 == 0:
            total_sum += num

    return total_sum

# another way using list comprehension
def multisum(number):
    multiples = [num for num in range(1, number + 1) if num % 3 == 0 or num % 5 == 0]
    return sum(multiples)

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)
