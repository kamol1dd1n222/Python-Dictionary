person = {
    "name": "Jasur",
    "age": 28,
    "email": "jasur@example.com",
    "city": "Toshkent",
}
key = input("Key:   ")
if key in person.keys():
    person.pop(key)
else:
    print("Bunday kalit yuq!")
print(person)
