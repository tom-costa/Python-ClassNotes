try:
    fileOpen = open("logTryExcept.txt", "w")
    num1,num2 = [int(num) for num in input("Enter two numbers: ").split()]
    num3 = num1/num2
    fileOpen.write(f"Writing to file {num3}")
    # print(num3)
except ZeroDivisionError:
    print("You can't divide a number by zero\n Please enter a non zero number")
else:
    print("You have entered a non zero number")  # executes when no error is raised/ thrown.
finally:
    fileOpen.close()
    print("File closed")    
print("print when there is no error")

