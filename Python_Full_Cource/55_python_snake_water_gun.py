import random

# Function to check who wins
def check_win(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "snake" and computer_choice == "water") or \
         (player_choice == "water" and computer_choice == "gun") or \
         (player_choice == "gun" and computer_choice == "snake"):
        return "You win!"
    else:
        return "Computer wins!"

# Main game function
def play_game():
    choices = ["snake", "water", "gun"]
    while True:
        try:
            player_choice = input("Enter your choice (snake, water, gun) or -1 to quit: ").lower()
            if player_choice == "-1":
                print("Thanks for playing! Goodbye!")
                break
            if player_choice not in choices:
                raise ValueError("Invalid choice! Please choose snake, water, or gun.")
            
            computer_choice = random.choice(choices)
            print(f"Computer chose: {computer_choice}")
            
            # Check result
            result = check_win(player_choice, computer_choice)
            print(result)
        
        except ValueError as e:
            print(e)

# Start the game
if __name__ == "__main__":
    play_game()
