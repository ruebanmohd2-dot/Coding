# 1) Take an integer input from the user and store it in `rows`.
#    (This represents the total number of rows to print.)
rows = int(input("Enter a number for the total number for rows:"))
# 2) Initialize `number = 1`.
#    (This is the starting value to be printed in Floyd's Triangle.)
number = 1
# 3) Print a heading message: "Floyd's Triangle".
print("Floyd's Triangle")
# 4) Use an outer loop to handle each row from 1 to `rows` (inclusive):
#    a) The current row number is `i`.
for i in range(1, rows+1):
    for j in range(1, i):
        print(number, end=" ")
        number = number + 1
    print()
# 5) Use an inner loop to handle the numbers in each row:
#    a) For row `i`, print `i` numbers, so loop `j` from 1 to `i` (inclusive).
#    b) Print the current value of `number` on the same line using `end='  '`.
#    c) Increase `number` by 1 after printing so the next number continues in sequence.

# 6) After finishing each row, print a blank `print()` to move to the next line.
