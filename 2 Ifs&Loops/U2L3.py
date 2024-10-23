count = 9
while (count != 0):
    print(count)
    count -= 1
# Start at 9 and end at 1
count = 9
while (count != 0):
    count -= 1
    print(count)
# Start at 8 and end at 0

# Part B

count = 0
trinum = 0
while (count != 6):
  count += 1
  trinum = trinum + count
  if (count == 1):
    print("The %dst triangular number is" % count, trinum)
  elif (count == 2):
    print("The %dnd triangular number is" % count, trinum)
  elif (count == 3):
    print("The %drd triangular number is" % count, trinum)
  else:
    print("The %dth triangular number is" % count, trinum)
