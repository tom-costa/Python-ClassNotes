guess = 3 
notGuessed = True
while notGuessed:
    number = int(input("Guess a number: "))
    if number == guess:
        print("Success")
        break
    print(f"You guessed {number}")
        
    
