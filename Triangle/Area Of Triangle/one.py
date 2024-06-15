# This program calculates the area of a triangle using base and height.

# Function to calculate the area of a triangle
def calculate_triangle_area(base, height):
    area = 0.5 * base * height  # Formula for area of triangle
    return area

# Main function to interact with the user
def main():
    print("Welcome to the Triangle Area Calculator!")
    print("This program calculates the area of a triangle given its base and height.")
    print()

    # Taking input from the user for base and height
    base = float(input("Enter the base length of the triangle: "))
    height = float(input("Enter the height of the triangle: "))

    # Calculating the area by calling the function
    area = calculate_triangle_area(base, height)

    # Displaying the calculated area
    print(f"The area of the triangle with base {base} and height {height} is: {area}")

# Calling the main function to run the program
if __name__ == "__main__":
    main()
