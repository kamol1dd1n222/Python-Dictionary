def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:
    result =  {}
    for student in range(len(students)):
        names = []
        for i in range(student,len(students)):
            if students[student].get("grade") == students[i].get('grade'):
                names.append(students[i].get("name"))
        
        result.setdefault(students[student].get('grade'),names)
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

