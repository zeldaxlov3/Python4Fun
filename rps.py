#### Rock Paper Scissors ####
import random

list1 = ["rock", "paper", "scissors"]
move_player = input("move_player: ")
move_computer = random.choice(list1)

print(move_player)
print(move_computer)

print(f"\You have chosen {move_player}, computer has chosen {move_computer}")

if move_player == move_computer:
    print(f"They both chose {move_player}, it's a tie")
elif move_player == "rock":
    if move_computer == "scissors":
        print("Player wins, computer loses")
    else:
        print("Paper covers rock! You lose.")

elif move_player == "scissors":
    if move_computer == "paper":
        print("Player wins, computer loses")
    else:
        print("Rock smashes scissors! You lose.")
elif move_player == "paper":
    if move_computer == "rock":
        print("paper fucks rocki player wins")
    else:
        print("computer wins")
