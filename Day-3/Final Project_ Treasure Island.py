## Treasure Island

# Instructions
# Make your own "Choose Your Own Adventure" game. 
# Use conditionals such as if, else, and elif statements to lay out the logic and the story's path in your program.

# Storyline for the adventure game:

# 1. The game starts with the player finding themselves in a mysterious forest. 
#    They can choose to go either "north" towards the mountains or "south" towards the river.

# 2. If they go "north", they encounter a grumpy troll guarding a bridge. 
#    They can choose to "fight" the troll or "run" back to the forest.
#     - If they choose to "fight", they find a magical sword and win. 
#     - They cross the bridge and reach a castle where they find a treasure chest. They win the game.
#     - If they choose to "run", they find themselves back at the start of the forest and the game restarts.

# 3. If they go "south", they reach a river where they find a boat. 
#    They can choose to "swim" across the river or "use" the boat.
#     - If they choose to "swim", they get caught in the current and lose the game.
#     - If they choose to "use" the boat, they safely cross the river and reach an island where they find a treasure chest. 
# They win the game.

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
starting_direction = input("Which way do you want to go? north towards the mountains or south towards the river? ").lower()
if starting_direction == 'north':
    print("encounter a grumpy troll guarding a bridge.")
    run_or_fight = input("do you want to run or fight? ").lower()
    if run_or_fight == 'fight':
        print("here's your treasure chest. you win!!")
    else:
        print("you lose. start again")
else:
    print("you need to cross this river")
    swim_or_boat = input("do you want to swim across the river or use the boat? ").lower()
    if swim_or_boat == 'swim':
        print("crocodile!!! you lose!")
    else:
        print("you have safely crossed the river. here's your treasure chest. you win!!")
