print("Make a choice from the following menu: ")
print("A: apples")
print("B: bananas")
print("C: cherries")

ch = input("Your choice: ")

if (ch == "A"):
    print("I prefer apples")
elif (ch == "B"):
    print("I prefer bananas")
elif:
    print("I prefer cherries")
else:
    print("Unexpected input.")

#MODIFY 2

num = int(input("Input a number from 1-100"))

if (num <= 100) and (num >= 80):
  print("A")
elif (num < 80) and (num >= 70):
  print("B")
elif (num < 70) and (num >= 60):
  print("C")
elif (num < 60) and (num >= 50):
  print("D")
elif (num < 50) and (num >= 1):
  print("F")
else:
  print("Invalid input.")
