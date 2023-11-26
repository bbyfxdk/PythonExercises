"""
class Elevator:
    CurrentFloor = 0

    def __init__(self, Bottom, Top):
        self.Bottom = Bottom
        self.Top = Top

    def go_to_floor(self, Floor):
        while self.CurrentFloor != Floor:
            if self.CurrentFloor < Floor:
                self.go_up()
            elif self.CurrentFloor > Floor:
                self.go_down()
            print(self.CurrentFloor)
        return self.CurrentFloor

    def go_up(self):
        self.CurrentFloor += 1

    def go_down(self):
        self.CurrentFloor -= 1

class Building:
    ElevatorList = []

    def __init__(self, Bottom, Top, Elevator_num):
        self.Top = Top
        self.Bottom = Bottom
        self.Elevator_num = Elevator_num
        for h in range(1, Elevator_num+1):
            h = Elevator(self.Bottom, self.Top)
            self.ElevatorList.append(h)

    def run_elevator(self, Elevator_index, Des_floor):
        self.ElevatorList[Elevator_index].go_to_floor(Des_floor)

    def fire_alarm(self):
        for h in self.ElevatorList:
            h.go_to_floor(self.Bottom)
            print(h.CurrentFloor)

# Testing the elevator
elevator = Elevator(1, 7)
elevator.go_to_floor(5)
elevator.go_to_floor(1)

building1 = Building(1, 8, 3)
building1.run_elevator(1,5)
building1.fire_alarm()
"""

# Exercise 4:

import random


class Car:
    CurrentSpeed = 0
    TravelledDistance = 0

    def __init__(self, Regis_num, MaxSpeed):
        self.Regis_num = Regis_num
        self.MaxSpeed = MaxSpeed

    def accelerate(self, SpeedChange):
        self.CurrentSpeed += SpeedChange
        if self.CurrentSpeed >= self.MaxSpeed:
            self.CurrentSpeed = self.MaxSpeed
        elif self.CurrentSpeed <= 0:
            self.CurrentSpeed = 0
        return self.CurrentSpeed

    def drive(self, Hours):
        self.TravelledDistance += (self.CurrentSpeed * Hours)


class Race:
    Cars = []

    def __init__(self, Name, Distance, Car_num):
        self.Name = Name
        self.Distance = Distance
        self.Car_num = Car_num
        for i in range(1, Car_num + 1):
            Regis_num = "ABC-" + str(i)
            MaxSpeed = random.randint(100, 201)
            car = Car(Regis_num, MaxSpeed)
            self.Cars.append(car)

    def hour_pass(self):
        for car in self.Cars:
            car.accelerate(random.randint(-10, 16))
            car.drive(1)

    def print_status(self):
        print("{:<20} {:<15} {:<15} {:<15}".format("Registration Number:", "Maximum speed:", "Current speed:",
                                                   "Travelled distance:"))
        for car in self.Cars:
            print(
                "{:<20} {:<15} {:<15} {:<15}".format(car.MaxSpeed, car.MaxSpeed, car.CurrentSpeed,
                                                     car.TravelledDistance))

    def race_finished(self):
        for Car in self.Cars:
            if Car.TravelledDistance >= self.Distance:
                return True


# the car race
race = Race("Grand Demolition Derby", 8000, 10)
Hour = 0

while not race.race_finished():
    race.hour_pass()
    Hour += 1
    if (Hour % 10) == 0:
        print(f"\n{Hour} hours has passed\n")
        race.print_status()

print(f"\nTotal {Hour} hours has passed\nResult of {race.Name} is:")
race.print_status()
