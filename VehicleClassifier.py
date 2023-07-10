class Vehicle:
    def start(self):
        print("Vehicle started.")

    def stop(self):
        print("Vehicle stopped.")


class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped.")


class Motorcycle(Vehicle):
    def start(self):
        print("Motorcycle started")

    def stop(self):
        print("Motorcycle stopped.")


vehicle = Vehicle()
vehicle.start()
vehicle.stop()

car = Car()
car.start()
car.stop()

motorcycle = Motorcycle()
motorcycle.start()
motorcycle.stop()