# 1) Create a list `L` with some integer values and print it as the original list.
L = [77, 87, 92, 102, 133, 13, 82, 23]
print(L)
# 2) Initialize a variable `count = 0` to store the sum of all elements in the list.
count = 0
# 3) Use a `for` loop to iterate through each element `i` in the list `L`:
#    a) Add each element to `count` using `count += i`.
for i in L:
    count = count+i
# 4) Calculate the average of the list:
#    a) Divide the total sum `count` by the number of elements `len(L)`.
#    b) Store the result in `avg`.
avg = count/len(L)
# 5) Print the total sum and the average.
print(count, avg)
# 6) Sort the list `L` in ascending order using `L.sort()`.

# 7) After sorting:
#    a) The smallest element will be at index 0 → print `L[0]`.
#    b) The largest element will be at the last index → print `L[-1]`.
L.sort()  # ascending
print(L)
print(L[0])
print(L[-1])

L.reverse()  # decending
print(L)
print(L[0])
print(L[-1])
