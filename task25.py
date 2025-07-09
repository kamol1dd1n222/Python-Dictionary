def group_by_age(people: list[dict[str, int | str]]) -> dict[int, list[str]]:
    result_dict = {}
    for person in range(len(people)):
        names = []
        for i in range(person,len(people)):
            if people[person].get('age') == people[i].get("age"):
                names.append(people[i].get("name"))
        result_dict.setdefault(people[person].get("age"),names)
    return result_dict
        

people = [
    {"name": "Ali", 'age': 18},
    {"name": "Abduvali", 'age': 20},
    {"name": "Abdulla", 'age': 19},
    {"name": "Alibek", 'age': 18},
    {"name": "Alisher", 'age': 18},
    {"name": "Abdug'ani", 'age': 20},
    {"name": "Akram", 'age': 21},
    {"name": "Abbos", 'age': 19}   
]
print(group_by_age(people))