# marks out of 100
StudentGradeBook = {"A": 50,
                    "B": 76,
                    "C": 80,
                    "D": 90,
                    "E": 100}
Avg = 0
TotalNumber = 5


# calculate avg
for i in StudentGradeBook.values():
    Avg = Avg+i

Avg = Avg/TotalNumber
print("The Class Average is:", Avg)

# find highest
print("Highest mark:", max(StudentGradeBook))
# Find lowest
print("Lowest Mark:", min(StudentGradeBook))

searchup = input("Enter An Alphabet to search for the student")
print(StudentGradeBook.get(searchup, "Sorry this student is not is this class"))
