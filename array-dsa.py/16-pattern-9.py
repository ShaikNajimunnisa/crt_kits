#a a a a a a a * * * * * * * c c c c c c c 
n = int(input('Enter rows: '))
for i in range(n):
    if i % 2 == 0:  # even rows: letters
        letter = chr(97 + i)  # 97 = 'a'
        print((letter + ' ') * n)
    else:  # odd rows: *
        print(('* ' * n))