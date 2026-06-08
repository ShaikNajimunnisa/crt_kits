class Product:
    def __init__(self, name, price):
        print("Product object is created...!")
        self.name = name
        self.price = price
        print("-----------------------------------")

P1 = Product('Phone', 2000)
print(f"name={P1.name}")
print(f"price={P1.price}")