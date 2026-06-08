# Python Study Tracker project
# Mehmet Sur
# Date: 5/24/2026
# Description: Tracks Python study progress, scores, and motivation

# Challenge requirements:
# 1. Setup - dictionary with name, day, topics_mastered, scores
# 2. show_summary() - print name, day, topics count, average score
# 3. add_score() - append score, return updated list
# 4. get_motivation() - if/elif/else returning motivation message
# 5. for loop - go through 3 new scores, call both functions
# 6. average > 75 check + random tip of the day



import random
import math

student = {"name": "Mehmet",
            "day": 21,
            "topics_mastered": ["Python basics", "Git", "German A1"],
            "scores": [80, 60, 90]}


def show_summary(student):
    print(f"Name: {student['name']}")
    print(f"Day: {student['day']}")
    print(f"Topics mastered: {len(student['topics_mastered'])}")
    print(f"Average score: {math.floor(sum(student['scores']) / len(student['scores']))}")



def add_score(student, score):
    student["scores"].append(score)

    return student["scores"]




def get_motivation(score):
   if score >= 90:
       return "Ausgezeichnet! 🇩🇪"
   elif score >= 70:
       return "Good job, keep pushing!"
   else:
       return "Review this topic again."
   

new_scores = [85, 92, 60]

for score in new_scores:
    add_score(student, score)
    motivation = get_motivation(score)
    print(f"Score: {score} — {motivation}")



average = math.floor(sum(student["scores"]) / len(student["scores"]))
print(average > 75)


tips = [
    "Code every day, even 10 minutes counts!",
    "Review old code before writing new code.",
    "Read error messages carefully, they tell you exactly what's wrong."
]

print(random.choice(tips))

print("--------------------------------")

show_summary(student)