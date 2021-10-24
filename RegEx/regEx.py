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
sentence = "Take up one brilliant idea, I mean one idea at a time, oops owner"

# Below we are looking for a word that had "o" as the first char and then +3 more chars after.
# It will only bring the first instance of it.
sResult = re.search(r'o\w\w\w\w', sentence)
print(sResult.group())

# Using .findall it returns with all results it finds. That includes parts of words that match.
sResult1 = re.findall(r'o\w\w', sentence)
print(sResult1)