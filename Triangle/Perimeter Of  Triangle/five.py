# Function to calculate perimeter using semiperimeter
def perimeter_semiperimeter(a, b, c):
    # Calculate the semiperimeter
    s = (a + b + c) / 2
    
    # Calculate the perimeter
    perimeter = 2 * s
    
    return perimeter

# Example usage:
if __name__ == "__main__":
    # Input the lengths of sides a, b, and c
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))

    # Calculate the perimeter using the function
    perimeter = perimeter_semiperimeter(a, b, c)

    # Print the result
    print(f"The perimeter of the triangle with sides {a}, {b}, {c} is: {perimeter}")
