lstNums = [1, 2, 3, 4, 5, 6, 7, 13, 20, 23, 9]

#Exercise: Use lambda to perform cube operation on a number
cube = lambda num: num**4
print(f"The CUBED result is: {cube(3)}")

#Exercise: Use lambda to list the odd numbers from a list of numbers
exercise = list(filter(lambda num: num % 2 == 1, lstNums))
print(f"The ODD numbers result: {exercise}")

#Exercise: Use lambda to filter a list of number (expression of choice = div, subtraction etc)
exercise1 = lambda num1, num2: num1 * num2
print(f"The FILTER result is: {exercise1(9, 5)}")

#Exercise: Use lambda to map function on a list of numbers (expression of choice = div, subtraction etc)
exercise2 = list(map(lambda num: num/2, lstNums))
print(f"The result of MAP is: {exercise2}")

#Exercise: Use lambda to reduce function on a list of numbers
from functools import reduce

exercise3 = reduce(lambda a, b: a+b, lstNums)
print(f"The SUM result is {exercise3}")