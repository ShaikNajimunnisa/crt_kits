#D D D D C C C C B B B B A A A A 

n = int(input('Enter the letter: '))
for i in range(n,0,-1):
    for j in range(1,n+1):
        print(chr(i+64), end="")
    print()