import random as rd

size = int(input("Enter tree size: "))
for i in range(1, size + 1):
    print((" " * (size - i)), end="")
    for j in range(i * 2 - 1):
        if rd.randint(1, 4) == 1:
            print("o", end="")
        else: 
            print("^", end="")
    print()

for i in range(0, size, 2):
    print((" " * (size - 1)) + "#")