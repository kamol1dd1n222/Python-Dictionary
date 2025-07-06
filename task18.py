students = {"name": "Ali", "age": 25, "grade": "A"}
for student in students.items():
    key = student[0].upper()
    value = student[1]
    print(f"{key} -> {value}")