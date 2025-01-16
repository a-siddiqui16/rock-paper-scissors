import random

array = ["rock", "paper", "scissors"]

def choices():
    player_choice = input("Enter your choice (rock, paper or scissors: ").lower()

    computer_choice = random.choice(array)

    choices = {"player": player_choice, "computer": computer_choice}

    return choices


def get_winner(player, computer):

    print(f"You chose {player} and the computer chose {computer}")
    if player == computer:
        return "Its a tie!"

    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors, you win!"
        else:
            return "Paper covers rock, you lose!"

    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock, you win!"
        else:
            return "Scissors cuts paper, you lose!"

    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper, you win!"
        else:
            return "Rock smashes scissors, you lose!"


result = choices()

final_result = get_winner(result["player"], result["computer"])

print(final_result)





                          

    
