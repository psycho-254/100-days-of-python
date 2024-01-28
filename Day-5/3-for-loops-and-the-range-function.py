## for loops and the range() function

# for number in range(1,10):
#     print(number) 
# specified range is not inclusive of the last number unless you add 1
# you can also specify the step range by adding a third number: range(1,10,3)

# add all numbers from 1 to 100

# total = 0
# for number in range(1,101):
#     total += number
# print(total)

## Adding Evens
# Instructions
# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. 
# Thus, the first even number would be 2 and the last one is 100:

# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

# Important, there should only be 1 print statement in your console output. 
# It should just print the final total and not every step of the calculation.

total = 0
for number in range(2,101,2):
    total += number
print(total)
