#revenue
n=7
#Revenue=[]
#for i in range(n):
    #ele=int(input(f"Enter the revenue for day {i+1} :"))
    #Revenue.append(ele)
   # print(f"Total Revenue :{sum(Revenue)} | Best Day :{max(Revenue)} | Worst Day :{min(Revenue)}")
          
#or
Revenue=list(map(int,input("Enter the Revenue for 7 days :").split()))
print(f"Total Revenue :{sum(Revenue)} | Best Day : {max(Revenue)} | Worst Day: {min(Revenue)} ")