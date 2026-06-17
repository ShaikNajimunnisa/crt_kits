n = int(input('Enter rows: '))  # how many rows
cols = 4  # 4 numbers per row

for i in range(1, n + 1):
    num = 2 * i   # 2, 4, 6, 8, ...
    for j in range(cols):
        print(num, end=" ")
    print()