"""Call the functions from utils.py to calculate the area and perimeter of a rectangle based on user input."""
from utils import rectangle_area, rectangle_perimeter
# Get user input for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
# Calculate area and perimeter
area = rectangle_area(length, width)
perimeter = rectangle_perimeter(length, width)
# Display the results
print(f"The area of the rectangle is: {area}")
print(f"The perimeter of the rectangle is: {perimeter}")
