def totalcal(bill_a, tip_per):
    total = bill_a*(1+0.01*tip_per)
    total = round(total, 2)
    print(total)


totalcal(bill_a=200, tip_per=10)
