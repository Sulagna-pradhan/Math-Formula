# Function to calculate perimeter using Coordinates of Vertices

import math

# Function to calculate distance between two points (vertices)
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Function to calculate perimeter using coordinates of vertices
def perimeter_coordinates(x1, y1, x2, y2, x3, y3):
    # Calculate distances between vertices
    side_a = distance(x1, y1, x2, y2)
    side_b = distance(x2, y2, x3, y3)
    side_c = distance(x3, y3, x1, y1)
    
    perimeter = side_a + side_b + side_c  # Calculate the perimeter
    
    return perimeter  # Return the perimeter

# Example usage:
if __name__ == "__main__":
    # Input the coordinates of the vertices of the triangle
    x1, y1 = map(float, input("Enter the coordinates of vertex 1 (x1 y1): ").split())
    x2, y2 = map(float, input("Enter the coordinates of vertex 2 (x2 y2): ").split())
    x3, y3 = map(float, input("Enter the coordinates of vertex 3 (x3 y3): ").split())

    # Calculate the perimeter using the function
    perimeter = perimeter_coordinates(x1, y1, x2, y2, x3, y3)

    # Print the result
    print(f"The perimeter of the triangle with vertices ({x1}, {y1}), ({x2}, {y2}), ({x3}, {y3}) is: {perimeter}")
