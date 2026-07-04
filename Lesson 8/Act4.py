# 1) Take three integer inputs from the user and store them in `a`, `b`, and `c`.
a = int(input("Enter A Number"))
b = int(input("Enter A Number"))
c = int(input("Enter A Number"))
# 2) Calculate the average of `a`, `b`, and `c`:
#    - Add them and divide by 3
#    - Store the result in `avg`
#    - Print `avg`
avg = a+b+c/3
print(avg)
# 3) Compare `avg` with `a`, `b`, and `c` using if–elif:
#    - If `avg` is greater than all three numbers, print that it is higher than `a`, `b`, and `c`.
#    - Else if `avg` is greater than `a` and `b`, print that it is higher than `a` and `b`.
#    - Else if `avg` is greater than `a` and `c`, print that it is higher than `a` and `c`.
#    - Else if `avg` is greater than `b` and `c`, print that it is higher than `b` and `c`.
#    - Else if `avg` is greater than only `a`, print that it is just higher than `a`.
#    - Else if `avg` is greater than only `b`, print that it is just higher than `b`.
#    - Else if `avg` is greater than only `c`, print that it is just higher than `c`.
# 4) If none of the above conditions match, print "invalid input".
if avg > a and avg > b and avg > c:
    print("Average is greater than all number")
elif avg > a and avg > b:
    print("1")

elif avg > a and avg > c:
    print("2")
elif avg > b and avg > c:
    print("3")
elif avg > a:
    print("4")
elif avg > b:
    print("5")
elif avg > c:
    print("6")
else:
    print("Invalid Input")
