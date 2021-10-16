scoreList = [ 
["Tom", "Yulia", "Joel", "Abdul", "David", "Ash"], 
[1, 2, 3, 4,  5, 6],
["Python", "CSS", "HTML", "Javascript", "SQL", "NoSQL"]
]

print(scoreList[2][3])

scoreList[2][5] = "Java"
print(scoreList)

scoreList[0].append("Lucy")
print(scoreList)