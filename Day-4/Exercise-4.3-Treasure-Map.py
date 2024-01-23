## Nested Lists
# these are lists within lists, eg;

# dirty_dozen = ['Strawberries', 'Spinach', 'Kale', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears', 'Tomatoes', 'Celery', 'Potatoes']
# fruits = ['Strawberries', 'Apples','Grapes', 'Peaches', 'Cherries', 'Pears', 'Nectarines']
# veges = ['Spinach', 'Kale','Tomatoes','Celery', 'Potatoes' ]
# dirty_dozen = [fruits,veges]
# print(dirty_dozen)

# Treasure Map

# Instructions
# You are going to write a program which will mark a spot with an X.
# This map contains a nested list. When map is printed this is what the nested list looks like:

# ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']

# In the starting code, we have used new lines (\n) to format the three rows into a square, like this:

# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']

# This is to try and simulate the coordinates on a real map.
# Your job is to write a program that allows you to mark a square on the map using a two-digit system. 
# The first digit for the input will specify the column (the position on the horizontal axis). 
# The second digit in the input will specify the row number (the position on the vertical axis).
# First your program must take the user input and convert it to a usable format.
# Next, you need to use it to update your nested list with an "x".

# Example Input 1
# column 2, row 3 would be entered as:
# 23

# Example Output 1
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️',  'X', '⬜️']

# Example Input 2
# column 3, row 1 would be entered as:
# 31

# Example Output 2
# ['⬜️', '⬜️', 'X']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = str(input("Where do you want to put the treasure? "))
coordinates = []
column = int(position[0])
row = position[1]
print(coordinates.append(column))
