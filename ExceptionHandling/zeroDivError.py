try:
    num1,num2 = [int(num) for num in input("Enter two numbers: ").split()]
    num3 = num1/num2
    print(num3)
except ZeroDivisionError:
    print("You can't divide a number by zero\n Please enter a non zero number")
print("print when there is no error")