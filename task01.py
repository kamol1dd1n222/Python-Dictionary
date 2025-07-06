student = {}
name = input("Name:  ")
age = int(input("Age:  "))
grade = int(input("Grade:  "))

student.update({"name":name,
                "age": age,
                "grade":grade})
print(student)