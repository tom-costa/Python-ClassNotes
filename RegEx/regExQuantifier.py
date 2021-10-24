# sequences characters to match a single character in a given string
# \d is any digits between = 0-9 (So this matches a single character in a given string which should be a digit.)
# \D = non digit characters
# \s =white space 
# \S = non white space,
# \w = any alpha numeric char(any digits/character) = A-Z
# \W = non alpha numeric char
# \b = space around words
# \A = search at begining of string, 
# \Z = search at end of string.

import re
sentence = "Timmy the fish, Take up one brilliant 10 idea open the orb, I mean one 9 idea at a time, 7 oops owner"

sResult = re.findall(r'o\w+', sentence)
print(sResult)

sResult1 = re.findall(r'o\w*', sentence)
print(sResult1)

sResult2 = re.findall(r'o\w?', sentence)
print(sResult2)

sResult3 = re.findall(r'i\w{3}', sentence)
print(sResult3)

# min, max values:
sResult4 = re.findall(r'i\w{1,2}', sentence)
print(sResult4)