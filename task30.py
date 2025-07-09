def filter_non_zero(d: dict[str, int]) -> dict[str, int]:
    filter_one_dict = {}
    for dd in d.items():
        if dd[1] != 0:
            filter_one_dict.update({dd[0]: dd[1]})
    return filter_one_dict


dictionary = {
    "a" : 4,
    "b": 2,
    "c": 0,
    "g": 1,
    "k": 0,
    "sh": 11,
    "z": 0 
}
print(filter_non_zero(dictionary))