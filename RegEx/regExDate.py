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
sentence = "Timmy the fish 18-10-2020, Take up one brilliant 10 idea open the orb,18-10-2020"

# \d to search for digits, then the pattern is specified by the number of chars in the curly brackets.
sResult = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', sentence)
print(sResult)

