class Developer:
    def setName(self,name): # create the setter method
        self.name = name  # assign  parameter name to the object variable

    def getName(self):  # create the getter method
        return self.name   # return the value passed into the parameter

    def setPay(self, salary):
        self.salary = salary

    def getPay(self):
        return self.salary

dev1 = Developer()

dev1.setName("Paul")
dev1.setPay(4345)

print(dev1.getName())
print(dev1.getPay())

#  Exercise:

devExercise = Developer()
devExercise.setName('Jake')
devExercise.setPay(50000)

print("Name:", devExercise.getName())
print("Pay:", devExercise.getPay())