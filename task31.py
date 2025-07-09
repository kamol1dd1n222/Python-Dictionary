def count_letters(text: str) -> dict[str, int]:
    dict_letters = {}
    for char in text:
        char_count = text.count(char)
        if char != ' ' and char.isalpha():
            dict_letters.setdefault(char,char_count)
    return dict_letters

text = str(input("Text:  "))
print(count_letters(text))