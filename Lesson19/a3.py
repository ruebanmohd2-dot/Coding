# 1) Import the `math` module to access built-in mathematical functions.
import math
print(math.ceil(23.56), math.floor(23.56))
x = 10
y = -15
print(math.copysign(x, y))
print(math.fabs(-96))
print(math.fabs(56))
print(math.gcd(24, 56))
# 2) Use `math.ceil()` and `math.floor()` on the number 23.56:
#    a) `math.ceil(23.56)` gives the smallest integer greater than or equal to 23.56.
#    b) `math.floor(23.56)` gives the largest integer less than or equal to 23.56.
#    c) Print both results in a single statement.

# 3) Create two variables:
#    a) `x = 10`
#    b) `y = -15`

# 4) Use `math.copysign(x, y)` to copy the sign of `y` onto `x`:
#    a) Since `y` is negative, the returned value becomes -10.0.
#    b) Print the result.

# 5) Use `math.fabs()` to find absolute values:
#    a) `math.fabs(-96)` returns 96.0
#    b) `math.fabs(56)` returns 56.0
#    c) Print both absolute values.

# 6) Use `math.gcd(24, 56)` to find the Greatest Common Divisor of 24 and 56.
#    Print the GCD result.
