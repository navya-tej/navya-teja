import random

def get_user_choice():
    choices = ["rock","paper","scissors"]
    user_choice = input("Enter your choice(rock,paper,or scissors):").lower()
    while user_choice not in choices:
        print("Invalid choice.please choose rock,paper,or scissors.")
        user_choice = input("Enter your choice(rock,paper,or scissors):").lower()

    return user_choice

def get_computer_choice():
    choices = ["rock","paper","scissors"]
    return random.choice(choices)

def determine_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
     return "It is a tie!"

    if((user_choice == "rock"and computer_choice=="scissors")or(user_choice=="paper"and computer_choice=="rock")or(user_choice=="scissors"and computer_choice=="paper")):
     return "You Win!"

    return "Computer Wins!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou choose:{user_choice}")
    print(f"Computer choose:{computer_choice}")

    result = determine_winner(user_choice,computer_choice)
    print(f"\nResult:{result}")
if __name__ == "__main__":
   play_game()
