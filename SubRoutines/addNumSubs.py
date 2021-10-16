# def addNum():
#     num1 = int(input("Enter your first number: "))
#     num2 = int(input("Enter your second number: "))
#     numSum = num1 + num2
#     print(f"The answer to {num1} + {num2} = {numSum}")
# addNum()

# Exercise 2: divide, subtract, multiply two numbers

# def userAnswers():
#     num1 = int(input("Enter your first number: "))
#     num2 = int(input("Enter your second number: "))

# userAnswers()

def divNum():
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    calcNum = num1 / num2
    print(f"The answer to {num1} / {num2} = {calcNum}")
divNum()

def subNum():
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    calcNum1 = num1 - num2
    print(f"The answer to {num1} - {num2} = {calcNum1}")
subNum()

def multNum():
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    calcNum2 = num1 * num2
    print(f"The answer to {num1} * {num2} = {calcNum2}")
multNum()