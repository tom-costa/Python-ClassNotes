# Abstract class can't be initiated. One method has to be an abstract class
from abc import abstractmethod, ABC

class Car(ABC):  # parent class inherits from the ABC to mandate all child classes implement the abstract method
    def __init__(self, make, model, year):  # parent class constructor
        self.make = make
        self.model = model
        self.year = year

    def startCar(self):
        pass

    @abstractmethod   # mark with the abstract decorator
    def driveCar(self):
        print("Starting the car...")

    def stopCar(self):
        print("Stopping the car...")


# Mercedes
class Merc(Car):
    def __init__(self, parkingAssist, make, model, year):
        super().__init__(make, model, year)  # remove the "self" because we are using SUPER
        self.parkingAssist = parkingAssist

    def startCar(self):
        print("Merc STARTCAR Override")   # Overriding the StartCar statement from the parent
        super().startCar() # Invoking the parent class method within the child class

mercCar = Merc(True, "Benz", "190", 2001)

print(mercCar.make)
print(mercCar.model)
print(mercCar.year)
print(mercCar.parkingAssist)

mercCar.startCar()
print(f"I am driving a {mercCar.year}, {mercCar.make}")
mercCar.stopCar()


class Bmw(Car):  # child class
    def __init__(self, cruisedControlled, make, model, year):   # inherited parent class fields
        super().__init__(make, model, year)     # invoke parent class constructor passing its parameters
        self.cruisedControlled = cruisedControlled

    def stopCar(self):
        print("SUPER - Stopping...")
        super().stopCar()


bmwCar = Bmw(True, "BMW", "312E", 2017)

print(bmwCar.make)
print(bmwCar.model)
print(bmwCar.year)
print(bmwCar.cruisedControlled)
print(f"I am driving a {bmwCar.year}, {bmwCar.make}")
bmwCar.stopCar()
bmwCar.driveCar()