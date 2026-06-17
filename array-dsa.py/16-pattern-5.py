#d c b a
n = int(input('Enter the value: '))
for i in range(n):
    for j in range(n-1, -1, -1):
        print(f"{chr(97 + j)} ", end="")
    print()