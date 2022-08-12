myArray = [1, 2, -1, 1, 0, 1, 2, -1, -1, -2]
x = -1
y = 0

for i in range(0, len(myArray), 2):
    x = x + myArray[i]
    y = y + myArray[i + 1]
for i in range(0, 4):
    for j in range(0, 4):
        if i == x and j == y:
            print('X', end="")
        else:
            print('O', end="")
    print()
