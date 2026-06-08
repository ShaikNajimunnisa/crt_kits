#mobile class
class mobile:
    def __init__(brand, self, price, color):
        print("Mobile object is created...!")
        self.brand = brand
        self.price = price
        self.color = color

def details(self):
    print("-----------------------------------")
    print(f"brand is {self.brand}")
    print(f"price is {self.price}")
    print(f"color is {self.color}")

s1 = mobile('vivo', '25000', 'Blue')
s1.details()

s2 = mobile('oppo',' 20000', 'pink')
s2.details()

s3 = mobile('Redmi', '35000', 'sea green')
s3.details()

s4 = mobile('1+', '30000', 'red')
s4.details()

s5 = mobile('apple', '50000', 'white')
s5.details()