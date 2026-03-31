import random

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.speed = max(0, min(car.max_speed, car.speed + change))
            car.drive(1)

    def print_status(self):
        print(f"\nRace: {self.name}")
        print("Reg\tSpeed\tDistance")
        for car in self.cars:
            print(f"{car.reg}\t{car.speed}\t{car.distance}")

    def race_finished(self):
        return any(car.distance >= self.distance for car in self.cars)
