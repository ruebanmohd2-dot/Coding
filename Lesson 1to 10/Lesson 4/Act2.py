# 1) Take the total withdrawal amount as input from the user and store it in `Amount`.
Amount = int(input("enter the withdrawal amount"))
# 2) Find how many 100-rupee notes are needed:
#    Divide `Amount` by 100 (whole number division) and store it in `note_1`.
note_1 = Amount//100
# 3) Find the remaining amount after taking out 100-rupee notes:
#    Use the remainder of `Amount` after dividing by 100.
r1 = Amount % 100
# 4) From the remaining amount, find how many 50-rupee notes are needed:
#    Divide the remainder by 50 (whole number division) and store it in `note_2`.
note_2 = r1//50
# 5) Find the remaining amount after taking out 50-rupee notes:
#    Use the remainder after dividing by 50.
r2 = r1 % 50
# 6) From the remaining amount, find how many 10-rupee notes are needed:
#    Divide the remainder by 10 (whole number division) and store it in `note_3`.
note_3 = r2//10
# 7) Print the number of 100-rupee notes, 50-rupee notes, and 10-rupee notes.
print(note_1, note_2, note_3)
