# Base class
class Vehicle:
    def move(self):
        return "Moving in a generic way..."

# Subclasses with polymorphism
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚢"

# Test polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())
