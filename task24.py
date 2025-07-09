def most_common_char(text: str) -> str:
   
    count_char = dict()
    for char in text:
        count = text.count(char)
        count_char.setdefault(char,count)
    
    mx_char = ""
    mx_char_count = 0
    for char,value in count_char.items():
        if value > mx_char_count:
            mx_char_count = value
            mx_char = char

    return mx_char,mx_char_count



text = input("Text: ").strip().lower()
print(most_common_char(text))