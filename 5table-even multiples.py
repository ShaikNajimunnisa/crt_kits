#Q)write a python program to print the multiplication of table 5 with only even multiples.
for i in range(2, 11, 2):
    print(f"5 x {i} = {5*i}")
              #or
for i in range(1, 11):
    if(i==5):
        continue #break
    print(i)