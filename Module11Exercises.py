# Exercise 1:
class Publication:
    def __init__(self, Name):
        self.Name = Name

    def print_information(self):
        pass

class Book(Publication):
    def __init__(self, Name, Author, Page_count):
        super().__init__(Name)
        self.Author = Author
        self.Page_count = Page_count

    def print_information(self):
        print(f"Name: {self.Name}\nAuthor: {self.Author}\nPage: {self.Page_count} pages")


class Magazine(Publication):
    def __init__(self, Name, Editor):
        super().__init__(Name)
        self.Editor = Editor

    def print_information(self):
        print(f"Name: {self.Name}\nEditor: {self.Editor}")

magazine1 = Magazine("Donald Duck", "Aki Hyyppä")
book1 = Book("Compartment No.6", "Rosa Liksom", 192)
magazine1.print_information()
book1.print_information()

# Exercise 2:

import random


class Car:
    CurrentSpeed = 0
    TravelledDistance = 0

    def __init__(self, Regis_num, MaxSpeed):
        self.Regis_num = Regis_num
        self.MaxSpeed = MaxSpeed

    def accelerate(self, Speedchange):
        self.CurrentSpeed += Speedchange
        if self.CurrentSpeed >= self.MaxSpeed:
            self.CurrentSpeed = self.MaxSpeed
        elif self.CurrentSpeed <= 0:
            self.CurrentSpeed = 0
        return self.CurrentSpeed

    def drive(self, Hours):
        self.TravelledDistance += (self.CurrentSpeed * Hours)


class ElectricCar(Car):
    def __init__(self, Regis_num, MaxSpeed, Battery):
        super().__init__(Regis_num, MaxSpeed)
        self.Battery = Battery


class GasolineCar(Car):
    def __init__(self, Regis_num, MaxSpeed, Tank):
        super().__init__(Regis_num, MaxSpeed)
        self.Tank = Tank


car1 = ElectricCar("ABC-15", 180, 52.5)
car2 = GasolineCar("ACD-123", 165, 32.2)
car1.accelerate(100)
car2.accelerate(120)
car1.drive(3)
car2.drive(3)
print(f"After 3 hours, electric car drove {car1.TravelledDistance} km")
print(f"After 3 hours, gasoline car drove {car2.TravelledDistance} km")