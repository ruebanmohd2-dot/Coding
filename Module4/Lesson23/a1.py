# 1) Create a dictionary `student_data` where:
#    a) Each key is a student ID (like "id1", "id2", etc.)
#    b) Each value is another dictionary containing student details:
#       - name
#       - class
#       - subject_integration
student_data = {"id1": {"name": "Def", "class": 8, "Subject_integration": "English,Math,Coding."},
                "id2": {"name": "XYZ", "class": 12, "Subject_integration": "English,Math,Coding."},
                "ïd3": {"name": "Def", "class": 8, "Subject_integration": "English,Math,Coding."},
                "ïd4": {"name": "Abc", "class": 8, "Subject_integration": "English,Math,Coding."}}
# 2) Create an empty dictionary `result` to store only unique student entries.
result = {}
# 3) Create an empty set `seen` to keep track of student detail combinations already added.
seen = []
# 4) Use a `for` loop to iterate through `student_data.items()`:
#    a) `student_id` holds the key (student ID)
#    b) `details` holds the value (student’s info dictionary)
for i, j in student_data.items():
    uniquekey = (j["name"], j["class"], j["Subject_integration"])
    if uniquekey not in seen:
        seen.append(uniquekey)
        result[i] = j

for k in result:
    print(k, ":", result[k])
# 5) For each student, create a tuple `unique_key` using:
#    (name, class, subject_integration)
#    (This tuple acts like a signature to identify duplicates.)

# 6) Check if `unique_key` is already in the `seen` set:
#    a) If it is NOT present:
#       i) Add `unique_key` to `seen`
#       ii) Add the student entry to `result` using `result[student_id] = details`
#    b) If it is already present, skip it (duplicate student details).

# 7) Print the final `result` dictionary line by line:
#    a) Use a loop through `result.items()`
#    b) Print each student ID and its details in the format: key : value
