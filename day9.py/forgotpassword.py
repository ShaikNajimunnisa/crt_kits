pin=input('Enter the password : ')
try:
    if(pin=='2001'):
        print('Logic is Successful')
    else:
        raise TypeError('Incorrect Password')  
except  TypeError as e:
    print(e) 