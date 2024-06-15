# This program calculates the area of a triangle using Circumradius.

import math  # Importing math module for sine function

# Function to calculate the area of a triangle using Circumradius
def calculate_triangle_area_circumradius(R):
    # Calculate the area using the formula: Area = R^2 * sin(A) * sin(B) * sin(C) / (4 * sin(A + B + C))
    area = R * R * math.sin(math.pi / 3) * math.sin(math.pi / 3) / (2 * math.sin(math.pi / 3))
    return area

# Main function to interact with the user
def main():
    print("Welcome to the Triangle Area Calculator using Circumradius!")
    print("This program calculates the area of an equilateral triangle given its circumradius.")
    print()

    # Taking input from the user for the circumradius
    R = float(input("Enter the circumradius of the equilateral triangle: "))

    # Calculating the area by calling the function
    area = calculate_triangle_area_circumradius(R)

    # Displaying the calculated area
    print(f"The area of the equilateral triangle with circumradius {R} is: {area}")

# Calling the main function to run the program
if __name__ == "__main__":
    main()
