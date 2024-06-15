# Function to calculate perimeter using lengths of sides
def perimeter_sides(a, b, c):
    perimeter = a + b + c  # Calculate the perimeter
    return perimeter  # Return the perimeter

# Example usage:
if __name__ == "__main__":
    # Input the lengths of the sides of the triangle
    side_a = float(input("Enter the length of side a: "))
    side_b = float(input("Enter the length of side b: "))
    side_c = float(input("Enter the length of side c: "))

    # Calculate the perimeter using the function
    perimeter = perimeter_sides(side_a, side_b, side_c)

    # Print the result
    print(f"The perimeter of the triangle with sides {side_a}, {side_b}, {side_c} is: {perimeter}")
