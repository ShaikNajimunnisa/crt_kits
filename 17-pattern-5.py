n = int(input('Enter n: '))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i % 2 == 1:        # odd row
            print(i, end=" ")
        else:                 # even row
            print("*", end=" ")
    print()