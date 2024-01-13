#  Mathematical operations
# the order of priorities is:

#   PEMDAS  
# () - parentheses
# ** - exponents
# * - multiplication
# / - division
# + - adition
# - _ subtraction
# 
## *&/ are equal and the sign that is on the left is given priority whenever theyre together in one statement
## +&- the above rule applies here too

## BMI Calculator

# Instructions
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of some's weight taking into account their height. e.g. 
# If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# Warning you should convert the result to a whole number.

# Hint
# Check the data type of the inputs.
# Try to use the exponent operator in your code.
# Remember PEMDAS.
# Remember to convert your result to a whole number (int).

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

Height = float(height)
Weight = int(weight)

BMI = Weight / (Height ** Height)
print(int(BMI))