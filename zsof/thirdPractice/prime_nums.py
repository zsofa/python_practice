# Kérjen be egy pozitív egész számot a konzolról!
# Írassa ki egymás mellé a prímszámokat 1-től mindaddig, míg az összegük még nem éri el a bekért számot
# (tehát: ha már elérné vagy meghaladná, akkor azt a prímszámot már nem kell kiírni)!

num = int(input())
primes = []
if num > 1:
    for i in range(2, num):
        if num % i != 0:
            primes.append(i)

add = 0
for m in primes:
    add += m
    if add <= num:
        print(m)



