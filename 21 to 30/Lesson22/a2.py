# 1) Define a function `palind(r)` to check whether a tuple is a palindrome
#    (meaning it reads the same forward and backward).
def palind(r):
    e = len(r)-1
    s = 0
    while s < e:
        if r[s] != r[e]:
            return False
        s += 1
        e -= 1
    return True


r = (1, 2, 3, 4, 2, 1)
TF = palind(r)
if TF == True:
    print("The Tuple is Flip-Flop")
else:
    print("The Tuple is not Flip-Flop")


# 2) Inside the function:
#    a) Set `e = len(r) - 1` to point to the last index of the tuple.
#    b) Set `s = 0` to point to the first index of the tuple.

# 3) Use a `while` loop to compare elements from both ends:
#    a) Repeat while `s < e`.
#    b) If the element at the start `r[s]` is not equal to the element at the end `r[e]`,
#       return False immediately (not a palindrome).
#    c) Move the start pointer forward using `s += 1`.
#    d) Move the end pointer backward using `e -= 1`.

# 4) If the loop finishes without mismatches, return True.
#    (This means the tuple is a palindrome.)

# 5) Create a tuple `r = (1, 2, 3, 3, 2, 1)`.

# 6) Call the function `palind(r)`:
#    a) If it returns True, print "The Tuple is Flip-Flop".
#    b) Otherwise, print "The Tuple is not Flip-Flop".
