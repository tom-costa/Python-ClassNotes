class MobilePhone:
    def __init__(self):
        self.name = "Samsung"
        self.description = "Slim build, touch screen"
        self.price = 949
m1 = MobilePhone()

print(m1.name)
print(m1.description)
print(m1.price)

print("///////////////////////////")
# Exercise: Create a class of your choice
# create two instances(objects) of the class
# print the values inside the class through object

class Laptop:
    def __init__(self, brand, CPU, screensize):
        self.brand = brand
        self.CPU = CPU
        self.screensize = screensize
    
lap1 = Laptop("Apple","M1", "13.3 in")
print("brand:", lap1.brand)
print("CPU:", lap1.CPU)
print("screensize:", lap1.screensize)

print("///////////////////////////")
lap2 = Laptop("LG", "Ryzen", "15.4 in")
print("brand:", lap2.brand)
print("CPU:", lap2.CPU)
print("screensize:", lap2.screensize)
