# importing the json module
import json

# reads the json file and returns the data as a dictionary
def open_json(file_path):
    with open(file_path) as file:
        data = json.load(file)
        return data

# computes the final score at the end of the quiz
def compute_final_score(score, total_questions):
    return score / total_questions * 100

# global variables

# special characters
new_line = "\n"
tab_space = "\t"

# integer to keep track of the user's score
score = 0

catechism_json_file_path = "catechism.json"

# welcome message string
welcome_message = "Welcome to the Children's Catechism Quiz!"

 # open the json file and return the data as a dictionary
catechism_data = open_json(catechism_json_file_path)

# get the questions from the dictionary
questions = catechism_data["questions"]

# get the total number of questions
total_questions = len(questions)

print(new_line)
print(welcome_message)
print(new_line)
print("You will be asked " + str(total_questions) + " questions (multiple choice). Each question has 4 options. Type the number of the option you think is correct. You will be given 1 point for each correct answer.")
print(new_line)

# loop through the questions
for question in questions:
    # display the question to the user
    print(question["question"])
    print(new_line)

    # get the options from the dictionary
    options = question["options"]

    # display the options to the user
    # i is the index of the option
    for i in range(len(options)):
        print(tab_space + str(i) + ") " + options[i])

    print(new_line)

     # get the correct answer from the dictionary
    correct_answer = question["answer"]

    # get the user's answer
    user_answer = input("Your answer: ")
    print(new_line)

    index = int(user_answer)

    # check if the user's answer is correct
    if options[index] == correct_answer:
        print("Correct!")
        score = score + 1
    else:
        print("Incorrect!")
        print(new_line)
        print("The correct answer is: " + correct_answer)
    print(new_line)


print("Your score is: " + str(compute_final_score(score, total_questions)))
print(new_line)




