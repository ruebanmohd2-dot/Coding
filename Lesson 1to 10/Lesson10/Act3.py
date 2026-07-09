# 1) Ask the user to enter a number (greater than 1) and store it in `n`.
n = int(input("enter a number greater than 1:"))
# 2) Print a message saying you will display numbers from `n` down to 1.
print("from your entered number to 1 will be displayed")
# 3) Use a `for` loop that starts from `n`, goes down to 1, and decreases by 1 each time.
if n > 1:
    for i in range(n, 0, -1):
        print(i)
else:
    print("Number is Less than 2")
# 4) Inside the loop, print the current value of `i` (so numbers appear in reverse order).
