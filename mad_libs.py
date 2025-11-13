import random

'''
guess = int(input("I'm thinking of number between 1 and 10. Can you guess it? "))
secret_number = random.randint(1, 10)

match guess:
    case _ if guess == secret_number:
            print("Congratulations, you guessed it")
            
           ask = input("Play again? (yes/no): ").lower()
            if ask == "yes":
                print("...(new game starts)")
            else:
                print("Game over!!!")
                
    case 2:
        if guess > secret_number:
            print("Oops, your guess is a bit low. Give it another shot")
    case  3:
        if guess < secret_number:
            print("Nope, your guess is a bit low. Give it another shot!")
'''         
    # Generate a secret number between 1 and 10
secret_number = random.randint(1, 2)
 
# Variable checheck if user guessed correctly
guessed_correctly = False

# Counter to track the number of guessed
guess_count = 0

# Keep asking for guesses
while not guessed_correctly:
   # Get user's guess
    guess = int(input("Guess a number between 1 and 2: "))
    
    # increment the guess counter
    guess_count = guess_count + 1
    
# Match the guess with the secret number using match-case
match guess:
    case _ if guess == secret_number:
        print("Congratulations, you guessed it!")
        guessed_correctly = True
    case _ if guess > secret_number:
        print("Oops, your guess is a bit high. Try again!")
    case _ if guess < secret_number:
        print("Nope, your guess is a bit low. Give it another shot!")

# Show the secret number
print(f"The secret number was: {secret_number}")
print(f"It took you {guess_count} guesses to win!")