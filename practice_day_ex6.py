#Create a dictionary of students and their scores, then print names of students who scored above 75.
students_scores = {
    "Kirtan" : 85,
    "Mayur" : 66,
    "Karan" : 90,
    "Rajveer" :77,}
high_scorers = [name for name, score in students_scores.items() if score > 75]

print("Students who scored above 75:" , high_scorers)

#Output:
#Students who scored above 75: ['Kirtan', 'Karan', 'Rajveer']

