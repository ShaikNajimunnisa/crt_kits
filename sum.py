#Q)write a python program to calculate sum of n natural numbers.
num = int(input("Enter a number: "))
sum = 0
for i in range(1, num + 1):
    sum = sum + i
print(" The sum of first", num, " numbers is:", sum)    