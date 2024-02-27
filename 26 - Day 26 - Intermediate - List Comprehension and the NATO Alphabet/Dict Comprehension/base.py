import random

names = ["Alex", "Bein", "Caroline", "Dave", "Elanour", "Freddie"]

# students_score = [key:value for item in listt]

students_score = {student: random.randint(1, 100) for student in names}
print(students_score)

passed_students = {student: score for (student, score) in students_score.items() if score >= 60}
