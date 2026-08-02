x = {"R": 1, "S": 2, "X": 2, "Y": 1, "Z": 2}
print(x)
Value = 1
count = 0
for i in x:
    if x[i] == Value:
        count += 1
print(count)
