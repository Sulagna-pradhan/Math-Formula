# This program calculates the area of a triangle using coordinates of its vertices.

import math  # Importing math module for absolute value function

# Function to calculate the area of a triangle using coordinates
def calculate_triangle_area(x1, y1, x2, y2, x3, y3):
    # Calculate the area using the formula: Area = 0.5 * |x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)|
    area = 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
    return area

# Main function to interact with the user
def main():
    print("Welcome to the Triangle Area Calculator using Coordinates of Vertices!")
    print("This program calculates the area of a triangle given the coordinates of its vertices.")
    print()

    # Taking input from the user for coordinates of the vertices
    x1, y1 = map(float, input("Enter coordinates of vertex 1 (x1 y1): ").split())
    x2, y2 = map(float, input("Enter coordinates of vertex 2 (x2 y2): ").split())
    x3, y3 = map(float, input("Enter coordinates of vertex 3 (x3 y3): ").split())

    # Calculating the area by calling the function
    area = calculate_triangle_area(x1, y1, x2, y2, x3, y3)

    # Displaying the calculated area
    print(f"The area of the triangle with vertices ({x1}, {y1}), ({x2}, {y2}), ({x3}, {y3}) is: {area}")

# Calling the main function to run the program
if __name__ == "__main__":
    main()
