# Encapsulation is protecting the properties and functionalities of an object from other objects

class Learner:
    def setId(self, sId):  # create a setter method along with the parameter
        self.sId = sId 

    def getId(self):  # define a getter method which does require additional parameters
        return self.sId 

    def setName(self, setName):
        self.setName = setName

    def getName(self, getName):
        return self.getName

# Exercise: Add a setter and a gettter method for name
# Access it using the setter method
l1 = Learner()

l1.setId(1001)  #pass the arguments/ values to the setter parameter
print(l1.sId)

l1.setName("Jack")
print(l1.setName)