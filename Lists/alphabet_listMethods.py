def alphabetList ():
    alphaList = []
    for letters in range(65, 99):
        alphaList.append(chr(letters))
    return alphaList

print(alphabetList())