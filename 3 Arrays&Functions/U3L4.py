ar2 = [[3, 4, 1, 2, 6],
      [9, 2, 3, 7, 5],
      [4, 2, 1, 0, 3]]
ar4 = []
for i in range(len(ar2)):
  sums = 0
  ar3 = ar2[i]
  for j in range(len(ar3)):
      print(ar3[j], end=" ")
      sums += ar3[j]
  ar4.append(sums)
  print()

print(ar2)
print()
print(ar4)
