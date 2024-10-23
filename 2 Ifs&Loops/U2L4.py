# 1

fac = int(input("Input the factorial:"))
pr = fac
x = fac
while(x != 1):
    x -= 1
    fac *= x
print("%d! =" % pr, fac)

# 2

fac = int(input("Enter a value for the upper limit, n:"))
count = 0
wha = 1
while(count < fac):
    count += 1
    x = count
    wha *= x
    print("%d! =" % count, wha)

# 3

fac = int(input("Enter a value for the upper limit, n:"))
count = 0
wha = 1
if (fac == 0):
  print("0! = 1")
else:
  print("0! = 1")
  while(count < fac):
    count += 1
    x = count
    wha *= x
    print("%d! =" % count, wha)
