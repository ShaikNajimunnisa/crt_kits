    #Q)write a python program as a input from the user and check whether it is +ve or -ve or 0.
num=int(input("Enter a number: "))
if(num>0):
    print(f"{num} is positive.")    
elif(num<0):
    print(f"{num} is negative.")
else:
    print(f"{num} is zero.")