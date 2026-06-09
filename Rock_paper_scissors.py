import random

choices = ("rock", "paper", "scissors")
player =input("Choose rock, paper, or scissors: ").lower()

if player not in choices:
    print("Invalid choice. Please choose rock, paper, or scissors.")
else:
    computer_choice = random.choice(choices)
    print(f"Player Chose: {player}")
    print(f"Computer Chose: {computer_choice}")

    if player == computer_choice:
        print("draw!")
    elif player == "rock" and computer_choice == "scissors":
        print("You win!")
    elif player == "paper" and computer_choice == "rock":
        print("You win!")
    elif player == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("Computer wins!")
