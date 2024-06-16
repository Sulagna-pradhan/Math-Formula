# Function to calculate Semi-perimeter of a triangle using Trigonometry (Sine Rule)

import math

def semiperimeter_sine_rule(a, b, angle_C_degrees):
    angle_C_radians = math.radians(angle_C_degrees)
    c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(angle_C_radians))
    return (a + b + c) / 2

# Example usage:
if __name__ == "__main__":
    # Input the lengths of sides a and b, and the angle C in degrees
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    angle_C = float(input("Enter the angle C in degrees: "))

    # Calculate the semiperimeter
    s = semiperimeter_sine_rule(a, b, angle_C)

    # Print the result
    print(f"The semiperimeter of the triangle with sides {a}, {b}, and angle C {angle_C} degrees is: {s}")
