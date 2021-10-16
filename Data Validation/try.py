try:
    print("Enter a number: ")
    number = int(input())
except ValueError:
    print("Enter a NUMBER (no other characters): ")
    number = int(input())
print(f"print the {number}")