#4.write a python program to read 3 integer values and find the middle no.
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
if(a<b and a>c):
    print(f"{a} is the middle number.")
elif(b<a and b>c):
    print(f"{b} is the middle number.")
else:
    print(f"{c} is the middle  number.")