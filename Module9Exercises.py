import random


class Car:
    CurrentSpeed = 0
    TravelledDis = 0

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
        self.TravelledDis += (self.CurrentSpeed * Hours)


# Testing function
TestCar = Car("ABC-123", 142)
print(f"Registration number: {TestCar.Regis_num} Maximum speed: {TestCar.MaxSpeed}km/h")

TestCar.accelerate(30)
TestCar.accelerate(70)
TestCar.accelerate(50)
print(f"Current speed of the car: {TestCar.CurrentSpeed}")

TestCar.accelerate(-200)
print(f"Final speed: {TestCar.CurrentSpeed}")

# The car race
Cars = []
fastest = 0
for i in range(1, 11):
    Regis_num = "ABC-" + str(i)
    MaxSpeed = random.randint(100, 201)
    car = Car(Regis_num, MaxSpeed)
    Cars.append(car)

while fastest < 10000:
    for car in Cars:
        if car.TravelledDis > fastest:
            fastest = car.TravelledDis
        car.accelerate(random.randint(-10, 16))
        car.drive(1)


print("{:<20} {:<15} {:<15} {:<15}".format("Registration Number:", "Maximum speed:", "Current speed:", "Travelled distance:"))
for car in Cars:
    print(
        "{:<20} {:<15} {:<15} {:<15}".format(car.Regis_num, car.MaxSpeed, car.CurrentSpeed, car.TravelledDis))