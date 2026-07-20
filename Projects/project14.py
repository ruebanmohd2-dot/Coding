secret = 43
i = 1
while i <= 5:
    x = int(input("Enter Number"))
    print("Remaining Lives:", end="")
    for j in range(5-i):

        print("❤️", end=" ")

    if x == secret:
        print("U have won the game")
        break

    elif x in range(1, 21):
        print("\n Hint:Ice cold")
    elif x in range(21, 31):
        print("\n Hint:Cold")
    elif x in range(31, 36):
        print("\n Hint:Warm")
    elif x in range(36, 43):
        print("\n Hint:Hot")
    elif x in range(44, 51):
        print("\n Hint:Hot")

    i = i+1
