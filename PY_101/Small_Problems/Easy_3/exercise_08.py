# Grade Book
# Write a function that determines the mean (average) of the three scores passed to it,
# and returns the letter associated with that grade.
# Numerical score letter grade list:
# 90 <= score <= 100: 'A'
# 80 <= score < 90: 'B'
# 70 <= score < 80: 'C'
# 60 <= score < 70: 'D'
# 0 <= score < 60: 'F'
# Tested values are all between 0 and 100. 
#There is no need to check for negative values or values greater than 100.

# Solution

def get_grade(grade1, grade2, grade3):
    mean_grade = (grade1 + grade2 + grade3) / 3.0
    rounded_mean = round(mean_grade)

    if rounded_mean >= 90:
        return "A"
    elif rounded_mean >= 80:
        return "B"
    elif rounded_mean >= 70:
        return "C"
    elif rounded_mean >= 60:
        return "D"
    else:
        return "F"

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True
print(get_grade(86, 80, 89) == "B")      # True
print(get_grade(10, 50, 100) == "F")     # True

# Using Dictionary 
def get_grade_updated(first, second, third):
    avg = (first + second + third) // 3

    grade_book = {
        range(90,101) : 'A',
        range(80, 90) : 'B',
        range(70, 80) : 'C',
        range(60, 70) : 'D',
        range(0, 60) : 'F'
    }

    for score, letter_grade in grade_book.items():
        if avg in score:
            return letter_grade
        
print(get_grade_updated(95, 90, 93) == "A")      # True
print(get_grade_updated(50, 50, 95) == "D")      # True
print(get_grade_updated(86, 80, 89) == "B")      # True
print(get_grade_updated(10, 50, 100) == "F")     # True