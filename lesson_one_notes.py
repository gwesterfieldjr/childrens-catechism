# Agenda

# https://github.com/gwesterfieldjr/childrens-catechism/tree/main

# 1. Comments (how to provide notes in your code to explain to other programmers/your future self about the program)
# 2. Standard Output (how to print or output data to the end user of an application)
# 3. Data Types
#    - String (concatenation)
#    - Boolean (True/False)
#    - Integers (basic math)
#    - Arrays/Lists (size of a list)
#    - Dictionary/Map (key, value store)

# this is a comment. Any text that begins with a # is ignored by the program. 
# It is to provide more context and explanation to the programmer about the code

# print is function to output text to the user of our program
print("Hello World!")

# string: any variable value surrounded by double quotes "example"
# welcome message string
# notice our variable naming. no caps and each work is separated by and underscore (_). 
# This is called snake case which is common way to name variable in python.
welcome_message = "Welcome to the Children's Catechism Quiz!"

# string can contain special characters.
# For our app we need to account for 2 special chars

# new line
new_line = "\n"

# tab
tab_space = "\t"

print(welcome_message)

# concatenation of two strings (combining strings)
print(welcome_message + new_line)
print(tab_space + welcome_message)

# boolean: True or False
# In code we often need to know if something is True or False. Booleans are how we do this.
god_exists = True
print(god_exists)

# testing equality
print(10 == 10)

print("God" == "God")

# True
print(10 > 9)

# False
print(0 > 10)

# integer: any non decimal number
#  score to keep track of the user's score
score = 0
print(score)

score = score + 1
print(score)

score = score + 1
print(score)

# concatenation only works with strings. you can't combine a string and integer type.
#print("Your score is: " + score)

# So you have to convert your integer to a string
print("Your score is: " + str(score))

# list of questions
questions = ["Who made you?", "What else did God make?", "Why did God make you and all things?"]

print(questions)

# list index starts at 0
print(questions[0])
print(questions[1])
print(questions[2])
# index out of bounds error
# print(questions[3])

# get the length of our list
total_questions = len(questions)

print("You will be asked " + str(total_questions) + " questions (multiple choice). Each question has 4 options. Type the number of the option you think is correct. You will be given 1 point for each correct answer.")

questions.append("How can you glorify God?")
print(questions[3])

catechism = {
    "Who made you?": "God",
    "What else did God make?": "All things",
    "Why did God make you and all things?": "For his glory"
}

print(catechism["Who made you?"])
print(catechism["What else did God make?"])
print(catechism["Why did God make you and all things?"])

catechism["How can you glorify?"] = "By loving him and doing what he commands."

print(catechism["How can you glorify?"])


# next week we will look at conditional logic using if/else statements 
# and how to iterate over lists and dictionaries using loops