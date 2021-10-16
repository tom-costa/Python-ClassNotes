# Logical Expressions evaluate to True or False.

# Equal to: "==" is a Comparison Operator. (4 == y)
# What is on the left is equal to what's on the right.

num1 = 15
num2 = 20

print((num1 == 15 and num2 == 20)) # returns True as both sides equal to True
print((num1 == 15 and num2 == 19)) # returns False as one of the sides is False.

# AND condition:
print((num1 == 15 or num2 == 19)) # returns True as one of the sides is True, and the condition is OR.

# OR condition:
print((num1 == 15 or num2 == 19)) # returns True as one of the sides is True, and the condition is OR.

# NOT condition:
print(not(num1 == 15 and num2 ==20)) # This returns False because the numbers ARE equal, when asking if they do NOT equal equal numbers = False