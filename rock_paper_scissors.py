import random

def get_user_choice():
    while True:
        user_choice = input("Choose Rock, Paper, or Scissors: ").strip().lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice!!! Please choose rock, paper, or scissors")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    outcomes = {("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")}
    if user_choice == computer_choice:
        return "It's a draw!!!"
    elif (user_choice, computer_choice) in outcomes:
        return "You win!!!"
    else:
        return "Computer Wins!!!"

user_wins = 0
computer_wins = 0
draw = 0
rounds_played = 0

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You choose {user_choice}")
    print(f"Computer chooses {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    if result == "You win!!!":
        user_wins += 1
    elif result == "Computer Wins!!!":
        computer_wins += 1
    else:
        draw += 1

    rounds_played += 1

    print(f"User wins: {user_wins}, Computer wins: {computer_wins}, Draw: {draw}, Rounds played: {rounds_played}")

    play_again = input("Play again (YES/NO): ").strip().lower()
    if play_again != "yes":
        print("Goodbye!!!")
        break
