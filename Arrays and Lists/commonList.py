aList = ["Tom", "Yulia", "Joel", "Abdul", "David", "Ash"]
bList = ["Ashkan", "Ben", "Kavitha", "David", "Jay", "Sajid"]
cList = []

cList = [names for names in aList if names in bList]
print(cList)