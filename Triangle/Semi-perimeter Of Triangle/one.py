# Function to calculate Semi-perimeter of a triangle using lengths of sides

def semiperimeter_sides(a, b, c):
    return (a + b + c) / 2

# Example usage:
if __name__ == "__main__":
    # Input the lengths of the sides of the triangle
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))

    # Calculate the semiperimeter
    s = semiperimeter_sides(a, b, c)

    # Print the result
    print(f"The semiperimeter of the triangle with sides {a}, {b}, {c} is: {s}")
