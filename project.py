import random

print("Welcome to Rock-Paper-Scissors!")
print("Choose: rock, paper, or scissors")

choices = ["rock", "paper", "scissors"]

while True:
    user = input("Your choice: ").lower()

    if user not in choices:
        print("Invalid choice! Try again.\n")
        continue

    computer = random.choice(choices)
    print("Computer chose:", computer)

    # Determine winner
    if user == computer:
        print("It's a tie!\n")
    elif (user == "rock" and computer == "scissors") \
         or (user == "scissors" and computer == "paper") \
         or (user == "paper" and computer == "rock"):
        print("You win!\n")
    else:
        print("Computer wins!\n")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
