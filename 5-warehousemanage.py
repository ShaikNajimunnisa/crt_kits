godownA=list(map(str,input("enter the product codes: ").split()))
godownB=list(map(str,input("enter the product codes: ").split()))
print(f"Unified inventory: ' ,set(godownA+godownB()) | total : len()")
