def add(a, b):
  return a + b
done = False
while (done == False):
  try:
    num1 = float(input("Input a number:"))
    num2 = float(input("Input another number:"))
    print(add(num1, num2))
    done = True
  except:
    print("Error. Input valid numbers.")

#MODIFY 2

import math
def myPow(m, n):
  return m**n
  
base = float(input("Input a base number:"))
power = float(input("Input a power:"))

print("myPow: ", myPow(base, power))
print("math.pow: ", math.pow(base, power))
