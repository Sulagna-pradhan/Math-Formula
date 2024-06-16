""" The Pythagorean Theorem relates the lengths of the sides in a right-angled triangle. The theorem states that in a right-angled triangle, the square of the length of the hypotenuse
c is equal to the sum of the squares of the lengths of the other two sides """


import math

# Function to calculate the hypotenuse given sides a and b
def calculate_hypotenuse(a, b):
    c = math.sqrt(a**2 + b**2)  # Calculate the hypotenuse using Pythagorean Theorem
    return c  # Return the hypotenuse

# Function to calculate a side given the hypotenuse and the other side
def calculate_side(c, a_or_b):
    b_or_a = math.sqrt(c**2 - a_or_b**2)  # Calculate the other side using Pythagorean Theorem
    return b_or_a  # Return the calculated side

# Example usage:
if __name__ == "__main__":
    # Choose the type of calculation
    print("Choose the calculation type:")
    print("1: Calculate the hypotenuse (c) given sides a and b")
    print("2: Calculate a side (a or b) given the hypotenuse (c) and the other side (a or b)")
    choice = int(input("Enter 1 or 2: "))

    if choice == 1:
        # Input the lengths of sides a and b
        a = float(input("Enter the length of side a: "))
        b = float(input("Enter the length of side b: "))

        # Calculate the hypotenuse
        hypotenuse = calculate_hypotenuse(a, b)

        # Print the result
        print(f"The hypotenuse of the right-angled triangle with sides {a} and {b} is: {hypotenuse}")

    elif choice == 2:
        # Input the length of the hypotenuse and one side
        c = float(input("Enter the length of the hypotenuse (c): "))
        a_or_b = float(input("Enter the length of the other side (a or b): "))

        # Calculate the other side
        other_side = calculate_side(c, a_or_b)

        # Print the result
        print(f"The length of the other side of the right-angled triangle with hypotenuse {c} and side {a_or_b} is: {other_side}")

    else:
        print("Invalid choice. Please enter 1 or 2.")








# EXPLANATION - 
"""
Function Definition (calculate_hypotenuse):
his function calculate_hypotenuse takes two parameters a and b, which are the lengths of the two sides of a right-angled triangle.
It calculates the hypotenuse c using the Pythagorean Theorem: 
It returns the calculated hypotenuse c.

Function Definition (calculate_side):
This function calculate_side takes two parameters c (the hypotenuse) and a_or_b (one of the other sides).
It calculates the other side b_or_a using the Pythagorean Theorem: 
It returns the calculated side b or a.
"""