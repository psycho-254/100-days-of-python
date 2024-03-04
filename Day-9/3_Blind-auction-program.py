## Blind Auction

# Instructions
# The objective is to write a program that will collect the names and bids of different people. 
# The program should ask for each bidder's name and their bid individually.

# Welcome to the secret auction program. 
# What is your name?: Angela
# What's your bid?: $123
# Are there any other bidders? Type 'yes' or 'no'.
# yes
# If there are other bidders, the screen should clear, so you can pass your phone to the next person. 
# If there are no more bidders, then the program should display the name of the winner and their winning bid.
# The winner is Elon with a bid of $55000000000
# Use your knowledge of Python dictionaries and loops to solve this challenge.

print("Welcome to the secret auction program.")
bids = []
end_game = True
while end_game:
    name = input("What is your name?: ")
    bid = input("What's your bid?: ")
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
    if other_bidders == 'yes':
        end_game = True
    else:
        end_game = False
        print("The winner is  ")
    def add_bid(bidder, amount):
        new_bid = {
            "name": bidder,
            "amount": amount,
        }
        bids.append(new_bid)
    add_bid(bidder=name, amount=bid)