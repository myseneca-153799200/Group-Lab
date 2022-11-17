#!/usr/bin/env python3
#Date Created = 2022/11/17

import random

options = ("rock", "paper", "scissors")
gameruns = True

while gameruns:

    user = None
    system = random.choice(options)

    while user not in options:
        user = input("Please select from (rock, paper, scissors): ")

    print(f"user: {user}")
    print(f"system: {system}")

    if user == system:
        print("Tie! Well Played!")
    elif user == "rock" and system == "scissors":
        print("You win! Well Played!")
    elif user == "paper" and system == "rock":
        print("You win! Well Played")
    elif user == "scissors" and system == "paper":
        print("You win! Well Played")
    else:
        print("You lose! Better Luck next time!!!!")

    if not input("Would you like to play again ? (y/n): ").lower() == "y":
        gameruns = False

print("Hope you enjoyed the game!")
