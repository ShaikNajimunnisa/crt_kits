#Q) write a python program to find the summation of each digit in the number.
num=int(input("Enter the number : "))
sum=0
rem=0
while(num!=0):
    rem=num%10
    sum=sum+rem
    num=num//10
print(f"sum of digits is{sum}")
'''rem=25%10----->5
sum=0+5
num=2

rem=2%10----->2
sum=5+2
num =0
'''