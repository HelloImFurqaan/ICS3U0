import math

x = input("Please input a whole number: ")
x = int(x)
y = input("Please input another nonzero whole number")
y = int(y)
print("Now deciding if", y, "is a factor of", x, "...")
if (y != 0):
  rem = x % y
  if rem == 0:
    print("Yes!", y, "is a factor of", x)
#MODIFY 2
import math

x = input("Please input a whole number: ")
x = int(x)
y = input("Please input another nonzero whole number")
y = int(y)
print("Now deciding if", y, "is a factor of", x, "...")
if (y != 0):
  rem = x % y
  if rem == 0:
    print("Yes!", y, "is a factor of", x)
  else:
    print(y, "is not a factor of", x)
else:
  print("0 is not a valid input, factor could not be determined.")
#MODIFY 3
import math

x = input("Please input a whole number between 1 and 20: ")
x = int(x)
if (x >= 1 and x <= 20):
  y = input("Please input another whole number between 1 and 20: ")
  y = int(y)
  if (y >= 1 and y <= 20):
    rem = x % y
    if rem == 0:
      print("Yes!", y, "is a factor of", x)
    else:
      print(y, "is not a factor of", x)
  else:
    print("OUT OF RANGE.")
else:
  print("OUT OF RANGE.")
