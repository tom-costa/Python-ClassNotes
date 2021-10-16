# def addNumbers():
#     num1 = 5
#     num2 = 10
#     num3 = num1 + num2
#     return num3
# print("total: ", addNumbers())

# def addTwoNums(a, b):
#     numSum = a + b
#     return numSum
# print("total: ", addTwoNums(30, 54))

# def compareNums(a, b):
#     if a > b:
#         return a
#     else: return b
# print(compareNums(10, 20))

def addTwoNums(a, b):
    numSum = a + b
    return numSum

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

solution = (addTwoNums(num1, num2))

print(f"The  answer to {num1} + {num2} is:  {solution}")
