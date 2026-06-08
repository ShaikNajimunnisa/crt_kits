#HDFC-OTP
str='Your HDFC  Bank OTP is 748291 valid for 10 minutes'
print(f"OTP extracted: {str[22:29]}" ) 

#or
a = list(map(str,input().split()))
for i in a:
    if i.isdigit():
        print(i)