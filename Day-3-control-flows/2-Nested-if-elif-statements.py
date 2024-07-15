# # Nested if statements and elif statements

# BMI Calculator 2.0

# Instructions
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# Warning you should round the result to the nearest whole number. The interpretation message needs to include the words in bold from the interpretations above. e.g. 
# underweight, normal weight, overweight, obese, clinically obese.

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
BMI = round(weight / (height * height))

if BMI < 18.5:
    print(f"your BMI is {BMI}, you are underweight")
elif BMI > 18.5 and BMI < 25:
    print(f"your BMI is {BMI}, you are normal weight")
elif BMI > 25 and BMI < 30:
    print(f"your BMI is {BMI}, you are slightyly overweight")
elif BMI >30 and BMI < 35:
    print(f"your BMI is {BMI}, you are obese")
else:
    print(f"your BMI is {BMI}, you are clinically obese")

