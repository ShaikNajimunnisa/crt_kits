ifsc = input()

if len(ifsc) == 11 and ifsc[:4].isalpha() and ifsc[4] == '0' and ifsc[5:].isalnum():
    print("Valid IFSC Code")
else:
    print("Invalid IFSC Code")
    
        
    