# Function to calculate Semi-perimeter of a triangle using Coordinates of Vertices

import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def semiperimeter_coordinates(x1, y1, x2, y2, x3, y3):
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3, x1, y1)
    return (a + b + c) / 2

# Example usage:
if __name__ == "__main__":
    # Input the coordinates of the vertices of the triangle
    x1, y1 = map(float, input("Enter the coordinates of vertex 1 (x1 y1): ").split())
    x2, y2 = map(float, input("Enter the coordinates of vertex 2 (x2 y2): ").split())
    x3, y3 = map(float, input("Enter the coordinates of vertex 3 (x3 y3): ").split())

    # Calculate the semiperimeter
    s = semiperimeter_coordinates(x1, y1, x2, y2, x3, y3)

    # Print the result
    print(f"The semiperimeter of the triangle with vertices ({x1}, {y1}), ({x2}, {y2}), ({x3}, {y3}) is: {s}")
