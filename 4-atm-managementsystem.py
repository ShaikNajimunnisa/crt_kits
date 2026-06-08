#ATM MANAGEMENT SYSTEM
pin=int(input("Enter the pin:"))
acc_bal=0
if(pin==1234):
    print("Welcome to bank")
    #Deposite, Withdrawl, Balance Inquery, Exit.
while True:    
    print("1. Deposit")
    print("2. Withdrawl")
    print("3. Balance Inquery")
    print("4. Exit")
    
    choice=int(input("Enter the  choice :"))
    print("\n")
    if(choice==1):
        amount=int(input("Enter the amount to deposit:"))
        acc_bal=acc_bal+amount
        print(f"Dear Customer yourn account xxxxxxxxxxxx1234 is credited with {amount}")
    elif(choice==2):
        amount=int(input("Enter the amount to withdraw:"))
        if(amount<acc_bal):
            print(f"Dear Customer yourn account xxxxxxxxxxxx1234 is debited with {amount}")
            acc_bal=acc_bal-amount
        else:
            print("Insufficient balance............")
    elif(choice==3):
        print(f"Dear Customer your account xxxxxxxxxxxx1234 has balance {acc_bal}")
    else:
        print("Thank you")
        break
else:
    print("Entered wrong pin ")     