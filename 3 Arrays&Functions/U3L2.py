items = []
itemnum= int(input("How many items are you entering? "))
print("Enter your items now: ")
for x in range(itemnum):
  items.append(input("Next item: "))
print("You have entered %d items." % itemnum)
for item in items:
  print(item)
