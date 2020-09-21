import os
import random as rand
import re

# Check absolute path of your system 
# print(os.getcwd())
again = False
# Open and read file
# You can put the quizfile.txt in the absolute path of your system or somewhere else (ex. open("C:\Users\*chosen_folder*\quizfile.txt", "r"))
file = open("C:/Users/-/Desktop/quizfilesample.txt", "r", encoding="utf-8")
lines = file.readlines()
# Make a pair list of question and answerR
lines = list(line.split(' | ') for line in lines)
# Remove all white spaces, new lines and tabs 
for i in range(len(lines)):
    lines[i][len(lines[i])-1] = re.sub(r"[\n\t\s]*","",lines[i][len(lines[i])-1])
passing_score = round(len(lines) * 0.7)
print("No. of Questions:",len(lines))
print("Passing score:", passing_score)
print("Allowed attempts: Unlimited")
while again != True:
    # Contains your score
    score = 0 
    # Contains incorrect answers, format : [*question*, *answer*, *your_answer*]
    incorrect = []  
    # Randomize questions
    sampled_lines = rand.sample(lines, len(lines)) 
    # Read every randomized questions
    for i in range(len(sampled_lines)):
        ans = str(input(str(i+1)+". "+sampled_lines[i][0]+" | Your answer: "))
        ans = re.sub(r"[\n\t\s]*","",ans)

        if ans.lower() == sampled_lines[i][1].lower():
            score += 1
        else:
            incorrect.append([sampled_lines[i][0].lower(), "Correct answer; "+sampled_lines[i][1].lower(), "Your answer: "+ans])
    print("Your score:",score,"/",len(sampled_lines))
    print("You Passed!" if score >= passing_score else "You Failed!")
    print("Incorrect Answers:")
    print(*incorrect, sep="\n")
    again = bool(input("Again? Type True or False: "))
    os.system('cls')
file.close() 

