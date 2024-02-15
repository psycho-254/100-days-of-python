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
# Use the same wording as the Example Outputs to make sure the tests pass.


n = int(input("Check this number: "))
def prime_checker(number):
    for number in range(2,n +1):
        result = n % number == 0

    if result== 0:   
        print("It's a prime number.")
    else: 
        print("It's not a prime number.")    


prime_checker(number=n)