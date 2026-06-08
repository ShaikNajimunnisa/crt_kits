num=int(input("Enter the number : "))
count=0
rem=0
while(num!=0):
    rem=num%10
    count+=1 #count=count+1
    num=num//10
print(f"count of digits is{count}")