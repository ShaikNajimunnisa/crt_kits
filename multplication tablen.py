#Q) write a python program to print multiplication table of n.
num=int(input("Enter a number: "))
print(f"multiplication table of {num}: ")
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")