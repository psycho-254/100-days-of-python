# Data types

# strings - "hello"
#   print("hello"[2]) - this method of pulling one character in a string is called subscripting

# integers - numbers without any decimal place
#   0123456789

# float - decimal numbers
#   234.986

# boolean - True or False
#   used to prove if a statement is true or false


# print(70 + float("100.5"))


# Instructions
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# Warning. Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.


# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
total = int(two_digit_number[0]) + int(two_digit_number[1])
print(total)