# A simple program to play a game of Rock, paper, scissors
# against the computer!

from random import choice

rand_list = ["Rock", "Paper", "Scissors"]

print("...Rock...\n...Paper...\n...Scissors...")
user1 = input("Enter Player 1's choice\n")
user2 = choice(rand_list)  # user2 is computer that chooses  at random from rand_list.
print("Player 2 choosed ", user2)

if user1 == "Rock" and user2 == "Paper":
    print("Player 1  Wins!")
elif user1 == "Rock" and user2 == "Scissors":
    print("Player 2 Wins!")
elif user1 == "Paper" and user2 == "Rock":
    print("Player 1 Wins!")
elif user1 == "Paper" and user2 == "Scissors":
    print("Player 2 Wins")
elif user1 == "Scissors" and user2 == "Rock":
    print("Player 2 Wins")
elif user1 == "Scissors" and user2 == "Paper":
    print("Player 1 Wins!")
elif user1 == user2:
    print("It's a tie")
else:
    print(
        "Something went wrong!"
    )  # In case the user input is anything other than "Rock", "Paper", "Scissors".

# There is no looping in this version of the game.
