# Function to calculate perimeter using Sine Rule
import math

def perimeter_sine_rule(a, b, angle_C_degrees):
    # Convert angle from degrees to radians
    angle_C_radians = math.radians(angle_C_degrees)
    
    # Calculate side c using Sine Rule: c / sin(C) = a / sin(A) = b / sin(B)
    c = (a * math.sin(angle_C_radians)) / math.sin(math.pi - angle_C_radians)
    
    # Calculate perimeter
    perimeter = a + b + c
    
    return perimeter

# Example usage:
if __name__ == "__main__":
    # Input the lengths of sides a and b, and the angle C in degrees
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    angle_C = float(input("Enter the angle C in degrees: "))

    # Calculate the perimeter using the function
    perimeter = perimeter_sine_rule(a, b, angle_C)

    # Print the result
    print(f"The perimeter of the triangle with sides {a}, {b} and angle C {angle_C} degrees is: {perimeter}")
