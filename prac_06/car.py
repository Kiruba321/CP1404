class Car:
    def __init__(self, fuel=0, name=""):
        self.fuel = fuel
        self.name = name
        self.odometer = 0

    def add_fuel(self, amount):
        self.fuel += amount

    def drive(self, distance):
        fuel_needed = distance / 10
        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
            self.odometer += distance
        else:
            print("Not enough fuel to drive that far!")

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"


