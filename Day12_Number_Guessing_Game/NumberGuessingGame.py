import random 

def NumberGuess():
    print("Welcome To Number Guessing Game!")
    the_number = random.randint(1,100)
    print("I'm thinking of a number between 1 to 100")
    difficulty = input("Choose difficulty 'easy' or 'hard': ")
    
    if difficulty == 'hard':
        attempts = 5
        for i in range(5):
            print(f"You have {attempts} attempts left to guess the Number.")
            guess = int(input("Make a guess: "))
            if guess == the_number:
                print(f"You got it! The anser was {the_number}")
                print("Refresh page to restart")
                break
            elif guess < the_number:
                print("Too Low!")
                attempts-= 1
            else:
                attempts-= 1
                print("Too High!")
    elif difficulty == 'easy':
        attempts = 10
        for i in range(10):
            print(f"You have {attempts} attempts left to guess the Number.")
            guess = int(input("Make a guess: "))
            if guess == the_number:
                print(f"You got it! The anser was {the_number}")
                print("Refresh page to restart")
                break
            elif guess < the_number:
                print("Too Low!")
                attempts-= 1
            else:
                attempts-= 1
                print("Too High!")
    else:
        print("Type a valid input.")
        
NumberGuess()
                