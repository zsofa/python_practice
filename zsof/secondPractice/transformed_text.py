# Kérjen be a konzolról egy tetszőleges hosszúságú, ékezetek nélküli szöveget!
# Cseréljen ki minden 'a ' betűt négyesre, minden 'e' betűt hármasra és minden 'o' betűt nullára!
# Elvárt kimenet:
# <modositott szoveg>

text = str(input())


def change_text(input_text):
    return input_text.replace('a', '4').replace('e', '3').replace('o', '0')


print(change_text(text))

