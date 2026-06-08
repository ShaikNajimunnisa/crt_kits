#Q) write a python program to  print reversed multiplication tables from 1 to n.
num = int(input("Enter a number: "))
for i in range(1, num + 1): 
    print(f"multiplication table of {i}: ")
    print("------------------------------------")
    for j in range(10, 0, -1):
        print(f"{i} x {j} = {i*j}")