# try
S = "#"
for i in range(10, 0, -1):
    print(S * i)

# MODIFY 2
S = "#"
spaces = 4
for i in range(1, 10, 2):
    print(" " * spaces, S * i)
    spaces -= 1

# MODIFY 3
S = "#"
spaces = 5
for i in range(1, 12, 2):
    print(" " * spaces, S * i)
    spaces -= 1
spaces = 1
for i in range(9, 0, -2):
    print(" " * spaces, S * i)
    spaces += 1
