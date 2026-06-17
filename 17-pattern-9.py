n = int(input('Enter n: '))
for i in range(1, n + 1):
    square_of_i = i * i
    for j in range(n):
        print(square_of_i, end=" ")
    print()