secretnumber = 43

print("Number Guessing Games")
attempts_left = 5
won = False
while attempts_left > 0 and not won:
    print("Lives remaining: ", end="")
    for x in range(attempts_left):
        print("❤️", end=" ")
    print()

    guess = int(input("Enter your guess: "))
    if guess <= 0:
        print("Please enter a valid number!\n")
        continue

    if guess == secretnumber:
        won = True
else:
    attempts_left = attempts_left - 1
    if attempts_left > 0:

        if guess < 20:
            print("Hint: 🧊 ice cold")
        elif guess < 30:
            print("Hint: 🥶 cold")
        elif guess < 35 or guess > 50:
            print("Hint: 🪄 warm")
        else:
            print("Hint: 🔥 hot")
        print("Keep trying!")
