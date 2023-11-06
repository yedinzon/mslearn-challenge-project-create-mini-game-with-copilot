# Import the random module
import random

# Define the options
options = ["rock", "paper", "scissors"]

# Define the rules
rules = {
    "rock": "scissors", # Rock beats scissors
    "paper": "rock", # Paper beats rock
    "scissors": "paper" # Scissors beats paper
}

score = {
    "rounds": 0,
    "wins": 0
}

# Define a function to get the user's choice
def get_user_choice():
    # Prompt the user to enter their choice
    user_choice = input("Enter a choice (rock, paper, scissors): ")
    # Validate the user's input
    while user_choice not in options:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter a choice (rock, paper, scissors): ")
    # Return the user's choice
    return user_choice

# Define a function to get the computer's choice
def get_computer_choice():
    # Use the random module to choose a random option
    computer_choice = random.choice(options)
    # Return the computer's choice
    return computer_choice

# Define a function to determine the winner
def determine_winner(user_choice, computer_choice):
    # Print the user's and the computer's choices
    print(f"You chose {user_choice}.")
    print(f"The computer chose {computer_choice}.")
    # Compare the choices and determine the winner
    if user_choice == computer_choice:
        print("It's a tie.")
    elif rules[user_choice] == computer_choice:
         # Count the wins
        score["wins"] += 1
        print("You win!")
    else:
        print("You lose.")

# Define a main function to run the game
def main():
    # Set a flag to control the game loop
    play_again = True
    # Loop until the user wants to quit
    while play_again:
        # Count the rounds
        score["rounds"] += 1
        # Get the user's and the computer's choices
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        # Determine the winner
        determine_winner(user_choice, computer_choice)
        # Ask the user if they want to play again
        answer = input("Do you want to play again? (yes/no): ")
        # Validate the user's input
        while answer not in ["yes", "no"]:
            print("Invalid answer. Please type yes or no.")
            answer = input("Do you want to play again? (yes/no): ")
        # Set the flag to False if the user wants to quit
        if answer == "no":
            play_again = False
            print(f"Your score: {score['wins']}/{score['rounds']}")
            print("Thanks for playing. Goodbye!")

# Call the main function to start the game
main()
