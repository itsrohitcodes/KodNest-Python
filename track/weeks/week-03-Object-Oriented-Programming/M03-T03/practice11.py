# Build Vehicle and ElectricCar Classes

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        return f"Brand: {self.brand}"


class ElectricCar(Vehicle):
    # Create show_battery() here
    def show_battery(self, battery_capacity):
        return f"Battery: {battery_capacity} kWh"


brand = input()
battery_capacity = int(input())

car = ElectricCar(brand)

print(car.show_brand())
print(car.show_battery(battery_capacity))