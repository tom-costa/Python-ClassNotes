from functools import reduce
lstNums = [1, 2, 3, 4, 5, 6, 7, 13, 20, 23, 9]

lstResult = reduce(lambda x, y: x+y, lstNums)
print(f"Sum = {lstResult}")








