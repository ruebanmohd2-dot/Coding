# 1) Ask the user to enter the number of electricity units consumed and store it in `units`.
units = (int(input("Enter THe number of electricity units")))
# 2) Use if–elif–else to decide the cost based on `units`:
#    - If `units` is less than 50:
#      Set `amount` as units × 2.60 and set `surcharge` as 25.
#    - Else if `units` is 100 or less:
#      Set `amount` as (cost for first 50 units) + (remaining units × 3.25)
#      Set `surcharge` as 35.
#    3- Else if `units` is 200 or less:
#      Set `amount` as (cost for first 50 units) + (cost for next 50 units) + (remaining units × 5.26)
#      Set `surcharge` as 45.
#   4 - Else (units more than 200):
#      Set `amount` as (cost for first 50) + (next 50) + (next 100) + (remaining units × 8.45)
#      Set `surcharge` as 75.
if units < 50:
    amount = 2.60*units
    surcharge = 25
elif units <= 100:
    amount = 2.60*50+(units-50)*3.25
    surcharge = 35
elif units <= 200:
    amount = 2.60*50+3.25*50+(units-100)*5.26
    surcharge = 45
else:
    amount = 2.60*50+3.25*50+5.26*100+(units-200)*8.45
    surcharge = 75
# 3) Calculate the final bill:
#    total = amount + surcharge
total = amount+surcharge
# 4) Print the electricity bill (`total`) in 2 decimal places.
print(total)
