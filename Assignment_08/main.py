from building import Building
from car import Car
from race import Race

# Elevator test
building = Building(1, 10, 3)
building.run_elevator(0, 5)
building.run_elevator(0, 1)

building.fire_alarm()

# Race test
cars = [Car(f"ABC-{i}", 120) for i in range(1, 11)]
race = Race("Grand Demolition Derby", 8000, cars)

hours = 0
while not race.race_finished():
    race.hour_passes()
    hours += 1
    if hours % 10 == 0:
        race.print_status()

race.print_status()
print("Race finished!")
