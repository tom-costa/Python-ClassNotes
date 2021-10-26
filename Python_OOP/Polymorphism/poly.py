# Polymorphism - Poly means multi and morphic means shapes
# in OOP shares means behaviour. Different behviour based on the data or objects that the functions are dealing with.
# Is implemented through DUCK typing

class Cat:
    def talking(self):  # method talking
        print("Meeoow")

class Person:
    def talking(self):
        print("Hello... you")

class Dog:
    def talking(self):
        print("Woof! Woof!")

# Creaste a function without specifying the type of object and obj as the parameter to invoke the method of the object.
def someTalking(obj):
    obj.talking()

c = Cat()
someTalking(c)

p = Person()
someTalking(p)

d = Dog()
someTalking(d)