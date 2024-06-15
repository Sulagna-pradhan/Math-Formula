# This program calculates the area of a triangle using Trigonometry (Sine Rule).

import math  # Importing math module for sine function

# Function to calculate the area of a triangle using Sine Rule
def calculate_triangle_area_sine_rule(a, b, angle_C_degrees):
    # Convert angle from degrees to radians
    angle_C_radians = math.radians(angle_C_degrees)
    
    # Calculate the area using the formula: Area = 0.5 * a * b * sin(C)
    area = 0.5 * a * b * math.sin(angle_C_radians)
    return area

# Main function to interact with the user
def main():
    print("Welcome to the Triangle Area Calculator using Trigonometry (Sine Rule)!")
    print("This program calculates the area of a triangle given two sides and the included angle.")
    print()

    # Taking input from the user for the sides and included angle
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    angle_C_degrees = float(input("Enter the measure of angle C in degrees: "))

    # Calculating the area by calling the function
    area = calculate_triangle_area_sine_rule(a, b, angle_C_degrees)

    # Displaying the calculated area
    print(f"The area of the triangle with sides {a}, {b} and angle C {angle_C_degrees} degrees is: {area}")

# Calling the main function to run the program
if __name__ == "__main__":
    main()
