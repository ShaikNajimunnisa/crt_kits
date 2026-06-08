#2.write a python program to read 3 integer values and find the smallest no.

num1=int(input("Enter a number1: "))
num2=int(input("Enter a number2: "))
num3=int(input("Enter a number3: "))
if(num1<=num2 and num1<=num3):
    print(f"{num1} is the smallest number.") 
elif(num2<=num1 and num2<=num3):
    print(f"{num2} is the smallest number.")
else:
    print(f"{num3} is the smallest number.")
    