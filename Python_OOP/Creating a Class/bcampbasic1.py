class Bcamp:
    def __init__(self, name, course, ratings):
        self.name = name
        self.course = course
        self.ratings = ratings
    

learner1 = Bcamp(
    name = input("Enter your name: "),
    course = input("Enter your course: ")
    ratings = int(input("Enter a rating"))
    )

# learner1.course = "CSS" 
print(f"My name is {learner1.name} and I am enrolled on {learner1.course}")

learner2 = Bcamp("John", "Python")
print(f"My name is {learner2.name} and I am enrolled on {learner2.course}")