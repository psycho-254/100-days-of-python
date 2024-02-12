#Step 1 

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.


#Step 2

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

#Step 3

#TODO-1: - Use a while loop to let the user guess again. 
# The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). 
# Then you can tell the user they've won.


#step 4

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

#TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

import random
from Hangman_art import stages, logo
from Hangman_words import word_list
chosen_word = random.choice(word_list)
print(logo)
print(chosen_word)
guess = input("Guess a letter: ").lower()
lives = 6
display=[]
guessed_leters = []

for n in range(len(chosen_word)):
        display += '_'
end_game = False
while end_game == False:
    if guess in guessed_leters:
        print(f'you,ve already guessed this letter: {guess}. Try a different letter')
    for n in range(len(chosen_word)):
        if guess == chosen_word[n]:
            display[n] = guess
            guessed_leters.append(guess)
    print(display)
    
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(f'sorry {guess} is not in the word. you lose a life')
    if lives == 0:
        end_game = True
        print('you lost')
    elif '_' not in display:
        end_game = True
        word = ''.join(display)
        print(f'You won! The correct answer is {word}')
        
    else:
        guess = input("Guess another letter: ").lower()   


#Step 5


#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#TODO-2: - Import the stages from hangman_art.py and make this error go away.
#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
#TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
#TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #Join all the elements in the list and turn it into a String.

   

   



















# for n in range(0, len(chosen_word)):

# end_game = False
# while end_game is not True:
#     lives = 6
#     guess = input("Guess another letter: ").lower()
#     for n in range(0, len(chosen_word)):
#         guess = input("Guess a letter: ").lower()
#         display = []
#             display += '_'
#             if guess == chosen_word[n]:
#                 display[n] = chosen_word[n]
#         print(display)
#         if guess != chosen_word[n]:
#             lives -= 1
#             if lives == 0:
#                 end_game = True
#                 print("you lose")
#         elif guess == chosen_word[n]:
#             display[n] = chosen_word[n]
#     print(display)

#     if '_' not in display:
#         print("you won")













# for n in range(0, len(chosen_word)):
#     if guess == chosen_word[n]:
#         print(guess)

# while len('_') in display:
#     for n in range(0, len(chosen_word)):
#         display += '_'
#         if guess == chosen_word[n]:
#             display[n] = chosen_word[n]
#             display -= '_'
#     print(display)

# while "_" in display:
#     guess = input("Guess another letter: ").lower()
#     for n in range(0, len(chosen_word)):
#         if guess == chosen_word[n]:
#             display[n] = chosen_word[n]
#     print(display)

#     if '_' not in display:
#         print("you won")