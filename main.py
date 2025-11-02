import random

choice = ("rock", "paper", "scissors")
gameRunning = True

while gameRunning:

    player = None
    computer = random.choice(choice)

    while player not in choice:
        player = input("Rock, paper, scissors? ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie")
    elif player == "rock" and computer == "scissors":
        print("Player Won!")
    elif computer == "rock" and player == "scissors":
        print("Computer Wins!")
    elif player == "paper" and computer == "rock":
        print("Player Wins!")
    elif player == "rock" and computer == "paper":
        print("Computer Wins")
    elif player == "scissors" and computer == "paper":
        print("Player Wins!")
    else:
        print("Computer Wins!")

    playAgain = input("Play again? (y/n) ")
    if playAgain == "y":
        break
    elif playAgain == "n":
        gameRunning = False
    else:
        print("Please type y/n")
print("Thank you for playing!")

      