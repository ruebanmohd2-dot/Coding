# 1) Ask the user to enter a number and store it in `n`.
n = int(input("Enter A Number:"))
# 2) Set `sum` to 0.
#    (This will store the running total.)
sum = 0
# 3) Use a `for` loop from 1 to `n` (inclusive):
#    - In each step, add the current value of `i` to `sum`.
for i in range(1, n+1):
    sum = sum+i
# 4) After adding, print the current value of `sum`.
#    (So the user can see how the sum increases step by step.)
print(sum)


# 1) Ask the user to enter a number and store it in `n`.
n = int(input("Enter A Number:"))
# 2) Set `sum` to 0.
#    (This will store the running total.)
product = 1
# 3) Use a `for` loop from 1 to `n` (inclusive):
#    - In each step, add the current value of `i` to `sum`.
for i in range(1, n+1):
    product = product*i
# 4) After adding, print the current value of `sum`.
#    (So the user can see how the sum increases step by step.)
print(product)
