#Q)write a python  program to print the factorial of n. 
num = int(input("Enter a number: "))
fact = 1 
for i in range(1, num + 1):
    fact = fact * i
    print("The fact of", num, "is", fact) 
    