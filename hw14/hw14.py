class Vehicle:
    def __init__(self, producer: str, model: str, year: int, tank_capacity: float, max_speed: int,
                 fuel_consumption: float, tank_level: float = 0, odometer_value: int = 0):
        self.producer = producer
        self.model = model
        self.year = year
        self.tank_capacity = tank_capacity
        self.max_speed = max_speed
        self.fuel_consumption = fuel_consumption
        self.tank_level = tank_level
        self.odometer_value = odometer_value

    def refueling(self):
        refueled = self.tank_capacity - self.tank_level
        self.tank_level = self.tank_capacity
        print(f"Was refueled {refueled} litres")

    def race(self, distance):
        max_distance = round(self.tank_level / self.fuel_consumption * 100, 2)
        if max_distance < distance:
            distance = max_distance
        fuel_used = round(self.fuel_consumption / 100 * distance, 2)
        self.tank_level -= fuel_used
        self.odometer_value += distance
        time_passed = distance / (self.max_speed * 0.8)
        result = {
            "distance": distance,
            "tank_level": self.tank_level,
            "time_passed": time_passed
        }
        return result

    def lend_fuel(self, other):
        if self.tank_capacity == self.tank_level or other.tank_level == 0:
            print("Нічого страшного, якось розберуся")
        else:
            to_lend_fuel = self.tank_capacity - self.tank_level
            if to_lend_fuel > other.tank_level:
                to_lend_fuel = other.tank_level
            other.tank_level -= to_lend_fuel
            self.tank_level += to_lend_fuel
            print(f"Дякую, бро, виручив. Ти залив мені {to_lend_fuel} літрів пального")

    def __eq__(self, other):
        is_years_equal = self.year == other.year
        is_odometers_equal = self.odometer_value == other.odometer_value
        return is_years_equal and is_odometers_equal

    def __repr__(self):
        return f"{self.producer}, {self.model}, {self.year}, {self.tank_level} of {self.tank_capacity}, " \
               f"{self.max_speed}, {self.fuel_consumption},  {self.odometer_value}"


aveo = Vehicle("Chevrolet", "Aveo", 2008, 45, 150, 7)
emgrand = Vehicle("Geely", "Emgrand", 2014, 60, 160, 8)
