# 5.Create a function that accepts a varying number of items, each represented as a dictionary containing an item's name and price. The function should return the total cost of the items.
# Use Case: This can be used in an e-commerce platform where customers can add any number of items to their shopping cart.

def calculate_total_cost(*args):
    total_cost = 0
    for item in args:
        total_cost += item['price']
    return total_cost

items = []
while True:
    name = input("Enter the item name (or type 'done' to finish): ")
    if name.lower() == 'done':
        break
    price = float(input(f"Enter the price for {name}: "))
    items.append({'name': name, 'price': price})

total_cost = calculate_total_cost(*items)
print(items)
print(f"The total cost of the items is ${total_cost:.2f}")

