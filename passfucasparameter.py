def one(xyz):
    print("First Function"+xyz())
def two():
    return "Second Function" # is created to give as a parameter to the 1st func
one(two)