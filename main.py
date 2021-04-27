# using if else statement

import random

while True:
    guess = input("make ur choice:")
    guess = guess.lower()
    choices = ['stone', 'paper', 'scissors']
    computer = random.choice(choices)
    print("ur guess:", guess)
    print("computer guess:", computer)

    if guess == computer:
        print("game is tie")

    elif guess == "stone":
        if computer == "paper":
            print("u loss")
        else:
            computer == "scissors"
            print("u won!!")

    elif guess == "paper":
        if computer == "scissors":
            print("u loss")
        else:
            computer == "stone"
            print("u won!!")

    elif guess == "scissors":
        if computer == "stone":
            print("u loss")
        else:
            computer == "paper"
            print("u won!!")
    else:
        print("invalid choice")
