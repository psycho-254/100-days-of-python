## functions

def my_function():
  print("hello")

my_function()

#  navigation script for karel the robot using functions
def turn_right():
    turn_left()
    turn_left()
    turn_left()

turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()

## Hurdles race

# Reeborg has entered a hurdles race. Make him run the course, following the path shown.
# What you need to know
# The functions move() and turn_left().
# More advanced
# You may have noticed that your solution has some repeated patterns. 
# If you know how to define functions, define a function named jump() and use it to simplify your program.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    

jump()
jump()
jump()
jump()
jump()
jump()