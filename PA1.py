"""
Furqaan Mohammed 752879
Date: 1 October, 2024
Course: ICS3U0-Introduction to Computer Science
Title: Three-Part Python Output with Math
Description: A program which performs four different calculations with input from the user.
VARIABLE DICTIONARY: 
  w           (float) Width of the rectangle.
  l           (float) Length of the rectangle (also used as the length of the pendulum).
  a           (float) Area (used for both rectangle and circle).
  r           (float) Radius (used for both the circle and the cylinder).
  h           (float) Height of the cylinder.
  s           (float) Surface area of the cylinder.
  v           (float) Volume of the cylinder.
  g           (float) Gravitational acceleration constant
  p           (float) Period of the pendulum.
"""

import math as m

# Calculate the area of a rectangle
print("Calculate the area of a rectangle.")
w = input("Input the width of the rectangle: ")  # Input width
l = input("Input the length of the rectangle: ")  # Input length
w = float(w)  # Convert width to a floating-point number
l = float(l)  # Convert length to a floating-point number
a = w * l  # Calculate area
print("The area of the rectangle is: %.2f" % a)  # Print the area formatted to 2 decimal places
print(" ")

# Calculate the area of a circle
print("Calculate the area of a circle.")
r = input("Input the radius of the circle: ")  # Input radius
r = float(r)  # Convert radius to a floating-point number
r = m.pow(r, 2)  # Square the radius 
a = r * m.pi  # Calculate area 
print("The area of the circle is: %.2f" % a)  # Print the area formatted to 2 decimal places
print(" ")

# Calculate the surface area and volume of a cylinder
print("Calculate the surface area and volume of a cylinder.")
h = input("Input the height of the cylinder: ")  # Input height
h = float(h)  # Convert height to a floating-point number
r = input("Input the radius of the cylinder: ")  # Input radius
r = float(r)  # Convert radius to a floating-point number
s = 2 * m.pi * r * h 
r = m.pow(r, 2)  # Square the radius
s = s + 2 * m.pi * r  # Calculate suface area
v = m.pi * r * h  # Calculate volume 
print("The surface area of the cylinder is: %.2f" % s)  # Print the surface area formatted to 2 decimal places
print("The volume of the cylinder is: %.2f" % v)  # Print the volume formatted to 2 decimal places
print(" ")

# Calculate the period of a pendulum
print("Calculate the period of a pendulum.")
l = input("Input the length of the pendulum (in meters): ")  # Input pendulum length
l = float(l)  # Convert length to a floating-point number
g = 9.8 
p = 2 * m.pi * m.sqrt(l / g)  # Calculate period
print("The period of the pendulum is: %.2f seconds." % p)  # Print the period formatted to 2 decimal places
print(" ")

# End of program
print("All calculations have been completed. Thank you for running the program!")
