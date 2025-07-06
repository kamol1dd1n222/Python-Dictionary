def counter_names(names: list[str]) -> dict[str, int]:
    names_dict = dict()
    for name in names:
        counter = names.count(name)
        if name not in names_dict.keys():
            names_dict.update({name: counter})
    return names_dict

names = ["Ali", "Vali", "Ali", "Hasan", "Ali", "Vali", "Olim", "Hasan"]
print(counter_names(names))