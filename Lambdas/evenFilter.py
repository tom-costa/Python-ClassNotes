#  declare list o f  numbers

lstNums = [1, 2, 3, 4, 5, 6, 7, 13, 20, 23, 9]

lstResult = list(filter(lambda num: num%2==0, lstNums))

print(f"The list of even numbers {lstResult}")

for i in lstResult:
    print(i)