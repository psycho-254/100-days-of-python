## Prime Number checker

# Instructions
# You need to write a function that checks whether if the number passed into it is a prime number or not.
# Example Input 1
# 73
# Example Output 1
# It's a prime number.

# Example Input 2
# 75
# Example Output 2
# It's not a prime number.

# Hint
# Make sure you name your function/parameters the same as when it's called on the last line of code.

n = int(input("Check this number: "))
def prime_checker(number):
    is_prime = True
    if n == 1:
        print("It's not a prime number.")
    else:
        for i in range(2,number):
            if number % i == 0:   
                is_prime = False
        if is_prime:
            print("It's a prime number.")
        else: 
            print("It's not a prime number.")

prime_checker(number=n)

