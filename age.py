#Q)write a python program to read age as input  from the user and check whether the age is valid to vote or not.
age=int(input("Enter your age: "))
if(age>=18):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
    #ternary operator
    res="eligible" if age>=18 else "not eligible"
    print("You are" ,res, "to vote.")
    
