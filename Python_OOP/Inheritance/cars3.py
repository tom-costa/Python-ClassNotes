
class Car:  # parent class
    def __init__(self, make, model, year):  # parent class constructor
        self.make = make
        self.model = model
        self.year = year

    def startCar(self):
        print("Starting the car...")

    def stopCar(self):
        print("Stopping the car...")


# Mercedes
class Merc(Car):
    def __init__(self, parkingAssist, make, model, year):
        Car.__init__(self, make, model, year)
        self.parkingAssist = parkingAssist

    def startCar(self):
        print("Merc STARTCAR Override")   # Overriding the StartCar statement from the parent
mercCar = Merc(True, "Benz", "190", 2001)

print(mercCar.make)
print(mercCar.model)
print(mercCar.year)
print(mercCar.parkingAssist)

mercCar.startCar()
print(f"I am driving a {mercCar.year}, {mercCar.make}")
mercCar.stopCar()


