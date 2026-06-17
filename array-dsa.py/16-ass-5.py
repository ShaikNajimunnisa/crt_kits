#2,3,5,7,11,13,17,19,23,.....n--pattern
n = int(input('Enter n: '))
for num in range(2, n + 1):
    if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
        print(num, end=' ')