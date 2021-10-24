
# Set is an unordered list, when it prints it does not stick to the order in the code.
# So we cannot access a key using Index value
# It also DOES NOT show duplicate values!
# You can add (update) and remove items, but cannot REPLACE, as there's no fixed Index.

set1 = {10, 20, 43, "xyz", "abc"}
print(set1)
print(type(set1))

# To add items to a set, use .update() and always use [ ]
set1.update([1, 4, "bcd"])
print(set1)

set2={4, 7, "paul", "peter"}
set1.update(set2)
print(set1)

# To remove items from set, use .remove()

set1.remove("peter")
print(set1)

for i in set2:
    print(i)

# Method .add() can only add 1 item at a time. Use .update() for adding multiple.
set1.add("Python")
print(set1)

set3 = {21, 22, 23, "John"}
print(set3)

# When you FREEZE a set, you cannot add or remove from it.
fSet3 = frozenset(set3)
fSet3.add("HTML")
print(fSet3)