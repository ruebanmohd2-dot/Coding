# --- STEP 1: SET YOUR SECRET NUMBER ---
# You can change this number before you run the code and pass it to your friend!
secret = 27

# This clears the screen so your friend cannot see the code above when it runs
os.system('cls' if os.name == 'nt' else 'clear')

print("=== NUMBER GUESSING GAME ===")
print("A secret number between 1 and 50 has been set.")
print("You have 5 attempts to guess it. Good luck!\n")

# --- GAME SETUP ---
attempts_left = 5
won = False

# --- STEP 2: MAIN GAME LOOP ---
while attempts_left > 0 and not won:
    # Display remaining lives as hearts using a for loop
    print("Lives remaining: ", end="")
    for i in range(attempts_left):
        print("❤️", end=" ")
    print()  # Prints a new line

    # Read the player's guess
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number!\n")
        continue

    # Check the guess
    if guess == secret:
        won = True
    else:
        attempts_left -= 1

        # Only give a hint if they still have lives left
        if attempts_left > 0:
            # Calculate how far away the guess is
            difference = abs(secret - guess)

            # --- STEP 3: HINT SYSTEM ---
            if difference >= 20:
                print("Hint: 🧊 ice cold")
            elif difference >= 10:
                print("Hint: 🥶 cold")
            elif difference >= 5:
                print("Hint: 🪄 warm")
            else:
                print("Hint: 🔥 hot")
            print(f"Keep trying!\n")

# --- STEP 4: WIN / LOSS MESSAGES ---
print("\n==============================")
if won:
    print(
        f"🎉 Congratulations! You guessed the secret number {secret} correctly!")
else:
    print(f"💥 Game Over! You ran out of lives.")
    print(f"The secret number was: {secret}")
print("==============================")
