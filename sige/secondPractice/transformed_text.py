# Kérjen be a konzolról egy tetszőleges hosszúságú, ékezetek nélküli szöveget!
# Cseréljen ki minden 'a ' betűt négyesre, minden 'e' betűt hármasra és minden 'o' betűt nullára!
# Elvárt kimenet:
# <modositott szoveg>

text = input()

output = text.replace('a', '4').replace('e', '3').replace('o', '0')
print(output)
