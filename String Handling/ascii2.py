# chr()  -  takes a decimal and returns the ASCII equivalent.
# ord()  - Takes a character and returns the decimal equivalent.

varMsg = ""
varLetter = input("Enter a letter: ")
varConversion = ord(varLetter)
varMsg = varMsg + str(varConversion)
print(varMsg)

arrayNumbers = [1, 2, 3, 4, 5]  # fixed in size