# Valósítson meg anagram(s1, s2) függvényt,
# ahol s1 és s2 egy-egy tetszőleges magyar vagy angol szöveg,
# az ábécé karaterein és szóközön kívül mást nem tartalmaznak.
# Döntse el, hogy a két szöveg anagramma vagy sem.
# A függvény ennek megfelelő logikai értékkel térjen vissza.
# Két szöveg akkor anagramma, ha pontosan ugyanazokat a karaktereket és ugyanakkora mennyiségben tartalmazzák.
# A szóközök nem számítanak, és mindegy, hogy egy betű kicsi vagy nagy.

def anagram(s1, s2):
    first_chars = {}
    second_chars = {}

    for char in s1.replace(" ", "").lower():
        if char in first_chars:
            first_chars[char] += 1
        else:
            first_chars[char] = 1

    for char in s2.replace(" ", "").lower():
        if char in second_chars:
            second_chars[char] += 1
        else:
            second_chars[char] = 1

    return first_chars == second_chars
