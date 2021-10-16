
s1 = "    AmigosBootcamp   "
s2  = "Python"

print(s1[3], s2[-1])

print(f"There are", len(s2), "characters in", s2)

# Slicing the List:

print(s2[1:4])
print(s2[2:])
print(s2[:3])
# Using negative Index
print(s2[-4:-1])
# Using Step
print(s1[0:15:2])

# Print in reverse order
print(s2[7::-1])
print(s1[::-1])

# Stripping spaces

print(s1.strip())
print(s1.lstrip())
print(s1.rstrip())

# Find/ Locate word in sequence

s4 = "Today is a beautiful day"
print(s4.find("day"))
print(s4.find("day",0,len(s4)))
print(s4.count("a"))
print(s4.count(""))
print(s4.replace("day", "weather"))
