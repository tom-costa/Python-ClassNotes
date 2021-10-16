varWord  = "Bootcamp"
varUserGuess = ""
varNotguessed = varWord !=  varUserGuess
varGuesses = 0

while varNotguessed and varGuesses < 5:
    if varGuesses == 1:
        varFletter = varWord[0]
        print(f"The First letter of the word is: {varFletter}")
    elif varGuesses == 3:
        varLletter = varWord[7]
        print(f"The Last letter of the word is: {varLletter}")
    varUserGuess = input("Guess the word")
    varGuesses = varGuesses + 1
    arNotguessed = varWord !=  varUserGuess
if  varWord == varUserGuess:
    print("You guess correct")
else:
    print("Incorrect guess")