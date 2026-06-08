class Product:
    def __init__(self, name, age):
        print("Student object is created...!")
        self.name = name
        self.age = age

    def details(self):
        print("-----------------------------------")
        print(f"name is {self.name}")
        print(f"age is {self.age}")

s1 = Product('scoot', 23)
s1.details()

s2 = Product('aline', 26)
s2.details()

s3 = Product('samee', 29)
s3.details()

s4 = Product('Meera', 30)
s4.details()

s5 = Product('Munni', 32)
s5.details()