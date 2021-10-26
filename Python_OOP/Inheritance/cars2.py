
class Car:  # parent class
    def __init__(self, make, model, year):  # parent class constructor
        self.make = make
        self.model = model
        self.year = year

    def startCar(self):
        print("Starting the car...")

    def stopCar(self):
        print("Stopping the car...")

# Exercise: Add and invoke a method

    def petrolOut(self):
        print("You're out of petrol, refill now!")

class Bmw(Car):  # child class
    def __init__(self, cruisedControlled, make, model, year):   # inherited parent class fields
        Car.__init__(self, make, model, year)     # invoke parent class constructor passing its parameters
        self.cruisedControlled = cruisedControlled

bmwCar = Bmw(True, "BMW", "312E", 2017)

print(bmwCar.make)
print(bmwCar.model)
print(bmwCar.year)
print(bmwCar.cruisedControlled)
print(f"I am driving a {bmwCar.year}, {bmwCar.make}")

# Mercedes
class Merc(Car):
    def __init__(self, parkingAssist, make, model, year):
        Car.__init__(self, make, model, year)
        self.parkingAssist = parkingAssist

mercCar = Merc(True, "Benz", "190", 2001)

print(mercCar.make)
print(mercCar.model)
print(mercCar.year)
print(mercCar.parkingAssist)

mercCar.startCar()
print(f"I am driving a {mercCar.year}, {mercCar.make}")
mercCar.stopCar()
mercCar.petrolOut()


# Tesla
class Tesla(Car):
    def __init__(self, selfDriving, make, model, year):
        Car.__init__(self, make, model, year)
        self.selfDriving = selfDriving
    
teslaCar = Tesla(True, "Tesla", "Roadster", 2018)

print(teslaCar.make)
print(teslaCar.model)
print(teslaCar.year)
print(teslaCar.selfDriving)
print(f"I am driving a {teslaCar.year}, {teslaCar.make}, Self-Driving? {teslaCar.selfDriving}")