
#Q)write a python program to read the month no as a input from the user and check whether it is valid  month no or not.
month=int(input("Enter month number: "))
if(month>=1 and month<=12):
    print(month ," is valid.")
else:
    print(month ," is  invalid.")