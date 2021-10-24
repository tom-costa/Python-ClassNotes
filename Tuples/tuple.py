# Tuple is a colletion that is ordered and UNMUTABLE.
# To add to a Tuple you cannot use add or update, you need to append the values via concatenation.


tuple1 = (21, 10, 30, "abc", "john")
print(type(tuple1))
tuple2 = (21, 6, 7, 9, 35)

maxTuple2 = max(tuple2)
minTuple2 = min(tuple2)
tuple2Sorted = sorted(tuple2)
tuple2RevSorted = sorted(tuple2, reverse=True)

print(f"max number from tuple: {maxTuple2}")
print(f"min number from tuple: {minTuple2}")
print(f"Sorted in ascending order: {tuple2Sorted}")
print(f"Sorted in ascending order: {tuple2RevSorted}")

for x in tuple2:
    print(x)

for x in tuple1:
    print(x)


# Manipulate tuple based on index position
print(tuple1.index("abc"))
