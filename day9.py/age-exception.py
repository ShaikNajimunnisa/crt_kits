age=int(input('Enter the age : '))
if(age>=18):
    print('Eligible to vote')
else:
    raise Exception('Not Eligible to vote')  