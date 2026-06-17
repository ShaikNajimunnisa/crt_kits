n = int(input('Enter rows: '))  # how many rows
cols = 4  # 4 numbers per row

for i in range(n):
    num = 2 * i + 1   # 1, 3, 5, 7, ...
    for j in range(cols):
        print(num, end=" ")
    print()
