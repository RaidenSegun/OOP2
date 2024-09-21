class Vehicle:
    def move(self):
        print("Транспорт движется")

    def fuel(self):
        return "Неизвестно"

class Car(Vehicle):
    def move(self):
        print("Машина едет на дороге.")

    def fuel(self):
        return "Бензин"
    
class Bicycle(Vehicle):
    def move(self):
        print("Велосипедист крутит педали")

    def fuel(self):
        return "Физическая сила"
    
class Boat(Vehicle):
    def move(self):
        print("Лодка плавает по воде")
    
    def fuel(self):
        return "Дизель"
    
vehicles = [Car(), Bicycle(), Boat()]

for vehicle in vehicles:
    vehicle.move()
    print(f"Топливо: {vehicle.fuel()}\n")