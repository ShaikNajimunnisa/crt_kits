#product e-commerce 
Price=list(map(int,input('Enter the Prices : ').split()))
new_list=[]
#print([i for  i in price if i>1000])
for i in Price:
    if i>1000:
        new_list.append(i)
print(new_list)

#or 
Price=list(map(int,input('Enter the Prices :').split()))
print([i for i in Price if i>1000])