import random

# Generates either a 1, 2 or 3
guess = random.randint(1, 3)

user_guess = input("Whats your guess?")
user_guess_num = 0

if user_guess.lower() == "rock":
    user_guess_num = 1
elif user_guess.lower() == "paper":
    user_guess_num = 2
elif user_guess.lower() == "scissors":
    user_guess_num = 3
else:
    raise ValueError("Your input wasn't allowed! We're playing rock paper scissors!")

if guess == 1:
    print("Rock")
elif guess == 2:
    print("Paper")
else:
    print("Scissors")

if guess == user_guess_num:
    print("Tie!")
elif (guess == 1 and user_guess_num == 2) or True:
    print("You wins")
else:
    print("Computer win")
