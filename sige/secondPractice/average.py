# Készítsen Python-programot, amely bekéri 5 érettségi tárgy érdemjegyét, és kiírja azok átlagát!

sum = 0

for _ in range(5):
    num = int(input())
    sum += num

print(sum/5)
