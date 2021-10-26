# Encapsulation is protecting the properties and functionalities of an object from other objects

class Learner:
    def __init__(self):
        self.__id = 123  # Use __ (double underscore) to create a private field (hidden) which can't be accessed outside its class
        self.__name = "Paul"
        self.__age = 32
        self.__city = "London"
        self.__gender = "Male"


    def displayFields(self):
        print(self.__id)
        print(self.__name)
        print(self.__age)
        print(self.__city)
        print(self.__gender)


l1 = Learner()

# Method 1:
# NAME MANGLING: Is used to access hidden fields like the ones with the double score.
# Structure: variable + . + _ClassName + __ + FieldName
print(l1._Learner__id)  # 




# Method 2:
# Define a new function within the parent class already containing the assignment to the variables with "__" before them
# And then just call out that Function
l1.displayFields()


# Add 3 more private fields
print(l1._Learner__city)
print(l1._Learner__age)
print(l1._Learner__gender)

# Access the fields using one or both methods (via function/ or name mangling.)
