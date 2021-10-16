print("Hello \nthis will print in a new line\n" * 3)

# num1,num2=10,5
# print(num1, num2, sep=',')

name = "paul"
score = 94.5234
print(type(score))
print(type(name)) # Type function prints the datatype being used

"""Format print statement"""

print("hello ", name, "your score is ", score)

"""Use of  placeholders"""

print("Using percentage signs: score is %s, your score  is %f"%(name, score))
print("score is %s, your score  is %.2f"%(name, score))

"""Use curly braces {} as placeholder"""
name = "paul"
score = 94.5234
print("Your name is {0}, and your score is {1}".format(name, score))  # Used as Indexes, but must define 
print("Your name is {0}, and your score is {1}".format(name, score))  # Used as Indexes, but must define 
