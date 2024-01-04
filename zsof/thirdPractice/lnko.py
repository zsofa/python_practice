# Írjunk Python-kódot két egész szám legnagyobb közös osztójának megtalálásához!
# Használjuk a "while" ciklust!

num1 = int(input())
num2 = int(input())


def lnko(a, b):
    while b != 0:
        a, b = b, a % b
    return a


fin = lnko(num1, num2)
print(fin)
