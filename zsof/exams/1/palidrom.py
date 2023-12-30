# Valósítson meg palindrom(s1, s2) függvényt,
# ahol s1 és s2 egy-egy tetszőleges magyar vagy angol szöveg,
# az ábécé karaterein és szóközön kívül mást nem tartalmaznak.
# Döntse el, hogy a két szöveg palindromvagy sem.
# A függvény ennek megfelelő logikai értékkel térjen vissza.
# Két szöveg akkor palidrom, ha az egyik pontsan ugyanaz mint a másik visszafelé.
# Pl.: radar visszafelé is radar. A szóközök nem számítanak,
# és mindegy, hogy egy betű kicsi vagy nagy.


def palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalpha())
    return s == s[::-1]


print(palindrome("radAr"))
