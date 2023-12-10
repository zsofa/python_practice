# Kérjünk be a konzolon egy pozitív egész számot!
# Rajzoljunk a konzolra úgy csillagokból piramist, hogy annyi sorból álljon, amekkora számot megadtunk.
# Minden sor 2-vel több csillagot tartalmazzon, mint a felette lévő!


num = int(input())

if num <= 0:
    num = int(input())

for i in range(1, num +1):
    star_num = 2 * i -1
    spaces = " " * (num -i)
    stars = "*" * star_num
    print(spaces + stars)