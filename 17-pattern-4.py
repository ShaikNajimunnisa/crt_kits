n = int(input())

s = ""
odd = 1

for i in range(1, n + 1):
    if i % 2 == 1:
        s += str(odd)
        odd += 2
    else:
        s += "*"
    
    print(s)