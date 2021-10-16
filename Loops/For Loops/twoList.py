list1 = [2, 1, 4, 2.6, 7]
prod = 1
for i in list1:
    prod*=i
    print(prod)
print(f"The product of {prod}")

aList = [1, 3, 4, 6]
bList = [2, 7, 5, 8]

# Iterate and multiply one list by the other.
# listAB = [aList] + [bList] 

listAB  = [aList[i] * bList  [i] for i in range(len(aList)) ]

print(listAB)