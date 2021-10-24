
try:
    num = int(input("Enter a number: "))
    assert num%2 == 0, "You have entered an invalid input or odd number"
except AssertionError as obj:
    print(obj)
print("After assertion")
