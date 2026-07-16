SecretNumber = 43
Guess = int(input("Enter A number"))

if Guess == 43:
    print("U have guessed The correct Number")
elif Guess <= 10:
    print("Ice Cold")
elif Guess > 10 or Guess < 20:
    print(" Cold")
elif Guess > 20 or Guess < 35:
    print(" Warm")
elif Guess > 35 or Guess < 42:
    print(" Hot")
elif Guess > 44 or Guess < 50:
    print(" Hot")
