# 1) Create a tuple `tuplex` containing different data types (string, boolean, float, integer)
#    and print the tuple.
tuplex = ("Hello", True, 14.4, 7)
print(tuplex)
# 2) Create another tuple `tuplex` containing only integer values and print it.
tuplex = (8,)
print(tuplex)
# 3) Demonstrate tuple immutability:
#    a) Tuples cannot be modified directly (cannot add/change elements in the same tuple).
#    b) Use the `+` operator to merge tuples and create a new tuple.
#    c) Add a single element (9) using `(9,)` and store the new tuple back in `tuplex`.
#    d) Print the updated tuple.
tuplex = tuplex+(9,)
print(tuplex)
# 4) Create a tuple `tuple1` and count occurrences of a specific value:
#    a) Use `tuple1.count(50)` to count how many times 50 appears.
#    b) Print the count.
tuple1 = (tuplex.count(50))
print(tuple1)
# 5) Create a tuple `tuplex` with multiple integers to demonstrate slicing.
tuplex = (12, 87023, 20937, 903472)
# 6) Slice a portion of the tuple using indexing:
#    a) Use `tuplex[3:5]` to get elements from index 3 up to index 4 (stop index is excluded).
#    b) Store it in `_slice` and print it.
_slice = tuplex[3:5]
print(_slice)
# 7) Slice from the beginning when the start index is not provided:
#    a) Use `tuplex[:6]` to get elements from index 0 up to index 5.
#    b) Store it in `_slice` and print it.
_slice = tuplex[:6]
print(_slice)
