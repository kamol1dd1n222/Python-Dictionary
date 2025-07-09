def merge_dicts(a: dict, b: dict) -> dict:
    result = dict()
    result.update(a)
    result.update(b)  #updatega kalit va qiymat berilsa va avval u bo'lsa kalit qiymatlarini 
                      # yangilab beradi. Shuning uchun oxiri yangilanib chiqadi
    
    return result


a = {"a": 17, "d":20}
b = {"b": 23, "c": 21}  

print(merge_dicts(a,b))
