# learners = {"Name": "",
#             "Course": "",
#             "TelNo": ""}

# learners["Name"] = input("Enter your name: ")
# learners["Course"]  = input("Enter course name: ")
# learners["TelNo"] = input("Enter Tel number: ")

# print(learners)

record1 = {1:"John", 2:"Paul", 3:"Mary", 4:"Kate"}
print(record1)
# print(type(record1))

rKeys = record1.keys()
for i in rKeys:
    print(i)

rValues  = record1.values()
for i in rValues:
    print(i)

print(f"The third item: {record1[3]}")

del record1 [3]

print(record1)