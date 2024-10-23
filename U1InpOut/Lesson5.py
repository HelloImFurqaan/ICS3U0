import math
radius = input("Input the radius: ")
radius = float(radius)
area = 0.5*math.pi*math.pow(radius, 2) + 4*math.pow(radius, 2)
print("The area of the Norman Window is:", area)
