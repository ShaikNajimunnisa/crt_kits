n = int(input('Enter rows: '))
for i in range(n):
    if i % 2 == 0:  # even rows: letters
        letter = chr(65 + i)  # 65 = 'A'
        print((letter + ' ') * n)
    else:  # odd rows: *
        print(('* ' * n))