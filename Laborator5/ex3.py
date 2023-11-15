class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class Car(Vehicle):
    def __init__(self, make, model, year, mileage):
        super().__init__(make, model, year)
        self.mileage = mileage

    def calculate_mileage(self):
        return f"The {self.make} {self.model} has a mileage of {self.mileage} miles per gallon."


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, mileage):
        super().__init__(make, model, year)
        self.mileage = mileage

    def calculate_mileage(self):
        return f"The {self.make} {self.model} has a mileage of {self.mileage} miles per gallon."


class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def calculate_towing_capacity(self):
        return f"The {self.make} {self.model} has a towing capacity of {self.towing_capacity} pounds."


def main():
    car = Car("Volkswagen", "Up", 2021, 30)
    motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2021, 50)
    truck = Truck("Man", "Series 2", 2021, 10000)

    print(car.calculate_mileage())
    print(motorcycle.calculate_mileage())
    print(truck.calculate_towing_capacity())


main()
