# Number Manipulation and F Strings

# how to round-off numbers
# use the function (round) , you can specify the number of decimal points by adding a number after the comma, eg;
#   print(round (8 / 3, 2))

# the flow division sign  (  //  ) is used when you want the result to be an integer and ignore all the decimal points, eg;
#   print(4 // 2) will give you 2 instead of the traditional 2.0

# F - Strings
# used to mix different data types in one statement, eg;

# score = 0
# height = 1.75
# theory = True

# print(f"your score is {score} , height is {height} and your theory is {theory}")

# Your Life in Weeks
# Instructions

# Create a program using maths and f-Strings that tells us 
# how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.

# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

# Example Input
# 56

# Example Output
# You have 12410 days, 1768 weeks, and 408 months left.

# Hint
# There are 365 days in a year, 52 weeks in a year and 12 months in a year.




age = input("What is your current age? ")
Age = int(age)
years_left = 90 - Age
days = years_left * 365
weeks = years_left * 52
months = years_left * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")