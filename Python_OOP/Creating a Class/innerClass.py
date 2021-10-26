# Its a class within a class

class Car:
    def __init__(self, make, year):
        self.make = make
        self.year = year
    
    class CarEngine:
        def __init__(self, engineNum):
            self.engineNum = engineNum

        def startCar(self):
            print("Engine start...")

# To access the Car class:   
c1 = Car('Benz', 2018)
c2 = Car('Audi', 2003)
c3 = Car('Toyota', 2015)

# Then new variable to access the inner class. 
# Structure: new variable = class created variable, + "." + innerClass name(value to be passed into it)
carEng1 = c1.CarEngine(1234)

print("make:", c1.make)
print("year:", c1.year)
print("engine:", carEng1.engineNum)
carEng1.startCar()

# Create two more instances/ objects of the class Car, passed in different values and display output the result
carEng2 = c2.CarEngine(80212)
print("make:", c2.make)
print("year:", c2.year)
print("engine:",carEng2.engineNum)
carEng2.startCar()

carEng3 = c3.CarEngine(70532)
print("make:",c3.make)
print("year:", c3.year)
print("engine:",carEng3.engineNum)
carEng3.startCar()
