#3.write a python program to check whether the user entered integer is a palindrome or not.
num = int(input("Enter an integer: "))
if str(num) == str(num)[::-1]:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")