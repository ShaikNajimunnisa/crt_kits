#Allow customers to order multiple pizzas in a single order.
size_price = {"small": 10, "medium": 15, "large": 20}
topping_price = {"cheese": 2, "pepperoni": 3, "olives": 5, "jalapenos": 5}

num_pizzas = int(input("enter number of pizzas: "))
order_total = 10

for p in range(1, num_pizzas + 1):
    print(f"\nPizzas {p}:")
    size = input("enter the size of pizzas: ")
    n = int(input("enter the number of toppings: "))

    pizzas_total = size_price[size] # base price

    for i in range(n):
        topping = input("enter your topping: ")
        pizzas_total += topping_price[topping]

    order_total += pizzas_total
    print(f"Pizzas {p} subtotal: ${pizzas_total}")

# delivery charge logic
if order_total < 50:
    delivery = 5
else:
    delivery = 0

grand_total = order_total + delivery

print("\n--- Bill ---")
print("Order value: $", order_total)
print("Delivery charge: $", delivery)
print("Total bill: $", grand_total)