#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

import random

chosen_word = random.choice(word_list)
print(chosen_word)
guess = input("Guess a letter: ").lower()

# for n in range(0, len(chosen_word)):
#     if guess == chosen_word[n]:
#         print(guess)

#Step 2


#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

display = []
for n in range(0, len(chosen_word)):
    display += '_'
    if guess == chosen_word[n]:
        display[n] = chosen_word[n]
print(display)


#Step 3

#TODO-1: - Use a while loop to let the user guess again. 
# The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). 
# Then you can tell the user they've won.

# while len('_') in display:
#     for n in range(0, len(chosen_word)):
#         display += '_'
#         if guess == chosen_word[n]:
#             display[n] = chosen_word[n]
#             display -= '_'
#     print(display)

while "_" in display:
    guess = input("Guess another letter: ").lower()
    for n in range(0, len(chosen_word)):
        if guess == chosen_word[n]:
            display[n] = chosen_word[n]
        else:
            display[n] -= 1
    print(display)

    if '_' not in display:
        print("you won")
