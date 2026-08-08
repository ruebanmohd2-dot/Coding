items = ["Pencil", "Eraser", "Notebook", "Sharpener", "Glue"]
stock = [12, 0, 8, 5, 3]

inventory = dict(zip(items, stock))
print(inventory)

availableitems = [item for item in items if inventory[item] > 0]
print("Available items:", availableitems)

chosen_item = input("Enter an item: ")

if inventory[chosen_item] == 0:
    print("Sorry! This item is out of stock.")
    exit()


Prices = [2, 3, 10, 1, 5]

markup = int(input("Enter markup amount: "))

marked_prices = list(map(lambda price: price + markup, Prices))
print("Marked-up Prices:", marked_prices)

index = items.index(chosen_item)
final_price = marked_prices[index]

print(f"Price of {chosen_item}: {final_price}")

inventory[chosen_item] -= 1
print(f"Remaining stock of {chosen_item}: {inventory[chosen_item]}")

print(" SCHOOL STORE INVENTORY CHECKER")
print(f"Item Bought: {chosen_item}")
print(f"Price Paid: {final_price}")
print("Updated Inventory:")
print(inventory)
print("Thank you for shopping!")
