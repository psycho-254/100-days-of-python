## Python lists
# list is what you would call a data structure
# it's a way of organizing and storing data in Python. 

# list = [item1, item2, item3, ....]
# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
#  "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", 
# "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", 
# "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", 
# "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", 
# "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", 
# "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
# Exercise
## Who's Paying

# Instructions
# You are going to write a program which will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.
# Important: You are not allowed to use the choice() function.
# Line 8 splits the string names_string into individual names and puts them inside a List called names. 
# For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name

# Example Input
# Angela, Ben, Jenny, Michael, Chloe

# Note: notice that there is a space between the comma and the next name.
# Example Output
# Michael is going to buy the meal today!
# Abdulmuradov, Aliyev, Gadzhiyev, Magomedov, Omarov

import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
no_of_people = len(names)
boss = names[random.randint(0,no_of_people-1)]

print(f"{boss} is going to buy the meal today!")