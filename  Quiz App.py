# Quiz App
#Features:
#- Load questions from a file (CSV)
#- Score user answers


import csv

questions = []
with open("questions.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        questions.append(row)
score = 0
for q in questions:
    ans = input(q["q"] + " ")
    if ans.lower() == q["a"].lower():
        score += 1

print("Score: " + str(score) + "/" + str(len(questions)))
