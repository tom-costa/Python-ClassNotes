# Task6: Number list
# 1.	Create an empty list of numbers
list1 = []
# 2.	add five numbers in the list in no particular order
list1 = [13, 5, 27, 12, 54, 63]
print("Exercise 2: ", list1)
# 3.	add a sixth number in index position 4
list1.insert(4, 6)
print("Exercise 3: ", list1)
# 4.	add a seventh number (don’t use index position)
list1.append(7)
print("Exercise 4: ", list1)
# 5.	sort the list in ascending and descending order
list1.sort()
print("Exercise 5 Sort: ",list1)
list1.sort(reverse=True)
print("Exercise 5 Reverse: ",list1)
# 6.	delete number in index position 1
del(list1[1])
print("Exercise 6: ",list1)
# 7.	count the numbers in the list
print("Exercise 7: ",len(list1))
# 8.	print the max and min number in the list
print("Exercise 8 Max: ",max(list1))
print("Exercise 8 Min: ",min(list1))
# 9.	remove the maximum number in the list(don’t use index position)
list1.remove(max(list1))
print("Exercise 9: ",list1)