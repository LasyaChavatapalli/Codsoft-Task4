import random

def to_get_user_choice():
    while True:
        user_choice = input("Enter rock, paper, or scissors: ").strip().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice! Please enter rock, paper, or scissors.")

def to_get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def finding_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        print("\nLet's play Rock, Paper, Scissors!")
        user_choice = to_get_user_choice()
        computer_choice = to_get_computer_choice()
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = finding_winner(user_choice, computer_choice)
        print(result)
        
        if 'You' in result:
            user_score += 1
        elif 'Computer' in result:
            computer_score += 1
        
        print(f"\nScore - You: {user_score} | Computer: {computer_score}")
        
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("\nThanks for playing!")
            break

play_game()