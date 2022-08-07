# Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель",
# наслідувані від "Транспортний засіб".
# Наповніть класи атрибутами на свій розсуд.
# Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".

class Transport:
    def __init__(self, weight, fuel_type):
        self.weight = weight
        self.fuel_type = fuel_type


class Car(Transport):
    def __init__(self, weight, fuel_type, wheels_count, car_body):
        super().__init__(weight, fuel_type)
        self.wheels_count = wheels_count
        self.car_body = car_body


class Airplane(Transport):
    def __init__(self, weight, fuel_type, cargo_type, pilots_count):
        super().__init__(weight, fuel_type)
        self.cargo_type = cargo_type
        self.pilots_count = pilots_count


class Ship(Transport):
    def __init__(self, weight, fuel_type, type_, displacement):
        super().__init__(weight, fuel_type)
        self.type_ = type_
        self.displacement = displacement


aveo = Car(1200, "gasoline", 4, "hatchback")
emgrand = Car(1260, "propan/gasoline", 4, "sedan")
su25 = Airplane(9800, "kerosene", "bomb", 1)
boing737 = Airplane(10050, "kerosene", "passengers", 2)
regina = Ship(90000, "diesel", "corvette", 925)
hornet = Ship(100000, "diesel", "aircraft_carrier", 27100)
