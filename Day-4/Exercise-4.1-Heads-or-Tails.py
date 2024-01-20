## Randomisation

# randomu modules are used to generate pseudo-random numbers for various probabilistic distributions.
# below is a link to pyhton documenatation about random modules:
# https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

# What are Python modules?

# Modules are files containing Python definitions and statements.
# They serve as a way to organize code, making it reusable and easier to manage.
# Each module can contain functions, classes, variables, and runnable code.
# You can create your own modules or use the vast collection of built-in and third-party modules available.

# you first need to import the module:

import random

# random_integer = random.randint(1,5)
# random_float = random.random()
# print(random_float + random_integer)


# Exercise
## Heads or Tails

# Instructions
# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
# Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.
# There are many ways of doing this. But to practice what we learnt in the last lesson, 
# you should generate a random number, either 0 or 1. 
# Then use that number to print out Heads or Tails.

# e.g. 1 means Heads 0 means Tails

# Example Output
# Heads
# or
# Tails

number = random.randint(0,1)

if number == 0:
    print("Heads")
else:
    print("Tails")