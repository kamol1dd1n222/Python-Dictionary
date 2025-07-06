kalit  = input("Kalit:  ")
car = {"brand": "Chevrolet", "model": "Cobalt", "color": "white","year":2025}
if car.get(kalit) == None:
    print("Topilmadi")
else: 
    print(car.get(kalit))