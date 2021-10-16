# chr()  -  takes a decimal and returns the ASCII equivalent.
# ord()  - Takes a character and returns the decimal equivalent.

varMsg = ""
varNum = int(input("Enter a number"))
varConversion = chr(varNum)
varMsg = varMsg + varConversion
print(varMsg)