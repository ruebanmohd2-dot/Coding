try:
    Operation = input(
        "Enter Operation To Be Done On The two numbers: (Expexted Entry + - * /)")
    N1 = float(input("Enter First Number"))
    N2 = float(input("Enter Second Number"))
    if Operation == "+":
        def addition(x, y):
            return x + y
        print(addition(N1, N2))

    elif Operation == "-":
        def subtraction(x, y):
            return N1 - N2
        print(subtraction(N1, N2))

    elif Operation == "*":
        def multiplication(x, y):
            return N1 * N2
        print(multiplication(N1, N2))

    elif Operation == "/":
        def Division(x, y):
            return N1 / N2
        print(Division(N1, N2))

except ValueError:
    print("Invalid Input Please Enter Number")
except ZeroDivisionError:
    print("Cannot Be divided with 0")
