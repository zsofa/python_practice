# Írjunk Python-kódot két egész szám legkisebb közös többszörösének megtalálásához!
# Használjuk a "while" ciklust!

num1 = int(input())
num2 = int(input())


def lnko(a, b):
    while b != 0:
        a, b = b, a % b
    return a


lcm = (num1 * num2) // lnko(num1, num2)

print(lcm)
