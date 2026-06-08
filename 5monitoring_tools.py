data=list(map(int,input("enter the HTTP codes: ").split()))
Last_Five=data[-5:]
print(f"Last_Five records: {Last_Five} | critical error found: :{True if 500 in Last_Five else Flase}")