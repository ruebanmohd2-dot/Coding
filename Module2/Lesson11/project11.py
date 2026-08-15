number = int(input("Enter a number: "))
original_number = number
digitcount = 0
if number == 0:
    digitcount = 1
else:
    while number > 0:
        number = number // 10
        digitcount += 1
print(f"The total number of digits {original_number} is: {digitcount}")
