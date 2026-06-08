#nested fun:
def one():
    def two():
        print("Two")
    print("One")
one()