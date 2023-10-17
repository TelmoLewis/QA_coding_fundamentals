import random

def get_user_choice():
    while True:
        user_choice = input("choose Rock, Paper or Scissors: ").strip().lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice!!! Please choose rock, paper or scissors")

def get_computer_choice():
   return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
   outcomes = {("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")}
   if user_choice == computer_choice:
       return "Its a draw!!!"
   if (user_choice, computer_choice) in outcomes:
       return "You win!!!"
   else:
       print("Computer Wins!!!")

user_wins = 0
computer_wins = 0
draw = 0
rounds_played = 0

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You choose {user_choice}")
    print(f"Computer choose {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    if "You win!!!" in result:
        user_wins += 1
    elif "Computer wins!!!" in result:
        computer_wins += 1
    else:
        draw += 1

    rounds_played += 1

    print(f"User wins: {user_wins}, Computer wins: {computer_wins}, Draw: {draw}, Rounds played: {rounds_played}")

    play_again = input("Play again (YES/NO): ").strip().lower()
    if play_again != "yes":
        print("Goodbye!!!")
        break
