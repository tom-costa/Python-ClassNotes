list1 = ["Hello", "Good morning", "Sayonara", "Hola"]

list1.append("Ciao")
print(list1)

list1.insert(1, "See you later")
print(list1)

print(list1.pop(3))

list2 = [10, 20, "Javascript", 3.67]
del(list2[1])
print(list2)

#  Min, Max, Sort,  Reverse
list3 = [12, 3, 45, 13]

print(max(list3))
print(min(list3))
list3.sort()
print(list3)

list3.sort(reverse=True)
print(list3)

# list3.clear()
# print(list3)

# Remove item from list
list2.remove("Javascript")
print(list2)