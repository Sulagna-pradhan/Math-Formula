# This program calculates the area of a triangle using Heron's formula.

import math  # Importing math module for square root function

# Function to calculate the area of a triangle using Heron's formula
def calculate_triangle_area(a, b, c):
    # Calculate semi-perimeter
    s = (a + b + c) / 2
    
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return area

# Main function to interact with the user
def main():
    print("Welcome to the Triangle Area Calculator using Heron's formula!")
    print("This program calculates the area of a triangle given its three sides.")
    print()

    # Taking input from the user for the sides of the triangle
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))

    # Calculating the area by calling the function
    area = calculate_triangle_area(a, b, c)

    # Displaying the calculated area
    print(f"The area of the triangle with sides {a}, {b}, {c} is: {area}")

# Calling the main function to run the program
if __name__ == "__main__":
    main()
