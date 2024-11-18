# Right Triangles
# Write a function that takes a positive integer, n, 
# as an argument and prints a right triangle whose sides each have n stars.
# The hypotenuse of the triangle (the diagonal side in the images below)
# should have one end at the lower-left of the triangle, and the other end at the upper-right.
# triangle(5) should print
#     *
#    **
#   ***
#  ****
# *****

# Solution

def triangle(num):
    for i in range(1, num + 1):
        print((' ' * (num - i)) + ('*' * i))

triangle(1)
triangle(5)
triangle(7)
triangle(9)

