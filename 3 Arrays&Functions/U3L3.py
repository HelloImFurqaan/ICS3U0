items = ["Apples", "Bananas", "Cherries", "Dosa"]
sizes = []
check = []

for i in range(len(items)): 
  sizeI = len(items[i])
  sizes.append(sizeI)

for i in range(len(sizes)):
  if sizes[i] == len(items[i]):
    check.append(True)
  else:
    check.append(False)

for i in range(len(sizes)):
  print("%d | %8s | %s" % (sizes[i], items[i], check[i]))
