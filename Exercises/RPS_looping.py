from random import choice


user_count = 0
computer_count = 0
user = input(
    "<<Rock>>\n<<Papper>>\n<<Scissors>>\nPress (r\p\s)\nPress <stop> to exit\n"
)


while user != "stop":  # When user input is "stop" the loop breaks
    rps = ["r", "p", "s"]
    computer = choice(rps)  # The computer chooses at random from the above list

    print(computer)
    if user == "r" and computer == "p":
        print("The computer wins!")
        computer_count += (
            1  # after each combination of user-computer choices the win count increases
        )
        user = input("Press <stop> to exit or choose again (r\p\s)\n")
    elif user == "r" and computer == "s":
        print("You win!")
        user_count += 1
        user = input("Press <stop> to exit or choose again (r\p\s)\n")
    elif user == "p" and computer == "r":
        print("You win!")
        user_count += 1
        user = input("Press <stop> to exit or choose again (r\p\s)\n")
    elif user == "p" and computer == "s":
        print("The computer wins!")
        computer_count += 1
        user = input("Press <stop> to exit or choose again (r\p\s)\n")
    elif user == "s" and computer == "r":
        print("The computer wins!")
        computer_count += 1
        user = input("Press <stop> to exit or choose again (r\p\s)\n")
    elif user == "s" and computer == "p":
        print("You win!")
        user_count += 1
        user = input("Press <stop> to exit or choose again (r\p\s)\n")
    elif user == computer:
        print("It's a tie!")
        user = input("Press <stop> to exit or choose again (r\p\s)\n")
    else:
        print("Something went wrong!")
        user = input("Press <stop> to exit or choose again (r\p\s)\n")


print(
    "Game Over\nThe final score is \nPlayer : ",
    user_count,
    "\nComputer : ",
    computer_count,
)
if user_count > computer_count:  # Test for the winner of most games after the loop ends
    print("You are the winner!")
    quit()
elif user_count < computer_count:
    print("The computer is the winner!")
    quit()
else:
    print("It's a tie!")
    quit()
