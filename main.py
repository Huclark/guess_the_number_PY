import random # module used to generate random numbers

#define the function
def guess_the_number():
    random_num = random.randint(1, 100) # generate random positive integer from 1 to 100
    max_trials = 5 # set maximum number of attempts to 5
    
    print("Welcome to the Guess the Number Game!")
    print(f"I'm thinking of a number between 1 and 100.")

    no_of_tries = 0
    while no_of_tries < max_trials:
        try:
            guess = int(input("Take a guess: ")) # store user input
            
            # compare user input with random number generated
            if guess == random_num:
                print(f"Congratulations! You guessed the right number; which is {random_num}")
                break
            
            elif guess < random_num:
                print("Try Again! Your guess was too low!")
                
            else:
                print("Try Again! Your guess was too high")
                
            no_of_tries += 1
            
        except ValueError: # handle cases for non-integer input
            print("Invalid input. Please enter a number")
            
    if no_of_tries == max_trials: 
        print(f"Game over! The secret number was {random_num}")
    
    play_again = input("Do you want to play again? (Yes/N0): ")
    if play_again.lower() == "yes": 
        guess_the_number()
    
    else:
        print("Thanks for playing")

guess_the_number()        
