gamersList = []

add_gamers = True

while add_gamers:
    userName = input("Enter your username: ")
    userPass = input("Enter your password: ")
    userScore = input("Enter your current score: ")
    userHscore = input("Enter your username: ")

    gamer = {"userName" : userName,
             "userPass" : userPass,
             "userScore" : userScore,
             "userHscore" : userHscore
    }

    gamersList.append(gamer)
    answer = input("Would you like to add another gamer? Y/N ")

    if answer == "N":
        add_gamers = False

print(gamersList)

record = int(input("Enter the record number you want to search for? "))
gamer = (gamersList[record])
gamerField = input("Enter the field name/ attribute you want to display")
print(gamer[gamerField])
