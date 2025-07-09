from random import randint
def group_indices(numbers: list[int]) -> dict[int, list[int]]:
    number_dict = {}
    
    for i in range(len(numbers)):
        number_index = []
        for j in range(i,len(numbers)):
            if numbers[i] == numbers[j]:
                number_index.append(j)
        if numbers[i] not in number_dict.keys():
            number_dict.update({numbers[i] : number_index})
    return number_dict


numbers = []
for i in range(10):
    numbers.append(randint(1,11))
print(numbers)

print(group_indices(numbers))

