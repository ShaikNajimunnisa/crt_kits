# Pizza ordering system: choose size and toppings, then show total bill.
size_price = {"small": 10, "medium": 15, "large": 20}
topping_price = {"cheese": 2, "pepperoni": 3, "olives": 5, "jalapenos": 5}

size = input("enter the size of pizza: ")
n = int(input("enter the number of toopings: "))

total = size_price[size] # add base price

for i in range(n):
    topping = input("enter your topping: ")
    total += topping_price[topping]

print("Total bill: $", total)


#or
size_price = {"small": 10, "medium": 15, "large": 20}
topping_price = {"cheese": 2, "pepperoni": 3, "olives": 5, "jalapenos": 5}

size = input("enter the size of pizza: ")
n = int(input("enter the number of toopings: "))

# base price
total = size_price[size]

# add each topping price
toppings = [input("enter your topping: ") for _ in range(n)]
total += sum(topping_price[t] for t in toppings)

print("Total bill: $", total)