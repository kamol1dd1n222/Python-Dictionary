inventory = {}
soni = int(input("Mahsulotlar soni:  "))
for i in range(soni):
    mahsulot = input(f"{i + 1} - mahsulot: ")
    inventory.setdefault(mahsulot, 0)
print(inventory)