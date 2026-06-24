size = int(input("size: "))
for i in range(1, size + 1):
    print((" " * (size - i)) + ("^" * (i * 2 - 1)))

for i in range(0, size, 2):
    print((" " * (size - 1)) + "#")