#Write a program that takes the radius of circle as input and return its area,use the formula Area=ph*r^2. in python. Round the output to 2 decimal places.
import math

def circle_area(radius):
    return round(math.pi * radius ** 2, 2)

# Test cases
print("Test Case 1: Input radius = 5")
print("Output:", circle_area(5))  # Expected: 78.54

print("Test Case 2: Input radius = 3")
print("Output:", circle_area(3))  # Expected: 28.27
