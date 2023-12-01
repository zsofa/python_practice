# Készítsen Python-programot, amely bekéri 5 érettségi tárgy érdemjegyét, és kiírja azok átlagát!

grades = []
for i in range(5):
    grade = int(input())
    grades.append(grade)


print(sum(grades) / len(grades))