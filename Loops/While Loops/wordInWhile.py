print("Guess the word:")

guessWord = input()
while guessWord != "Bootcamp":
    print("Try again...")
    guessWord = input()
print(f"Well done, you guess the word: {guessWord}")