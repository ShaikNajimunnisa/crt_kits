#Q) write a program reverse to print multiplication table.
num=int(input("Enter a number: "))
print(f"multiplication table of {num}: ")
for i in range(10,0,-1):
    print(f"{num} x {i} = {num*i}")