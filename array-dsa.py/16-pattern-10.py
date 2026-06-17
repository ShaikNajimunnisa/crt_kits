n = int(input('Enter n: '))
for i in range(n):  # n rows
    for j in range(n):  # n columns
        if j % 2 == 0:  # even column: letter
            print(chr(97 + j), end=' ')
        else:  # odd column: *
            print('*', end=' ')
    print()