# 1) Store values in `a`, `b`, and `c`.
a = 5
b = 9
c = 3
# 2) Check if `a` is not equal to `b` using `!=` and print the result (True/False).
if a != b:
    print(bool(a != b))
# 3) Check if `b` is not equal to `c` using `!=` and print the result (True/False).
if b != c:
    print(bool(b != c))
# 4) Store two strings in `a` and `b`.
a = "Hello"
b = "Hi"
# 5) If `a` is not equal to `b`, print a message saying they are different.
if a != b:
    print("There are different")
# 6) Store new numeric values in `a` and `b`.
a = 4
b = 9
# 7) Check this condition: (a equals 1) is not the same as (b equals 5).
#    - If exactly one of these comparisons is True, the condition becomes True.
#    - If the condition is True, print "Hello".
if a == 1 or b == 5:
    print("False")
# 8) Take an integer input from the user and store it in `a`.
a = (int(input("Enter A number")))
# 9) Check if `a` is not divisible by 2 (remainder is not 0).
#    - If true, print that `a` is not an even number (it is odd).
if a % 2 == 0:
    print("Number is even")
else:
    print("Number is Odd")
