# Valósítson meg anagram(s1, s2) függvényt,
# ahol s1 és s2 egy-egy tetszőleges magyar vagy angol szöveg,
# az ábécé karaterein és szóközön kívül mást nem tartalmaznak.
# Döntse el, hogy a két szöveg anagramma vagy sem.
# A függvény ennek megfelelő logikai értékkel térjen vissza.
# Két szöveg akkor anagramma, ha pontosan ugyanazokat a karaktereket és ugyanakkora mennyiségben tartalmazzák.
# A szóközök nem számítanak, és mindegy, hogy egy betű kicsi vagy nagy.

def anagram(s1, s2):
    final1 = ''
    final2 = ''
    list_of_letters1 = []
    list_of_letters2 = []

    if ' ' in s1:
        final1 = s1.replace(' ', '').lower()
    else:
        final1 = s1.lower()

    if ' ' in s2:
        final2 = s2.replace(' ', '').lower()
    else:
        final2 = s2.lower()

    if final1.isalpha() and final2.isalpha():
        for i in final1:
            list_of_letters1.append(i)

        for j in final2:
            list_of_letters2.append(j)

        if set(list_of_letters1) == set(list_of_letters2):
            return True
        else:
            return False
    else:
        return False


print(anagram("dán ropifgggwgestő", "petőfi Sándor"))
