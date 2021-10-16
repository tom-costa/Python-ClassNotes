varWord = "Bootcamp"
count = 0

character = input(("Enter a character: "))

for letter in varWord:
    if letter == character:
        count = count + 1
print(f"The letter {character} appears:  {count} times")

# PRACTICE: To Do: add the ELSE statement!!