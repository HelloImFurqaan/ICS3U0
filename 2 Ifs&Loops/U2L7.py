import math

print("%3s|%5s|%7s|%5s" % ("N", "SQR", "Cubes", "Roots"))
print("---+-----+-------+-----")
for n in range(10, 200, 15):
  sqr = math.pow(n, 2)
  cube = math.pow(n, 3)
  root = math.sqrt(n)
  print("%3d|%5d|%7d|%5.2f" % (n, sqr, cube, root))
