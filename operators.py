x=10
y=3
print(f"Addition of x & y is {x+y}")
print(f"Subtraction of x & y is {x-y}")
print(f"Multiplication of x & y is {x*y}")
print(f"Division of x & y is {x/y}")
print(f"Modulo Division of x & y is {x%y}")
print(f"Positive Floor Division of x & y is {x//y}")
print(f"Negative Floor Division of x & y is {-x//y}")

#relational operaters
print(10>15)
print(10<15)
print(10>=15)
print(10<=15)
print(10==15)
print(10!=15)
#3.Assignment 
num=10
print(f"num = {num}")
num+=2 #num=num+2
print(f"num = {num}")
num-=4
print(f"num = {num}")
num*=10
print(f"num = {num}")
num/=10
print(f"num = {num}")
num%=10
print(f"num = {num}")
num**=10
print(f"num = {num}")
num//=10
print(f"num = {num}")
#4:logical operaters
num=10
print(num>5 and num<15)
print(num>5 or num<5)
print(not(num<15))

#5: bitwise operater
a=10
b=15
print(a & b)
print(a | b)
#6:bitwise operater
a=10
b=15
print('~a=',~a)
print('a&b=',a&b)
print('a|b=',a|b)
print('a^b=',a^b) #bitwise xor(-operation)
print('a<<2=',a<<2)
print('a>>2=',a>>2)

#membership operater
list1=[10,20,30,25,40,15]
print(10 in list1)#True
print(50 in list1)#False
print(10 not in list1)   #False
print(50 not in list1)  #True
print("Python" in "i am  working on python")  #True
print("Python" not in "i am  working on python")  #False

#identity operator
num1=10
print(num1)
print(id(num1))
num2=10
print(num2)
print(id(num2))
print(num1 is num2)