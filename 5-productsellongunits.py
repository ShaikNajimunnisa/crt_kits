price=list(map(int,input("Enter the prices: ").split()))
print(sorted(price,reverse=True)[:3])
