##Python Dictionaries

# programming_dictionary = {
#   "Bug": "An error in a program that prevents the program from running as expected.", 
#   "Function": "A piece of code that you can easily call over and over again.",
# }

# #Retrieving items from dictionary.
# # print(programming_dictionary["Function"])

# #Adding new items to dictionary.
# programming_dictionary["Loop"] = "The action of doing something over and over again."

# #Create an empty dictionary.
# empty_dictionary = {}

# #Wipe an existing dictionary
# # programming_dictionary = {}
# # print(programming_dictionary)

# #Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer."
# # print(programming_dictionary)

# #Loop through a dictionary
# # for key in programming_dictionary:
# #   print(key)
# #   print(programming_dictionary[key])

# #######################################

# #Nesting 
# capitals = {
#   "France": "Paris",
#   "Germany": "Berlin",
# }

# #Nesting a List in a Dictionary

# travel_log = {
#   "France": ["Paris", "Lille", "Dijon"],
#   "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }

# #Nesting Dictionary in a Dictionary

# travel_log = {
#   "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#   "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
# }

# #Nesting Dictionaries in Lists

# travel_log = [
# {
#   "country": "France", 
#   "cities_visited": ["Paris", "Lille", "Dijon"], 
#   "total_visits": 12,
# },
# {
#   "country": "Germany",
#   "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#   "total_visits": 5,
# },
# ]

## Exercise 1: grading program

# Grading Program
# Instructions
# You have access to a database of student_scores in the format of a dictionary. 
# The keys in student_scores are the names of the students and the values are their exam scores.

# Write a program that converts their scores to grades. 
# By the end of your program, you should have a new dictionary called student_grades 
# that should contain student names for keys and their grades for values. 
# The final version of the student_grades dictionary will be checked.

# DO NOT modify lines 1-7 to change the existing student_scores dictionary.
# DO NOT write any print statements.


# Expected Output
# '{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'

# Hint
# Remember that looping through a Dictionary will only give you the keys and not the values.
# If in doubt as to why your code is not doing what you expected, you can always print out the intermediate values.

# At the end of your program, the print statement will show the final student_scores dictionary, do not change this.

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# This is the scoring criteria:
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"
#TODO-1: Create an empty dictionary called student_grades.
#TODO-2: Write your code below to add the grades to student_grades.
student_grades = {}


for student in student_scores:
    score = student_scores[student]
    if score > 90:
        grade = 'Outstanding'
    elif score >80 < 90:
        grade = 'Exceeds Expectations'
    elif score >70 < 80:
        grade = 'Acceptable'
    elif score <=70:
        grade = 'Fail'
    student_grades[student] = grade

print(student_grades)





