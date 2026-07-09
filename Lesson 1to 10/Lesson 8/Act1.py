# parenteses have the highest precedence, so we can use them to control the order of operations and get the desired result.

# () > ** > * / // % > + - , evaluation is done from left to right for operators with the same precedence level.

# 1) Store values in `v`, `w`, `x`, `y`, and `z`.
v = 2
w = 4
x = 5
y = 6
z = 8
# 2) Calculate the expression (v + w) * x / y and store the result back in `z`.
z = (v+w)*x/y
# 3) Print the value of `z` with a message.
print(z)
# 4) Store a name in `name` and a number in `age`.
name = "Rueban"
age = 13
# 5) Check this condition using `or` and `and`:
#    - The code checks if `name` is "Alex"
#      OR (if `name` is "John" AND `age` is 2 or more).
#    - If the condition is true, print the welcome message.
#    - Otherwise, print the goodbye message.

if name == "Alex" or name == "John" and age >= 2:
    print("welcome")
else:
    print("Good Bye")
