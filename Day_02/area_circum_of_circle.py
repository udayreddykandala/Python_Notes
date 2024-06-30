# Calculate the area and circumference of a circle given its radius

import math

# Prompt the user to enter the radius
radius = float(input("Enter the radius of the circle: "))

# Calculate the area
area = math.pi * radius * radius

# Calculate the circumference
circumference = 2 * math.pi * radius

# Print the results
print(f"The area of the circle is {area:.2f}")
print(f"The circumference of the circle is {circumference:.2f}")
