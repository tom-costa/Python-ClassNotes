class Bcamp:
    def __init__(self, name, course, ratings):
        self.name = name
        self.course = course
        self.ratings = ratings
    
    def calcAverage(self):
        numOfRatings = len(self.ratings)
        averageOfRatings = sum(self.ratings)/numOfRatings
        # print(f"The average rating for {self.course} is {averageOfRatings}")
        print(averageOfRatings)

    def welcome(self):
        print("Welcome!!")

learner1 = Bcamp("Paul", "Math",[9,2,3,4,5])

learner1.welcome()
print(f"My name is {learner1.name} and I am enrolled on {learner1.course} and my rating is {learner1.ratings}")
average = learner1.calcAverage()
# learner2 = Bcamp("John", "Python")
# print(f"My name is {learner2.name} and I am enrolled on {learner2.course}")