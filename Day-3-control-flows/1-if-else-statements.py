# # Control Flow with if _ else and Conditional Operators

## Odd or Even

# Instructions
# Write a program that works out whether if a given number is an odd or even number.

# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.
# Example Input 1
# 43
# Example Output 1
# This is an odd number.

# Example Input 2
# 94
# Example Output 2
# This is an even number.

number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")
