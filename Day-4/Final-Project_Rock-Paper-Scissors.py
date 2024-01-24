## Rock Paper Scissors

# Instructions
# Make a rock, paper, scissors game.

# Start the game by asking the player:
# "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

# From there you will need to figure out:
# How you will store the user's input.
# How you will generate a random choice for the computer.
# How you will compare the user's and the computer's choice to determine the winner (or a draw).
# And also how you will give feedback to the player.

# # rules:
# Rock(0) wins against scissors(2).
# Scissors(2) win against paper(1).
# Paper(1) wins against rock(0).

import random
players_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
comps_choice = random.randint(0,2)
if players_choice == 0 and comps_choice == 2 or players_choice == 2 and comps_choice == 1 or players_choice == 1 and comps_choice == 0:
    print("You Win!")
elif players_choice == comps_choice:
    print("It's a Draw")
elif players_choice > 2:
    print("Error! Invalid Input")
else:
    print('You Lose!')































rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
