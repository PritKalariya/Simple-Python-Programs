import random

# Setup
game_list = ["Rock", "Paper", "Scissors"]
computer = c = 0
command = p = 0
print(f"Scores: Computer = {c} & Player = {p}")

# Main Loop
while True:
    computer_choice = random.choice(game_list)
    command = input("Rock, Paper, Scissors or Quit: ")

    if command == computer_choice:
        print("\nTie\n")
    elif command == "Rock":
        if computer_choice == "Scissors":
            print("\nPlayer Won!\n")
            p += 1
        else:
            print("\nComputer Won!")
            c += 1
    elif command == "Paper":
        if computer_choice == "Rock":
            print("\nPlayer Won!")
            p += 1
        else:
            print("\nComputer Won!")
            c += 1
    elif command == "Scissors":
        if computer_choice == "Paper":
            print("\nPlayer Won!")
            p += 1
        else:
            print("\nComputer Won!")
            c += 1
    elif command == "Quit":
        break
    else:
        print("Invalid Input.")

    # Display
    print(f"Player: {command}")
    print(f"Computer: {computer_choice}")
    print("")
    print(f"Scores: Computer = {c} & Player = {p}")
    print("")