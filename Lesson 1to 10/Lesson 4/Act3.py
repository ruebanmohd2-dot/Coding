# 1) Ask the user to enter marks for 4 subjects: math, english, science, and hindi.
#    Store each mark in its own variable.
mark1 = int(input("Enter Marks Scored In English"))
mark2 = int(input("Enter Marks Scored In Math"))
mark3 = int(input("Enter Marks Scored In Science"))
mark4 = int(input("Enter Marks Scored In Arabic"))
# 2) Add all 4 subject marks and store the total in `sum`.
sum = mark1+mark2+mark3+mark4
# 3) Print the total marks stored in `sum`.
print(sum)
# 4) Calculate the percentage:
#    - Divide `sum` by 400 (total maximum marks for 4 subjects, assuming each is out of 100)
#    - Multiply the result by 100
#    Store the final value in `perc`.
result = sum/400
x = result*100
perc = x
# 5) Print the percentage stored in `perc`.
print(perc)
