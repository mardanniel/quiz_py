import os
import random as rand
import re

# Check absolute path of your system 
# print(os.getcwd())
again = False
# Open and read file
# You can put the quizfile.txt in the absolute path of your system or somewhere else (ex. open("C:\Users\*chosen_folder*\quizfile.txt", "r"))
file = open("quizfilesample.txt", "r")
lines = file.readlines()
# Make a pair list of question and answerR
lines = list(line.split(' | ') for line in lines)
# Remove all white spaces, new lines and tabs 
for i in range(len(lines)):
    lines[i][1] = re.sub(r"[\n\t\s]*","",lines[i][1])
# Contains your score
score = 0
incorrect = []
while again != True:
    # Randomize questions
    sampled_lines = rand.sample(lines, len(lines)) 
    # Read every randomized questions
    for i in range(len(sampled_lines)):
        ans = str(input(sampled_lines[i][0]+" | Your answer: "))
        ans = re.sub(r"[\n\t\s]*","",ans)
        if ans.lower() == sampled_lines[i][1].lower():
            score += 1
        else:
            incorrect.append([sampled_lines[i][0].lower(), sampled_lines[i][1].lower(), ans])
    print("Your score:",score,"/",len(sampled_lines))
    print("Incorrect Answers:")
    print(*incorrect, sep=" ")
    again = bool(input("Again? Type True or False: "))
    os.system('cls')
file.close() 

