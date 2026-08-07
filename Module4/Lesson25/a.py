items = ["Pencil", "Eraser", "Notebook", "Sharpener", "Glue"]
stock = [12, 0, 8, 5, 3]

inventory = dict(zip(items, stock))
print(inventory)

availableitems = [item for item in items if inventory[item] > 0]
print("Available items:", availableitems)

chosen_item = input("Enter an item: ")

# 5) Check stock availability
if inventory[chosen_item] == 0:
    print("Sorry! This item is out of stock.")
    exit()


Prices = [2, 3, 10, 1, 5]

markup = int(input("Enter markup amount: "))

# 7) Apply markup using map()
marked_prices = list(map(lambda price: price + markup, prices))
print("Marked-up Prices:", marked_prices)

# 8) Find the selected item price
index = items.index(chosen_item)
final_price = marked_prices[index]

print(f"Price of {chosen_item}: {final_price}")

# 9) Update the inventory
inventory[chosen_item] -= 1
print(f"Remaining stock of {chosen_item}: {inventory[chosen_item]}")

# 10) Print the final store summary
print("\n===== SCHOOL STORE INVENTORY CHECKER =====")
print(f"Item Bought: {chosen_item}")
print(f"Price Paid: {final_price}")
print("Updated Inventory:")
print(inventory)
print("Thank you for shopping!")

"""
5) Check stock availability.
   a) Check if the item is not in the inventory.
   b) Check if the item stock is 0.
   c) Print an out-of-stock message.
   d) Use `exit()` to stop the program early.

6) Create prices and markup.
   a) Create a list named `prices`.
   b) Ask the user to enter a markup amount.
   c) Convert the markup input into an integer.

7) Apply markup using `map()`.
   a) Use `map()` to update every price.
   b) Use a lambda function to add the markup.
   c) Convert the result into a list.
   d) Print the marked-up prices.

8) Find the selected item price.
   a) Use `items.index()` to find the chosen item's position.
   b) Use the same index to get the marked-up price.
   c) Print the final price of the chosen item.

9) Update the inventory.
   a) Reduce the chosen item's stock count by 1.
   b) Print the remaining stock after purchase.

10) Print the final store summary.
   a) Print the school store inventory checker heading.
   b) Show the item bought and price paid.
   c) Show the updated inventory.
   d) Print a closing line to complete the summary.
"""
