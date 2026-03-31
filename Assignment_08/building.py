from elevator import Elevator

class Building:
    def __init__(self, bottom, top, num_elevators):
        self.elevators = [Elevator(bottom, top) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination):
        self.elevators[elevator_number].go_to_floor(destination)

    def fire_alarm(self):
        print("Fire alarm! Moving all elevators to bottom floor.")
        for elevator in self.elevators:
            elevator.go_to_floor(elevator.bottom)
