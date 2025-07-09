def group_by_length(words: list[str]) -> dict[int, list[str]]:
    group_dict = {}
    for word in words:
        lenght = len(word[0])
        group_dict[lenght] = word
    return group_dict

words = [
    ["Python"],
    ["is a high-level"],
    ["versatile"],
    ["programming"],
    ["language"],
    ["known for"],
    ["its readability"],
    [" and ease of use"]
]

print(group_by_length(words))