def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:
    result =  {}
    for student in students:
        grade = student.get("grade")
        name = student.get("name")
        result.setdefault(grade,[])
    return result



students: list[dict[str, str]] = [
    {"name": "Ali", "grade": "A"},
    {"name": "Vali", "grade": "B"},
    {"name": "Hasan", "grade": "C"},
    {"name": "Husan", "grade": "B"},
    {"name": "Olim", "grade": "A"},
    {"name": "Jasur", "grade": "C"},
    {"name": "Diyor", "grade": "B"},
    {"name": "Komil", "grade": "A"}
]
print(group_students(students))
