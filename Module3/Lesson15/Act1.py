def greet_customer():
    print("Welcome")
    print("Lemonade is available")


greet_customer()

price_per_cup = int(input("Enter Price"))
cups_sold = int(input("Enter Sold"))


def calculate(price, cup):
    total = price*cup
    return total


totalcost = calculate(price_per_cup, cups_sold)

round_totalcost = round(totalcost, 2)
print(round_totalcost)

amountpaid = int(input("Amount paid"))


def change(paid, total):
    change = paid-total
    return change


changedue = change(amountpaid, round_totalcost)


def thankyou(cups):
    if cups >= 5:
        return "Thank you"
    else:
        return "Thanks"


Msg = thankyou(cups_sold)
print("")
print("===== LEMONADE STAND RECEIPT =====")
print("Price Per Cup:", price_per_cup)
print("Cups Sold:", cups_sold)
print("Total Cost:", round_totalcost)
print("Amount Paid:", amountpaid)
print("Change Due:", changedue)
print(Msg)
print("===================================")
