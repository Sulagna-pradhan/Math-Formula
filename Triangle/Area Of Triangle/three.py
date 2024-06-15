# This program calculates the area of a triangle using side length and altitude (height).

# Function to calculate the area of a triangle using side and altitude
def calculate_triangle_area_with_altitude(side, altitude):
    # Calculate the area using the formula: Area = 0.5 * base * height
    area = 0.5 * side * altitude
    return area

# Main function to interact with the user
def main():
    print("Welcome to the Triangle Area Calculator using Side and Altitude!")
    print("This program calculates the area of a triangle given its side length and altitude.")
    print()

    # Taking input from the user for side length and altitude
    side = float(input("Enter the length of a side of the triangle: "))
    altitude = float(input("Enter the altitude (height) corresponding to the side: "))

    # Calculating the area by calling the function
    area = calculate_triangle_area_with_altitude(side, altitude)

    # Displaying the calculated area
    print(f"The area of the triangle with side length {side} and altitude {altitude} is: {area}")

# Calling the main function to run the program
if __name__ == "__main__":
    main()
