#!/usr/bin/env python3
#Date Created = 2022/11/17

import random

options = ("rock", "paper", "scissors")
gameruns = True

while gameruns:

    user = None
    computer = random.choice(options)

    while user not in options:
        user = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")
